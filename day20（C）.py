#       实验数据综合分析
import numpy as np
import matplotlib.pyplot as plt

times = np.linspace(0.1, 0.7, 7)      # 时间 (s)
experiment_positions = np.array([0.05, 0.20, 0.44, 0.79, 1.22, 1.76, 2.39]) # 位移 (m)
p_errors = np.array([0.02, 0.02, 0.03, 0.03, 0.04, 0.04, 0.05])  # 位移测量误差 (m)
fig, axes = plt.subplots(1,2)
axes[0].errorbar(times,experiment_positions,yerr=p_errors,color="red",label="Experiment")
axes[0].set_xlabel("Times (s)")
axes[0].set_ylabel("Positions (m)")
axes[0].set_title("Experiment (p-t)")
axes[0].grid(True)
axes[0].legend()

t_squared = times**2
axes[1].scatter(t_squared,experiment_positions,color="green",label="Experiment")
result = np.polyfit(t_squared,experiment_positions,1)
slope = result[0]
intercept = result[1]
fit_line = slope * t_squared + intercept
axes[1].plot(t_squared,fit_line,color="blue",label="Fit")
axes[1].set_xlabel("t*t (s*s)")
axes[1].set_ylabel("Positions (m)")
axes[1].set_title("Fit (p-t*t)")
axes[1].grid(True)
axes[1].legend()
plt.show()

g = 9.8
g_experiment = 2*slope
print("The G Of Experiment: ", g_experiment, "m/(s*s)")
error_g = (abs(g_experiment - g)/g) * 100
print("The Error Of G: ", error_g, "%")
#     print(f"The G Of Experiment: {g_experiment:.3f}m/(s*s), The Error Of G: {error_g:.2f}%")