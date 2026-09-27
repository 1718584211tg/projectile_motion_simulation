#     matplotlib
import numpy as np
import matplotlib.pyplot as plt
g = 9.8
times = np.linspace(0,10,100)
positions = 0.5*g*times**2
velocities = g*times
plt.plot(times,positions,color="blue",linestyle="-",linewidth=3,label="Object Falling")
plt.plot(times,velocities,color="green",linestyle="--",linewidth=2,label="Velocity")
#      linestyle="--"(虚）/"-"(实)/":"(点)/"-."(点划)
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Free Fall Motion")
plt.grid(True)
plt.legend()
plt.show()
 