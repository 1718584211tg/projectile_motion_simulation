#     导入函数
from physics_functions import get_number, calculate_kinetic_energy
mass = get_number("Please enter the mass: ")
velocity = get_number("Please enter the velocity: ")
energy = calculate_kinetic_energy(mass,velocity)
print("Kinetic Energy: ", energy, "J")