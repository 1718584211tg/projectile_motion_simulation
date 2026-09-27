#     曲线拟合
import numpy as np
import matplotlib.pyplot as plt
times = np.linspace(0,2.5,6)
experiment_positions = [0, 1.3, 5.2, 11.0, 20.4, 29.5]
t_squared = times**2

result = np.polyfit(t_squared,experiment_positions,1)
slope = result[0]
intercept = result[1]
print(slope)
print(intercept)
g_experiment = 2*slope
print(g_experiment)