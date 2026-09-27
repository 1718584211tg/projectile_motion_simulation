#        计算器
def calculate_kinetic_energy(mass, velocity):
    energy = 0.5*mass*velocity**2
    return energy
def calculate_free_fall(height):
    g = 9.8
    time = (2*height/g)**0.5
    velocity = (2*g*height)**0.5
    return time,velocity   
def analyze_motion(mass, velocity):
    energy = 0.5*mass*velocity**2
    if energy <  100:
        motion_state = "The object is in low energy state"
    elif energy < 500:
        motion_state = "The object is in medium energy state"
    else:
        motion_state = "The object is in high energy state"
    return energy, motion_state
print("   Physics Calculator    ")
print("1. Calculate Kinetic Energy")
print("2. Calculate Free Fall")
print("3. Analyze Motion")
mode = input("Please choose an option(1-3):")
if mode == "1":   #   “==”判断是否等于；注意数字1两边加引号“1”
    mass = float(input("Please enter the mass(kg): "))
    velocity = float(input("Please enter the velocity(m/s): "))
    energy = calculate_kinetic_energy(mass, velocity)
    print("The kinetic energy is ", energy ,"Joules")
elif mode == "2":
    height = float(input("Please enter the height: "))
    time,velocity = calculate_free_fall(height)
    print("The time taken to fall is ", time ,"seconds")
    print("The final velocity is ", velocity ,"m/s")
elif mode == "3":
    mass = float(input("Please enter the mass(kg): "))
    velocity = float(input("Please enter the velocity(m/s): "))
    energy,state = analyze_motion(mass, velocity)
    print("The kinetic energy is ", energy ,"Joules")
    print(state)
else:
    print("Invalid input")