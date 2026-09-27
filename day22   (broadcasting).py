#       broadcasting
import numpy as np

temp_data = np.array([20.1, 20.3, 20.5, 20.6,
                       21.0, 21.2, 21.5, 21.7,
                       19.8, 19.9, 20.0, 20.2])

temp_grid = temp_data.reshape(3,4)
temp_grid_K = temp_grid + 273.15
print(temp_grid_K)
position_means = temp_grid.mean(axis=1)
print(position_means)
position_means_exchange = position_means.reshape(3,1)
anomaly = temp_grid - position_means_exchange
print(anomaly)