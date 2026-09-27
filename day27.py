#       斜抛模拟
import numpy as np

def compute_trajectory(t, v0, angle_deg, g):
    theta_rad = np.radians(angle_deg)
    x = v0 * np.cos(theta_rad) * t
    y = v0 * np.sin(theta_rad) * t - 0.5*g*t**2
    return x, y
def main():
    v0 = 20
    angle_deg = 45
    g = 9.8
    t = np.linspace(0, 3, 50)
    x, y = compute_trajectory(t, v0, angle_deg, g)
    print(x[:5])
    print(y[:5])
if __name__ == "__main__":
    main()
