#     numpy二维数组数据提取
import numpy as np
data = np.array([
    [0,0],
    [1,3],
    [2,8],
    [3,15],
    [4,24]
])
times = data[:,0]
positions = data[:,1]
print(times)
print(positions)
average_velocity = (positions[-1] - positions[0])/(times[-1]-times[0])
print("The Average Velocity is: ", average_velocity, "m/s")
average_velocity1 = (positions[3]-positions[1])/(times[3]-times[1])
print("The Average Velocity1 is: ", average_velocity1, "m/s")