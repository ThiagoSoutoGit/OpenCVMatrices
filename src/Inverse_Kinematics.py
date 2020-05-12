import numpy as np
import sympy

np.set_printoptions(precision=3,
                    suppress=True)
sympy.init_printing(num_columns=240)

l2 = 500.0
l3 = 500.0
l4 = 230.0

theta_2 = np.deg2rad(0.0)
theta_3 = np.deg2rad(45.0)
theta_4 = np.deg2rad(45.0)

# joint 1

x05 = 500 + 500 * np.cos(theta_2)
y05 = 0.0
z05 = 500 + 500 * np.sin(theta_3)

t1 = np.arctan2(y05, x05)

print("theta_2 = {}".format(t1))

# joint 2

x14 = 500 + 500 * np.cos(theta_3)
y14 = 500 * np.sin(theta_3)
z14 = 0.0

B = np.arctan2(y14, x14)
c2 = (l3**2 - l2**2 - x14**2 - y14**2)/(-2*l2*np.sqrt(x14**2+y14**2))
s2 = np.sqrt(1 - c2**2)
w = np.arctan2(s2, c2)
t2 = B - w

print("theta_3 = {:.3f}".format(np.rad2deg(t2)))

t2 = np.arctan2(y14, x14) + np.arccos((l3**2 - l2**2 - x14**2 - y14**2) / (-2*l2*np.sqrt(x14**2 + y14**2)))

print("theta_4 = {:.3f}".format(np.rad2deg(t2)))
