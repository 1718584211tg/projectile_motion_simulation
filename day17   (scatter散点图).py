#     实验数据图像
import numpy as np
import matplotlib.pyplot as plt
g = 9.8
times = np.linspace(0,2.5,6)
theory_positions = 0.5*g*times**2
experiment_positions = [0, 1.3, 5.2, 11.0, 20.4, 29.5]
plt.plot(times,theory_positions,color="green",label="Theory")
plt.scatter(times,experiment_positions,color="red",label="Experiment")
plt.xlabel("Times (s)")
plt.ylabel("Positions (m)")
plt.title("Free Fall Motion")
plt.grid(True)
plt.legend()
plt.show()