#new.1斜抛运动计算器
import math   #    调用math模块
velocity = float(input("请输入物体斜抛速度(m/s): "))
angle = float(input("请输入物体斜抛角度(°): "))
angle_rad = math.radians(angle)   #弧度制转换
g=9.8
velocity_x = velocity * math.cos(angle_rad)
velocity_y = velocity * math.sin(angle_rad)
time=(velocity_y) / g
high=(velocity_y ** 2) / (2 * g)
T=(2 * velocity_y) / g
print("物体斜抛的水平速度为: ", velocity_x, "m/s")
print("物体斜抛的竖直速度为: ", velocity_y, "m/s")
print("物体斜抛到达最高点所需时间为: ", time, "s")
print("物体斜抛的最大高度为: ", high, "m")
print("物体斜抛的飞行时间为: ", T, "s")

#new.2受力运动分析
mass=float(input("请输入物体质量(kg): "))
force=float(input("请输入物体所受合力(N): "))
s=float(input("请输入物体位移(m): "))
E_k0=0.5*mass*0
W=force*s
E_k=E_k0+W
final_velocity=(2*E_k/mass)**0.5
print("物体所受的功为: ", W, "J")
print("物体的最终动能为: ", E_k, "J")
print("物体的最终速度为: ", final_velocity, "m/s")