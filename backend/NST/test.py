import jittor as jt
import torch


t = jt.float32([[[[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]],[[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]]],[[[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]],[[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]]]])
print(t.data)
print(torch.tensor(t.data))

# print(t)
# print(t.shape)
# print(f)
# print(f.shape)
# print(r)
# print(r.shape)
# print(x)
# print(y)
# print(z)