#     实验数据
velocities = [2, 4, 6, 8, 10]   # Lise = []
print(velocities)
print(velocities[0])  # 输出第一个元素
print(velocities[2])  # 输出第三个元素
velocities[1] = 5  # 修改第二个元素
print(velocities)   # .append(添加值); .remove(删除指定值)；.pop(删除指定位置)；.sort(排升序)
velocities.append(12)  # 添加新元素
print(velocities)
print(len(velocities))  # 输出列表长度

#     批量计算
mass = 3
velocities = [2, 4, 6, 8, 10]
for velocity in velocities:
    energy = 0.5*mass*velocity**2
    print("Velocity:", velocity, "m/s, Kinetic Energy:", energy, "J")

#     数据记录
velocities = []
while len(velocities) < 5:   # or:for i in range(5):
    velocity = float(input("Please enter velocity (m/s): "))
    velocities.append(velocity)
print("Recorded velocities:", velocities)

#     数据处理
velocities = [8, 3, 15, 2, 10, 6]   # unit: m/s
print("Original velocities:", velocities)
# Sort the velocities in ascending order
velocities.sort()
print("Sorted velocities:", velocities)
velocities.remove(15)
velocities.append(20)
print("Updated velocities:", velocities)
mass = 2
for velocity in velocities:
    energy = 0.5 * mass * velocity ** 2
    print("When the velocity is", velocity, "m/s, the kinetic energy is", energy, "J")

#   数据切片与索引
date = [10, 20, 30, 40, 50, 60]
print(date[1:4])
print(date[0:4])
print(date[3:6])
print(date[::-1])   # 倒序：date[：：-1] or date[-1::-1]
#     date[start:end:step]  start:起始索引，end:结束索引，step:步长
velocities = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(velocities[0:5])
print(velocities[5:10])
print(velocities[2:9:2])  # 步长为2
print(velocities[::-1])  # 倒序
print(velocities[-1:-9:-2])  # 倒序切片，步长为2