#     异常处理
#   try :
#       mass = float(input("Please enter the mass: "))
#       velocity = float(input("Please enter the velocity: "))
#       kinetic_energy = 0.5*mass*velocity**2
#       print("Kinetic Energy: ", kinetic_energy, "J")
#   except :
#       print("输入错误，请输入数字")

#     while + try/except
while True:
    try :
        mass = float(input("Please enter the mass: "))
        velocity = float(input("Please enter the velocity: "))
        energy = 0.5*mass*velocity**2
        print("Kinetic Energy: ", energy, "J")
        break
    except :
        print("输入错误，请输入数字！")

#     quiz
while True:
    try :
        mass = float(input("Please enter mass: "))
        print("The Mass: ", mass, "kg")
        break
    except :
        print("输入错误，请输入数字！")

#     动能计算器
while True:
    try :
        mass = float(input("Please enter mass: "))
        break
    except ValueError :
        print("输入错误，请重新输入质量！")
while True:
    try :
        velocity = float(input("Please enter velocity: "))
        break
    except ValueError :
        print("输入错误，请重新输入速度！")
kinetic_energy = 0.5*mass*velocity**2
print("The Kinetic Energy: ", kinetic_energy, "J")

#     包装函数
def get_number(prompt):
    while True:
        try :
            num = float(input(prompt))
            return num     #这里用break的话，函数最后一行要有return
        except ValueError:
            print("输入错误，请重新输入数字！")
mass = get_number("Please enter the mass: ")
velocity = get_number("Please enter the velocity: ")
energy = 0.5*mass*velocity**2
print("The Kinetic Energy: ", energy, "J")
