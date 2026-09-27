#     numpy二维数组
import numpy as np
data = np.array([
    [0, 0.0],
    [1, 2.5],
    [2, 10.0]
])
print(data.shape)
print(data.size)
print(data[1,1])
print(data[2,:])
print(data[:,1])