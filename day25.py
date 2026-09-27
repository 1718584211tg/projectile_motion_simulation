#       numpy综合
import numpy as np
np.random.seed(2)

g = 9.8
times = np.linspace(0.1, 1.0, 10)      # 10个时间点
s_true = 0.5 * g * times**2             # 理论位移，shape (10,)
noise = np.random.normal(loc=0,scale=0.05,size=50)
noise_ex = noise.reshape(5,10)
s_measurements = s_true + noise_ex
s_average = s_measurements.mean(axis=0)
s_error = s_measurements.std(axis=0)
print(times)
print(s_average)
print(s_error)