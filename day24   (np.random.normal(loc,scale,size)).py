#       随机数据模拟
import numpy as np

np.random.seed(1)   # 固定种子,方便你和我对结果

g = 9.8
times = np.linspace(0.1, 1.0, 10)   # 10个时间点
s_true = 0.5 * g * times**2         # 理论位移(无噪声)
noise = np.random.normal(loc=0, scale=0.05, size=10)
s_measured = s_true + noise
print(s_true)
print(s_measured)