#     数组基本操作
from physics_functions import calculate_kinetic_energy
import numpy as np
velocities = np.array([5,10,15,20,25])
print(velocities.shape)
print(velocities.size)
print(velocities[1])
print(velocities[0:3])
num1 = np.arange(0,10,2)   #   np.arange(start,stop,step)
num2 = np.linspace(0,20,5)   #   np.linspace(start,stop,num)
print(num1)
print(num2)
masses = np.array([2,2,2,2,2])
energies = calculate_kinetic_energy(masses,velocities)
print("Kinetic Energies: ", energies, "(J)")