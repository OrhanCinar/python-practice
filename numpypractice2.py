import numpy as np
import sys

# a = np.array([1, 2, 3], dtype='int32')
# print('1d', a)

# b = np.array([
#     [1, 2, 3, 5, 6, 9, 8, 7],
#     [9, 8, 7, 22, 369, 45, 6858, 85]
# ])
# print('2d', b)

# print("dim", b.ndim)
# print("shape", b.shape)
# print("type", b.dtype)
# print("size", b.itemsize)
# print("total size", b.size)
# print(b[0, -2])

# print(b[0, :]) rows
# print(b[:, 2]) columns
# b[1, 5] = 999
# c = np.array([[[1, 1], [2, 2]], [[3, 3], [7, 8]]])  # 3d
# print(c[0:1, 0])
# c[:, 1, :] = [[9, 9], [8, 8]]  # replace

# a = np.zeros((2, 3, 3))
# a = np.ones((2, 3, 3))
# a = np.ones_like((2, 3, 3))
# a = np.full((2, 2), 99, dtype='float32')

# a = np.full_like((2, 2), 99, dtype='float32')

# random decimal
# a = np.random.rand(4, 2, 3)
# a = np.random.randint(40, size=(3, 3))
# np.identity(9)
# a = np.array([[1, 2, 3]])
# r1 = np.repeat(a, 3, axis=0)

# union
# a = np.ones((5, 5))
# z = np.zeros((3, 3))
# z[1, 1] = 9
# a[1:4, 1:-1] = z

# copy
# a = np.array([1, 2, 3])
# b = a.copy()

# a[0] = 9

# a = np.array([1, 2, 3, 4], dtype='float32')
# b = np.array([4, 3, 2, 1])
# a *= 2

# a = np.ones((2, 3))
# b = np.full((3, 2), 2)
# c = np.matmul(a, b)

# c = np.identity(3)
# d = np.linalg.det(c)

#a = np.array([[1, 1, 1, 1], [2, 2, 2, 2]])
# max = np.max(a, axis=1)
# sum = np.sum(a)
#b = a.reshape(-1, 4)
v1 = np.array([[1, 1, 1, 1]])
v2 = np.array([[2, 2, 2, 2]])

#vstack = np.vstack([v1, v2, v1, v2, v1])
hstack = np.hstack([v1, v2, v1, v2, v1])

print(hstack)
