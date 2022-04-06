import jittor as jt


t = jt.float32([[[[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]],[[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]]],[[[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]],[[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]]]])
B, C, H, W = t.size()
# x = t.index_fill(2, torch.tensor([H-1, H-2, H-3]), -1)
# y = t.index_fill(3, torch.tensor([W-1, W-2]), -1)
z = t.add(-1)
print(t.view(C,-1))

# f = x.flatten()
# pos = (f==-1).nonzero()
# # print(pos)
# b = torch.cat([torch.cat((f[0:i],f[i+1:])) for i in pos])
# print(b.shape)
# r = f.view(B,C,H,W)
print(t.shape)
# d = t[:,:,2:,:]
# print(d)
f = t[:,:,:,:-2]
print(f)
print(f.shape)
B, C, H, W = f.size()
print(f.view(C,-1))

# print(t)
# print(t.shape)
# print(f)
# print(f.shape)
# print(r)
# print(r.shape)
# print(x)
# print(y)
# print(z)