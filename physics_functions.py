def get_number(prompt):
    while True:
        try :
            num = float(input(prompt))
            return num
        except ValueError :
            print("输入错误。请重新输入数字！")

def calculate_kinetic_energy(mass,velocity):
    energy = 0.5*mass*velocity**2
    return energy
