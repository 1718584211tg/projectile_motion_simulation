#   元组数据(Tuple)   注：不可像List一样修改数据
position = (10, 20)
print(position)
print(position[0])  # 输出第一个元素
print(position[1])  # 输出第二个元素
x , y = position   #只拿前面一个数: x, *_ = position ；拿前两个同理
print(x, y)

#   物体元组数据
motion_date = (5, 20, 100)
mass,velocity,height = motion_date
kinetic_energy = 0.5*mass*velocity**2
print("The object's mass is ", mass, "kg")
print("The object's velocity is ", velocity, "m/s")
print("The object's height is ", height, "m")
print("The object's kinetic energy is ", kinetic_energy, "Joules")

#   数据计算
def calculate(mass, velocity):
    kinetic_energy = 0.5*mass*velocity**2
    momentum = mass*velocity
    return kinetic_energy, momentum
mass = float(input("Enter mass(kg):"))
velocity = float(input("Enter velocity(m/s):"))
energy, momentum = calculate(mass, velocity)
print("The objecte's kinetic energy is:", energy, "Joules")
print("The objecte's momentum is:", momentum, "kg*m/s")

