from warnings import warn
import numpy as np
import numexpr as ne
from scipy.ndimage import uniform_filter, gaussian_filter
from scipy.ndimage.filters import convolve

from skimage.util.dtype import dtype_range
from skimage.util.arraycrop import crop
from skimage._shared.utils import warn, check_shape_equality

import argparse

def _as_floats(image0, image1):
    """
    Promote im1, im2 to nearest appropriate floating point precision.
    """
    float_type = np.result_type(image0.dtype, image1.dtype, np.float32)
    image0 = np.asarray(image0, dtype=float_type)
    image1 = np.asarray(image1, dtype=float_type)
    return image0, image1

def structural_similarity(im1, im2,
                          *,
                          win_size=None, gradient=False, data_range=None,
                          multichannel=False, gaussian_weights=False,
                          full=False, **kwargs):
    """
    Compute the mean structural similarity index between two images.
    Parameters
    ----------
    im1, im2 : ndarray
        Images. Any dimensionality with same shape.
    win_size : int or None, optional
        The side-length of the sliding window used in comparison. Must be an
        odd value. If `gaussian_weights` is True, this is ignored and the
        window size will depend on `sigma`.
    gradient : bool, optional
        If True, also return the gradient with respect to im2.
    data_range : float, optional
        The data range of the input image (distance between minimum and
        maximum possible values). By default, this is estimated from the image
        data-type.
    multichannel : bool, optional
        If True, treat the last dimension of the array as channels. Similarity
        calculations are done independently for each channel then averaged.
    gaussian_weights : bool, optional
        If True, each patch has its mean and variance spatially weighted by a
        normalized Gaussian kernel of width sigma=1.5.
    full : bool, optional
        If True, also return the full structural similarity image.
    Other Parameters
    ----------------
    use_sample_covariance : bool
        If True, normalize covariances by N-1 rather than, N where N is the
        number of pixels within the sliding window.
    K1 : float
        Algorithm parameter, K1 (small constant, see [1]_).
    K2 : float
        Algorithm parameter, K2 (small constant, see [1]_).
    sigma : float
        Standard deviation for the Gaussian when `gaussian_weights` is True.
    Returns
    -------
    mssim : float
        The mean structural similarity index over the image.
     cs : float
        The mean contrast sensitivity over the image. This is used for the multiscaled SSIM metrics
    grad : ndarray
        The gradient of the structural similarity between im1 and im2 [2]_.
        This is only returned if `gradient` is set to True.
    S : ndarray
        The full SSIM image.  This is only returned if `full` is set to True.
    Notes
    -----
    To match the implementation of Wang et. al. [1]_, set `gaussian_weights`
    to True, `sigma` to 1.5, and `use_sample_covariance` to False.
    .. versionchanged:: 0.16
        This function was renamed from ``skimage.measure.compare_ssim`` to
        ``skimage.metrics.structural_similarity``.
    References
    ----------
    .. [1] Wang, Z., Bovik, A. C., Sheikh, H. R., & Simoncelli, E. P.
       (2004). Image quality assessment: From error visibility to
       structural similarity. IEEE Transactions on Image Processing,
       13, 600-612.
       https://ece.uwaterloo.ca/~z70wang/publications/ssim.pdf,
       :DOI:`10.1109/TIP.2003.819861`
    .. [2] Avanaki, A. N. (2009). Exact global histogram specification
       optimized for structural similarity. Optical Review, 16, 613-621.
       :arxiv:`0901.0065`
       :DOI:`10.1007/s10043-009-0119-z`
    """
    check_shape_equality(im1, im2)

    if multichannel:
        # loop over channels
        args = dict(win_size=win_size,
                    gradient=gradient,
                    data_range=data_range,
                    multichannel=False,
                    gaussian_weights=gaussian_weights,
                    full=full)
        args.update(kwargs)
        nch = im1.shape[-1]
        mssim = np.empty(nch)
        cs = np.empty(nch)
        if gradient:
            G = np.empty(im1.shape)
        if full:
            S = np.empty(im1.shape)
        for ch in range(nch):
            ch_result = structural_similarity(im1[..., ch],
                                              im2[..., ch], **args)
            if gradient and full:
                mssim[..., ch], cs[..., ch], G[..., ch], S[..., ch] = ch_result
            elif gradient:
                mssim[..., ch], cs[..., ch], G[..., ch] = ch_result
            elif full:
                mssim[..., ch], cs[..., ch], S[..., ch] = ch_result
            else:
                mssim[..., ch], cs[..., ch] = ch_result
        mssim = mssim.mean()
        cs = cs.mean()

        if gradient and full:
            return mssim, cs, G, S
        elif gradient:
            return mssim, cs, G
        elif full:
            return mssim, cs, S
        else:
            return mssim, cs

    K1 = kwargs.pop('K1', 0.01)
    K2 = kwargs.pop('K2', 0.03)
    sigma = kwargs.pop('sigma', 1.5)
    if K1 < 0:
        raise ValueError("K1 must be positive")
    if K2 < 0:
        raise ValueError("K2 must be positive")
    if sigma < 0:
        raise ValueError("sigma must be positive")
    use_sample_covariance = kwargs.pop('use_sample_covariance', True)

    if gaussian_weights:
        # Set to give an 11-tap filter with the default sigma of 1.5 to match
        # Wang et. al. 2004.
        truncate = 3.5

    if win_size is None:
        if gaussian_weights:
            # set win_size used by crop to match the filter size
            r = int(ne.evaluate("truncate * sigma + 0.5"))  # radius as in ndimage
            win_size = ne.evaluate("2 * r + 1")
        else:
            win_size = 7   # backwards compatibility

    if np.any((np.asarray(im1.shape) - win_size) < 0):
        raise ValueError(
            "win_size exceeds image extent.  If the input is a multichannel "
            "(color) image, set multichannel=True.")

    if not (win_size % 2 == 1):
        raise ValueError('Window size must be odd.')

    if data_range is None:
        if im1.dtype != im2.dtype:
            warn("Inputs have mismatched dtype.  Setting data_range based on "
                 "im1.dtype.", stacklevel=2)
        dmin, dmax = dtype_range[im1.dtype.type]
        data_range = dmax - dmin

    ndim = im1.ndim

    if gaussian_weights:
        filter_func = gaussian_filter
        filter_args = {'sigma': sigma, 'truncate': truncate}
    else:
        filter_func = uniform_filter
        filter_args = {'size': win_size}

    # ndimage filters need floating point data
    im1 = im1.astype(np.float64)
    im2 = im2.astype(np.float64)

    NP = win_size ** ndim

    # filter has already normalized by NP
    if use_sample_covariance:
        cov_norm = NP / (NP - 1)  # sample covariance
    else:
        cov_norm = 1.0  # population covariance to match Wang et. al. 2004

    # compute (weighted) means
    ux = filter_func(im1, **filter_args)
    uy = filter_func(im2, **filter_args)

    # compute (weighted) variances and covariances
    uxx = filter_func(ne.evaluate("im1 * im1"), **filter_args)
    uyy = filter_func(ne.evaluate("im2 * im2"), **filter_args)
    uxy = filter_func(ne.evaluate("im1 * im2"), **filter_args)
    vx = ne.evaluate("cov_norm * (uxx - ux * ux)")
    vy = ne.evaluate("cov_norm * (uyy - uy * uy)")
    vxy = ne.evaluate("cov_norm * (uxy - ux * uy)")

    R = data_range
    C1 = ne.evaluate("(K1 * R) ** 2")
    C2 = ne.evaluate("(K2 * R) ** 2")

    A1, A2, B1, B2 = ((ne.evaluate("2 * ux * uy + C1"),
                       ne.evaluate("2 * vxy + C2"),
                       ne.evaluate("ux ** 2 + uy ** 2 + C1"),
                       ne.evaluate("vx + vy + C2")))
    D = ne.evaluate("B1 * B2")
    S = ne.evaluate("(A1 * A2) / D")

    # to avoid edge effects will ignore filter radius strip around edges
    pad = (win_size - 1) // 2

    # compute (weighted) mean of ssim
    mssim = crop(S, pad).mean()
    cs=np.mean(ne.evaluate("A2/B2")) #used for multiscaled

    if gradient:
        # The following is Eqs. 7-8 of Avanaki 2009.
        grad = filter_func(ne.evaluate("A1 / D"), **filter_args) * im1
        grad += filter_func(ne.evaluate("-S / B2"), **filter_args) * im2
        grad += filter_func(ne.evaluate("(ux * (A2 - A1) - uy * (B2 - B1) * S) / D"),
                            **filter_args)
        grad *= (2 / im1.size)

        if full:
            return mssim, cs, grad, S
        else:
            return mssim, cs, grad
    else:
        if full:
            return mssim, cs, S
        else:
            return mssim, cs


