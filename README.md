# Projectile-Motion-Simulation

本项目从一些基本的物理运动模拟开始，后面做了斜抛运动的模拟，计算轨迹及可视化，数据的保存。

## 所用到的主要物理公式如下：
 - x(t) = v0 * cos(theta) * t
 - y(t) = v0 * sin(theta) * t - 0.5 * g * t**2

## 关于如何运行

### 运行环境要求
Python 环境：
 - Python 3. x
运行用到的库(需提前安装)：
 - NumPy (可能会用到math)
 - Matplotlib

### 具体运行步骤
1. 先确保所需库已安装：
```
pip install numpy matplotlib
```
2. 找到主程序运行：
```
python day30.py
```
3. 运行后确认有两个文件生成：
 - `trajectory.png`(抛物运动曲线轨迹图)
 - `trajectory.csv`(轨迹数据)

