#     NumPy
import numpy as np
from physics_functions import calculate_kinetic_energy
masses = np.array([2,5,3])
velocities = np.array([10,20,15])
energies = calculate_kinetic_energy(masses,velocities)
print("Kinetic Energies:", energies, "(J)")
