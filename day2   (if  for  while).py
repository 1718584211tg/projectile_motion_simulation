#     速度判断器
velocity = float(input("请输入速度(m/s):"))
if velocity < 5:
    print("物体处于低速运动")
elif velocity < 20:
    print("物体处于中速运动")
else:
    print("物体处于高速运动")
    
#     物理成绩判断器
physics_score = float(input("请输入物理成绩(0-100分):"))
if physics_score < 60:
    print("物理成绩不及格")
elif physics_score <= 79:
    print("物理成绩及格")
elif physics_score <= 89:
    print("物理成绩良好")
else:
    print("物理成绩优秀")
    
#     物体状态判断器
mass = float(input("请输入物体质量(kg):"))
velocity = float(input("请输入物体速度(m/s):"))
energy = 0.5 * mass * velocity ** 2
print("物体的动能为: ", energy, "J")
if energy < 100:
    print("物体处于低能量状态")
elif energy < 500:
    print("物体处于中能量状态")
else:
    print("物体处于高能量状态")

#     动能计算器
mass = 2
for i in range(1, 21):
    velocity = i
    energy = 0.5 * mass * velocity ** 2
    if energy < 50:
        print("物体速度为", velocity, "m/s时,动能为:", energy, "J,处于低能量状态")
    elif energy < 200:
        print("物体速度为", velocity, "m/s时,动能为:", energy, "J,处于中能量状态")
    else:
        print("物体速度为", velocity, "m/s时,动能为:", energy, "J,处于高能量状态")

#      自由落体瞬时计算器
g=9.8
height = 100
time = 0
s = 0
velocity = 0
while s < height:
    time += 0.1
    velocity = g * time
    s = 0.5 * g * time ** 2
    print("时间为", time, "s时, 下落距离:", s, "m, 瞬时速度:", velocity, "m/s")
print("经过", time, "s, 物体已经到达地面")
    