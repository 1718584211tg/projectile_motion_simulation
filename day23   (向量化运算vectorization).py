#       向量化运算
import numpy as np

sensor_data = np.array([21.3, 22.1, -999.0, 20.8, 21.5, -999.0, 22.3, 19.9])
clean_data = np.where(sensor_data != -999.0, sensor_data, np.nan)
print(clean_data)
print(np.nanmean(clean_data))
print(np.mean(sensor_data))