#       numpy数组shape与reshape
import numpy as np

temp_data = np.array([20.1, 20.3, 20.5, 20.6,
                       21.0, 21.2, 21.5, 21.7,
                       19.8, 19.9, 20.0, 20.2])
print(temp_data.shape)
temp_grid = temp_data.reshape(3,4)
print(temp_grid)
print(temp_grid.shape)

#     print(temp_grid[1,:])
#     print(temp_grid[:,2])
#     print(temp_grid[2,0])
#     print(temp_grid[:2,:])
#     print(temp_grid[1,1:4])

print(temp_grid.mean(axis=1))   # 任务1
print(temp_grid.mean(axis=0))   # 任务2
print(temp_grid.max(axis=1))       # 任务3
