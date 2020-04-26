import numpy as np
import sympy as sympy
from src.MatrixManipulationSymbolic import MatrixSymbolic
import math

def main():
    """
    Example 6:

    Calculates the Three-link manipulator kinematics.
    At the end we can express a Transform from link 0 to link 3.
    """
    print('Example 7:')

    a1 = MatrixSymbolic()       # Rx(a_i-1)
    a2 = MatrixSymbolic()       # Dx(a_i-1)
    a3 = MatrixSymbolic()       # Dz(d_i)
    a4 = MatrixSymbolic()       # Rz(theta_i)

    print()
    print('t_0_1:')
    t_0_1 = (a1.rot_x('0')) * (a2.trans_x('0')) * (a3.trans_z('0')) * (a4.rot_z('theta_1'))
    print(sympy.pretty(t_0_1))

    print(sympy.pretty(a1.rot_x('x')))
    print(sympy.pretty(a4.rot_z('theta_2')))
    print()
    print('t_1_2:')
    t_1_2 = (a1.rot_x('x')) * (a2.trans_x('0')) * (a3.trans_z('0')) * (a4.rot_z('theta_2'))
    print(sympy.pretty(t_1_2))
    # print()
    # print('t_1_2 - 90:')
    # tt = a1.rot_x('x')
    # print(sympy.pretty(tt.subs(x, 90)))

    print()
    print('t_2_3:')
    t_2_3 = (a1.rot_x('0')) * (a2.trans_x('l2')) * (a3.trans_z('0')) * (a4.rot_z('theta_3'))
    print(sympy.pretty(t_2_3))

    print()
    print('t_3_4:')
    t_3_4 = (a1.rot_x('0')) * (a2.trans_x('l3')) * (a3.trans_z('0')) * (a4.rot_z('0'))
    print(sympy.pretty(t_3_4))

    # t_0_2 = t_0_1 * t_1_2
    # print()
    # print('t_0_2:')
    # print(sympy.pretty(t_0_2))
    #
    # print()
    # print('Simplified t_0_2:')
    # print(sympy.pretty(sympy.simplify(t_0_2)))
    #
    # t_2_4 = t_2_3 * t_3_4
    # print()
    # print('t_2_4:')
    # print(sympy.pretty(t_2_4))
    #
    # print()
    # print('Simplified t_0_4:')
    # print(sympy.pretty(sympy.simplify(t_2_4)))
    #
    # t_0_4 = t_0_2 * t_2_4
    # print()
    # print('t_0_4:')
    # print(sympy.pretty(sympy.simplify(t_0_4)))

    t_0_4 = t_0_1 * t_1_2 * t_2_3 * t_3_4

    print()
    print('t_0_4:')
    print(sympy.pretty(sympy.simplify(t_0_4)))

    # angle = 90
    # theta = np.deg2rad(angle)
    #
    # print()
    # print('t_12:')
    # t_12 = t_0_4.subs(x, np.deg2rad(90))
    # print(sympy.pretty(t_12))


    return


if __name__ == '__main__':
    main()


