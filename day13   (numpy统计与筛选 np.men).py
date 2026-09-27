#     numpy统计与数据筛选
import numpy as np
from physics_functions import calculate_kinetic_energy
velocities = np.array([3,8,12,18,25,30])
print(np.mean(velocities))
print(np.max(velocities))
print(np.min(velocities))
print(velocities[velocities > 15])
masses = np.array([2,2,2,2,2,2])
kinetic_energies = calculate_kinetic_energy(masses, velocities)
print(kinetic_energies[kinetic_energies > 200])