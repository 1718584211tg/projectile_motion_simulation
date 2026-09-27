#     动能计算函数
def calculate_kinetic_energy(mass,velocity):
    kinetic_energy = 0.5 * mass * velocity**2
    return kinetic_energy
mass = float(input("Enter mass (kg): "))
velocity = float(input("Enter velocity (m/s): "))
kinetic_energy = calculate_kinetic_energy(mass, velocity)
print("The kinetic energy is ", kinetic_energy, "Joules.")

#     自由落体计算函数
def calculate_free_fall(height):
    g = 9.8
    time = (2*height/g)**0.5
    velocity = (2*g*height)**0.5
    return time, velocity
height = float(input("Enter height (m):"))
time, velocity = calculate_free_fall(height)
print("The time taken to fall is ", time, "seconds.")
print("The velocity when hitting the ground is ", velocity, "m/s.")

#     物体运动状态分析函数
def analyze_motion(mass,velocity):
    energy = 0.5*mass*velocity**2
    if energy < 100:
        motion_state = "The object is in a low energy state"
    elif energy < 500:
        motion_state = "The object is in a medium energy state"
    else:
        motion_state = "The object is in a high energy state"
    return energy,motion_state
mass = float(input("Enter object mass (kg): "))
velocity = float(input("Enter object velocity (m/s): "))
energy, state = analyze_motion(mass, velocity)
print("The kinetic energy is ", energy, "Joules.")
print(state)