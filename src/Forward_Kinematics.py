import numpy as np
import sympy as sympy
from sympy import *


class ForwardKinematics:

    """
    Definition: This class generates Homogeneous transform matrices, although it uses a symbolic approach
    that can be used to multiply any matrix and obtain the translation or rotation.

    sympy.cos and sympy.sin: cos and sin for sympy

    sympy.simplify: SymPy has dozens of functions to perform various kinds of simplification.
    simplify() attempts to apply all of these functions
    in an intelligent way to arrive at the simplest form of an expression.

    Returns: It returns Rotation and translation matrices.

    Obs: **kwargs (keyword arguments) are used to facilitate the identification of the parameters, so initiate the
    object
    """
    np.set_printoptions(precision=3, suppress=True)

    sympy.init_printing(use_unicode=True, num_columns=400)

    def __init__(self, **kwargs):
        """
        Initializes the Object.
        """
        self._x_angle = kwargs['x_angle'] if 'x_angle' in kwargs else 'alpha_i-1'
        self._x_dist = kwargs['x_dist'] if 'x_dist' in kwargs else 'a_i-1'
        self._y_angle = kwargs['y_angle'] if 'y_angle' in kwargs else '0'
        self._y_dist = kwargs['y_dist'] if 'y_dist' in kwargs else '0'
        self._z_angle = kwargs['z_angle'] if 'z_angle' in kwargs else 'theta_i'
        self._z_dist = kwargs['z_dist'] if 'z_dist' in kwargs else 'd_i'

    def trans_x(self, a):
        """
        Definition: Translates the matrix a given amount `a` on the *X* axis by Defining a 4x4 identity
        matrix with `a` as the (1,4) element.

        :type a: string
        :param a: Distance translated on the X-axis

        Returns: The Translation Matrix on the *X* axis by a given distance
        """
        self._x_dist = a

        t_x = sympy.Matrix([[1, 0, 0, self._x_dist],
                            [0, 1, 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]])

        t_x = t_x.evalf()

        return t_x

    def trans_z(self, d):
        """
        Definition: Translate the matrix a given amount `d` on the *Z* axis. by Defining a matrix T 4x4 identity
        matrix with *d* (3,4) element position.

        :type d: string
        :param d: Distance translated on the Z-axis

        Returns: The Translation Matrix on the *Z* axis by a given distance
        """
        self._z_dist = d

        t_z = sympy.Matrix([[1, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, 1, self._z_dist],
                            [0, 0, 0, 1]])

        t_z = t_z.evalf()

        return t_z

    def rot_x(self, alpha):
        """
        Definition: Receives an alpha angle and returns the rotation matrix for the given angle at the *X* axis.

        :type alpha: string
        :param alpha: Rotation Angle around the X axis

        Returns: The Rotational Matrix at the X axis by an *given* angle
        """
        self._x_angle = alpha

        r_x = sympy.Matrix([[1, 0, 0, 0],
                            [0, sympy.cos(self._x_angle), -sympy.sin(self._x_angle), 0],
                            [0, sympy.sin(self._x_angle), sympy.cos(self._x_angle), 0],
                            [0, 0, 0, 1]])

        r_x = r_x.evalf()

        return r_x

    def rot_z(self, theta):
        """
        Definition: Receives an theta angle and returns the rotation matrix for the given angle at the *Z* axis.

        :type theta: string
        :param theta: Rotation Angle around the Z axis

        Returns: The Rotational Matrix at the Z axis by an *given* angle
        """
        self._z_angle = theta

        r_z = sympy.Matrix([[sympy.cos(self._z_angle), -sympy.sin(self._z_angle), 0, 0],
                            [sympy.sin(self._z_angle), sympy.cos(self._z_angle), 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]])

        r_z = r_z.evalf()

        return r_z


# def printM(expr, num_digits):
#     return expr.xreplace({n.evalf(): n if type(n) == int else Float(n, num_digits) for n in expr.atoms(Number)})

def printM(expr, num_digits):
    return expr.xreplace({n.evalf(): round(n, num_digits) for n in expr.atoms(Number)})


