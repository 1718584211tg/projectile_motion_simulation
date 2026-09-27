#       程序结构
import numpy as np

def compute_theory_position(t, g):
    s = 0.5*g*t**2
    return s
def add_measurement_noise(s_theory, scale, seed):
    np.random.seed(seed)
    noise = np.random.normal(loc=0,scale=scale,size=len(s_theory))   # 用size更通用，len()只能表一维数组元素数量
    s_measured = s_theory + noise
    return s_measured
def main():
    g = 9.8
    times = np.linspace(0.1, 1.0, 10)
    s_theory = compute_theory_position(times,g)
    s_measured = add_measurement_noise(s_theory, 0.05, 1)
    print(s_theory)
    print(s_measured)
if __name__ == "__main__":
    main()