def multiscale_structural_similarity(im1, im2,*,win_size=None, data_range=None, multichannel=False, gaussian_weights=False):
    check_shape_equality(im1, im2)
    weights = np.array([0.0448, 0.2856, 0.3001, 0.2363, 0.1333])
    levels = weights.size
    downsample_filter = np.ones((2, 2, 1)) / 4.0
    mssim = np.array([])
    mcs = np.array([])

    for _ in range(levels):
        ssim, cs = structural_similarity(im1, im2, win_size=win_size,data_range=data_range,multichannel=multichannel, gaussian_weights=gaussian_weights)
        mssim = np.append(mssim, ssim)
        mcs = np.append(mcs, cs)
        filtered = [convolve(im, downsample_filter, mode='reflect') for im in [im1, im2]]
        im1, im2 = [x[::2, ::2, :] for x in filtered]

    return (np.prod(mcs[0:levels-1] ** weights[0:levels-1]) * (mssim[levels-1] ** weights[levels-1]))


def peak_signal_noise_ratio(image_true, image_test, *, data_range=None):
    """
    Compute the peak signal to noise ratio (PSNR) for an image.
    Parameters
    ----------
    image_true : ndarray
        Ground-truth image, same shape as im_test.
    image_test : ndarray
        Test image.
    data_range : int, optional
        The data range of the input image (distance between minimum and
        maximum possible values).  By default, this is estimated from the image
        data-type.
    Returns
    -------
    psnr : float
        The PSNR metric.
    Notes
    -----
    .. versionchanged:: 0.16
        This function was renamed from ``skimage.measure.compare_psnr`` to
        ``skimage.metrics.peak_signal_noise_ratio``.
    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio
    """
    check_shape_equality(image_true, image_test)

    if data_range is None:
        if image_true.dtype != image_test.dtype:
            warn("Inputs have mismatched dtype.  Setting data_range based on "
                 "im_true.", stacklevel=2)
        dmin, dmax = dtype_range[image_true.dtype.type]
        true_min, true_max = np.min(image_true), np.max(image_true)
        if true_max > dmax or true_min < dmin:
            raise ValueError(
                "im_true has intensity values outside the range expected for "
                "its data type.  Please manually specify the data_range")
        if true_min >= 0:
            # most common case (255 for uint8, 1 for float)
            data_range = dmax
        else:
            data_range = dmax - dmin

    image_true, image_test = _as_floats(image_true, image_test)

    err = mean_squared_error(image_true, image_test)
    return 10 * np.log10((data_range ** 2) / err)

def mean_squared_error(image0, image1):
    """
    Compute the mean-squared error between two images.
    Parameters
    ----------
    image0, image1 : ndarray
        Images.  Any dimensionality, must have same shape.
    Returns
    -------
    mse : float
        The mean-squared error (MSE) metric.
    """
   
    check_shape_equality(image0, image1)
    image0, image1 = _as_floats(image0, image1)
    return np.mean(ne.evaluate("(image0 - image1) ** 2"), dtype=np.float64)

if __name__ == '__main__':
    pass