#   文件读写
file = open("velocity.txt", "r")
data = file.read()
print(data)
file.close()

file = open("velocity.txt", "r")
data = file.read()
data = data.split()
print(data)
velocities = []
for value in data:
    velocity = float(value)
    velocities.append(velocity)
print(velocities)
file.close()