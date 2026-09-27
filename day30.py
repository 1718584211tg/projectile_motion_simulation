#       综合项目
import numpy as np
import matplotlib.pyplot as plt
def compute_trajectory(t, v0, angle_deg, g):
    theta_rad = np.radians(angle_deg)
    x = v0*np.cos(theta_rad)*t
    y = v0*np.sin(theta_rad)*t - 0.5*g*t**2
    return x, y
def compute_flight_time(v0, angle_deg, g):
    theta_rad = np.radians(angle_deg)
    t_flight = 2*v0*np.sin(theta_rad)/g
    return t_flight
def plot_trajectory(x, y):
    plt.plot(x,y,color="green",linewidth=1,label="Projectile Curve")
    xm = x[np.argmax(y)]
    ym = y[np.argmax(y)]
    plt.scatter(xm,ym,color="red",label="Apex")
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title("Projectile Motion")
    plt.grid(True)
    plt.legend()
    plt.axis('equal')
    plt.savefig(r"d:\用户\py\trajectory.png", dpi=150)
    plt.show()
def main():
    params = {
        "v0": 20,
        "angle_deg": 45,
        "g": 9.8
    }
    t_flight = compute_flight_time(params["v0"], params["angle_deg"], params["g"])
    t = np.linspace(0, t_flight, 50)
    x, y = compute_trajectory(t, params["v0"], params["angle_deg"], params["g"])
    plot_trajectory(x, y)
    data = np.column_stack((x, y))
    np.savetxt(r"d:\用户\py\trajectory.csv", data, delimiter=",", header="x,y", comments="")
if __name__ == "__main__":
    main()