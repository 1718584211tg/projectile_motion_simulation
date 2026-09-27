#     文件读取
file = open("velocity.txt", "r")
data = file.read()
data = data.split()
velocities = []
for value in data:
    velocity = float(value)
    velocities.append(velocity)
print(velocities)
file.close()
mass = 2
for velocity in velocities:
    energy = 0.5*mass*velocity**2
    print("Velocity:", velocity, "m/s ; Kinetic Energy:", energy, "J")

#     with open() as file:
with open("velocity.txt", "r") as file:
    data = file.read()
    data = data.split()
velocities = []
mass = 2
for value in data:
    velocity = float(value)
    velocities.append(velocity)
for velocity in velocities:
    kinetic_energy = 0.5*mass*velocity**2
    print("Velocity:", velocity, "m/s; Kinetic Energy:", kinetic_energy, "J")

#     文件写入
with open("result.txt","w") as file:
    for velocity in velocities:
        energy = 0.5*mass*velocity**2
        file.write("Velocity: "+str(velocity)+" ; Kinetic Energy: "+str(energy)+"\n")
