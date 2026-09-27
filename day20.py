#     数据综合分析
import numpy as np
import matplotlib.pyplot as plt
g = 9.8
times = np.linspace(0, 2.5, 6)
experiment_positions = [0, 1.3, 5.2, 11.0, 20.4, 29.5]
errors = [0.05, 0.1, 0.13, 0.19, 0.26, 0.33]
theory_positions = 0.5*g*times**2
t_squared = times**2
result = np.polyfit(t_squared,experiment_positions,1)
slope = result[0]
intercept = result[1]
s = slope*t_squared+intercept
g_experiment = 2*slope
print("The G oF Experiment: ", g_experiment, "m/(s*s)")
plt.plot(times,theory_positions,color="green",label="Theory")
plt.errorbar(times,experiment_positions,yerr=errors,label="Experiment")
plt.title("Free Fall Experiment")
plt.xlabel("Times (s)")
plt.ylabel("Positions (m)")
plt.grid(True)
plt.legend()
plt.show()