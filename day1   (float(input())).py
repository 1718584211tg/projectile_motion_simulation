#day1. 第一题
mass=float(input("请输入质量(kg):"))
high=float(input("请输入物体的高度(m):"))
g=9.8
Ep=mass*g*high
print("物体的重力势能为：",Ep,"J")

#      第二题
velocity=float(input("请输入自由落体初速度(m/s):"))
time=float(input("请输入自由落体运动时间(s):"))
g=9.8
end_veloc=velocity+g*time
print("物体自由落体末速度为：",end_veloc,"m/s")

#      第三题
mass=float(input("请输入质量(kg):"))
velocity=float(input("请输入物体速度(m/s):"))
P=mass*velocity
print("物体的动量为：",P,"kg*m/s")

#      第四题
mass=float(input("请输入质量(kg):"))
velocity=float(input("请输入速度(m/s):"))
high=float(input("请输入高度(m):"))
g=9.8
Ek=0.5*mass*velocity**2
Ep=mass*g*high
P=mass*velocity
print("物体的动能为：",Ek,"J")
print("物体的重力势能为：",Ep,"J")
print("物体的动量为：",P,"kg*m/s")

#      第五题
high=float(input("请输入物体开始下落高度(m):"))
g=9.8
time=(2*high/g)**0.5
velocity=(2*g*high)**0.5
print("物体下落时间为：",time,"s")
print("物体落地速度为：",velocity,"m/s")