#     多子图subplots
import numpy as np
import matplotlib.pyplot as plt
g = 9.8
times = np.linspace(0,5,100)
positions = 0.5*g*times**2
velocities = g*times
fig, axes = plt.subplots(2,1)
axes[0].plot(times,positions,color="red",label="Positions-Times")
axes[1].plot(times,velocities,color="green",label="Velocities-Times")
axes[0].set_xlabel("Times (s)")
axes[0].set_ylabel("Positions (m)")
axes[1].set_xlabel("Times (s)")
axes[1].set_ylabel("Velocities (m/s)")
axes[0].grid(True)
axes[1].grid(True)
axes[0].legend()
axes[1].legend()
plt.show()