def main():
    """
    Assessment 02 Robotic manipulator design - Forward Kinematics.
    """
    a1 = ForwardKinematics()       # Rx(a_i-1)
    a2 = ForwardKinematics()       # Dx(a_i-1)
    a3 = ForwardKinematics()       # Dz(d_i)
    a4 = ForwardKinematics()       # Rz(theta_i)

    print('Matrix t_0_1:')
    t_0_1 = (a1.rot_x('0')) * (a2.trans_x('0')) * (a3.trans_z('l1')) * (a4.rot_z('theta_1'))
    print(sympy.pretty(t_0_1))

    print('\nMatrix t_1_2:')
    t_1_2 = (a1.rot_x('alpha_1')) * (a2.trans_x('0')) * (a3.trans_z('0')) * (a4.rot_z('theta_2'))
    t_1_2_subs = t_1_2.subs('alpha_1', np.deg2rad(90.00))
    print(sympy.pretty(printM(t_1_2_subs, 3)))

    print('\nMatrix t_2_3:')
    t_2_3 = (a1.rot_x('0')) * (a2.trans_x('l2')) * (a3.trans_z('0')) * (a4.rot_z('theta_3'))
    print(sympy.pretty(t_2_3))

    print('\nMatrix t_3_4:')
    t_3_4 = (a1.rot_x('0')) * (a2.trans_x('l3')) * (a3.trans_z('0')) * (a4.rot_z('theta_4'))
    print(sympy.pretty(t_3_4))

    print('\nMatrix t_4_5:')
    t_4_5 = (a1.rot_x('0')) * (a2.trans_x('l4')) * (a3.trans_z('0')) * (a4.rot_z('0'))
    print(sympy.pretty(t_4_5))

    t_0_5 = sympy.simplify(t_0_1 * t_1_2 * t_2_3 * t_3_4 * t_4_5)
    print('\nMatrix T_0_5: with substitutions Round')
    print(sympy.pretty(sympy.simplify(printM(t_0_5.subs('alpha_1', np.deg2rad(90.00)), 3))))
    t_0_5_subs = t_0_5.subs([('alpha_1', np.deg2rad(90.00)), ('l1', 230), ('l2', 500), ('l3', 500), ('l4', 180)])
    print('\nMatrix T_0_5: with substitutions Round')
    print(sympy.pretty(sympy.simplify(printM(t_0_5_subs, 3))))

    t_1_5 = sympy.simplify(t_1_2 * t_2_3 * t_3_4 * t_4_5)
    print('\nMatrix T_1_5:')
    print(sympy.pretty(printM(t_1_5.subs('alpha_1', np.deg2rad(90.00)), 3)))

    print('\nMatrix T_1_5: for theta_1 = 0 ')
    print(sympy.pretty(printM(t_1_5.subs([('alpha_1', np.deg2rad(90.00)), ('theta_1', np.deg2rad(0.00))]), 3)))

    print('\nMatrix T_1_5: for theta_1 = 0 ')
    print(sympy.pretty(printM(t_1_5.subs([('alpha_1', np.deg2rad(90.00)), ('theta_1', np.deg2rad(180.00))]), 3)))

    # t_1_5_subs = t_1_5.subs([('alpha_1', np.deg2rad(90.00)), ('l1', 230), ('l2', 500), ('l3', 500), ('l4', 180)])
    # print('\nMatrix T_1_5: with substitutions Round')
    # print(sympy.pretty(printM(t_1_5_subs, 3)))

    # Calculations for the Inverse kinematics problem

    t_1_4 = sympy.simplify(t_1_5 * t_4_5.inv())
    print('\nMatrix T_1_4:')
    print(sympy.pretty(printM(t_1_4.subs('alpha_1', np.deg2rad(90.00)), 3)))

    t_3_5 = sympy.simplify(t_1_5 * t_1_2.inv() * t_2_3.inv())
    print('\nMatrix t_3_5:')
    print(sympy.pretty(printM(t_3_5.subs('alpha_1', np.deg2rad(90.00)), 3)))





if __name__ == '__main__':
    main()
