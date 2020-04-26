import numpy as np
import sympy as sympy


class MatrixSymbolicHybrid:
    """
    Definition: This class generates Homogeneous transform matrices, although it uses a symbolic approach
    that can be used to multiply any matrix and obtain the translation or rotation.

    It uses `sympy` to generate the matrices:

    sympy.Matrix: creates a sympy matrix object.

    sympy.Symbol: creates a symbol, Symbols are identified by name and assumptions.
    First, you need to create symbols using Symbol("x")
    We are assuming here that the symbols are "Real" number.
    All newly created symbols have assumptions set according to `args`, for example:

        >>> a = symbols('a', integer=True)
        >>> a.is_integer
        True
        >>> x, y, z = symbols('x,y,z', real=True)
        >>> x.is_real and y.is_real and z.is_real
        True

    sympy.cos and sympy.sin: cos and sin for sympy

    sympy.simplify: SymPy has dozens of functions to perform various kinds of simplification.
    simplify() attempts to apply all of these functions
    in an intelligent way to arrive at the simplest form of an expression.

    Returns: It returns Rotation and translation matrices.

    Obs: **kwargs (keyword arguments) are used to facilitate the identification of the parameters, so initiate the
    object
    """
    np.set_printoptions(precision=3, suppress=True)

    sympy.init_printing(use_unicode=True, num_columns=250)

    def __init__(self, **kwargs):
        """
        Initializes the Object.
        """
        self._x_angle = kwargs['x_angle'] if 'x_angle' in kwargs else 'gamma_i-1'
        self._x_dist = kwargs['x_dist'] if 'x_dist' in kwargs else 'a_i-1'
        self._y_angle = kwargs['y_angle'] if 'y_angle' in kwargs else '0'
        self._y_dist = kwargs['y_dist'] if 'y_dist' in kwargs else '0'
        self._z_angle = kwargs['z_angle'] if 'z_angle' in kwargs else '0'
        self._z_dist = kwargs['z_dist'] if 'z_dist' in kwargs else '0'

    def trans_x(self, a='a_i-1'):
        """
        Definition: Translates the matrix a given amount `a` on the *X* axis by Defining a 4x4 identity
        matrix with `a` as the (1,4) element.

        :type a: string
        :param a: Distance translated on the X-axis

        Returns: The Translation Matrix on the *X* axis by a given distance
        """
        if type(a) is not str:
            self._x_dist = sympy.sympify(a)
        else:
            self._x_dist = sympy.Symbol(a, real=True)

        trans_x = sympy.Matrix([[1, 0, 0, self._x_dist],
                                [0, 1, 0, 0],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1]])

        return trans_x

    def trans_y(self, b='b_i-1'):
        """
        Definition: Translate the matrix a given amount `d` on the *Z* axis. by Defining a matrix T 4x4 identity
        matrix with *b* (3,4) element position.

        :type b: string
        :param b: Distance translated on the Z-axis

        Returns: The Translation Matrix on the *Z* axis by a given distance
        """
        if type(b) is not str:
            self._y_dist = sympy.sympify(b)
        else:
            self._y_dist = sympy.Symbol(b, real=True)

        trans_y = sympy.Matrix([[1, 0, 0, 0],
                                [0, 1, 0, self._y_dist],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1]])

        return trans_y

    def trans_z(self, d='d_i-1'):
        """
        Definition: Translate the matrix a given amount `d` on the *Z* axis. by Defining a matrix T 4x4 identity
        matrix with *c* (3,4) element position.

        :type d: string
        :param d: Distance translated on the Z-axis

        Returns: The Translation Matrix on the *Z* axis by a given distance
        """
        if type(d) is not str:
            self._z_dist = sympy.sympify(d)
        else:
            self._z_dist = sympy.Symbol(d, real=True)

        trans_z = sympy.Matrix([[1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 1, self._z_dist],
                                [0, 0, 0, 1]])

        return trans_z

    def rot_x(self, gamma='gamma_i-1'):
        """
        Definition: Receives an alpha angle and returns the rotation matrix for the given angle at the *X* axis.
        If the angle is given in radian degrees should be False.

        :type gamma: string
        :param gamma: Rotation Angle around the X axis

        Returns: The Rotational Matrix at the X axis by an *given* angle
        """
        if type(gamma) is not str:
            self._x_angle = sympy.sympify(gamma)
        else:
            self._x_angle = sympy.Symbol(gamma, real=True)

        rot_x = sympy.Matrix([[1, 0, 0, 0],
                              [0, sympy.cos(self._x_angle), -sympy.sin(self._x_angle), 0],
                              [0, sympy.sin(self._x_angle), sympy.cos(self._x_angle), 0],
                              [0, 0, 0, 1]])

        return rot_x

    def rot_y(self, beta='beta_i-1'):
        """
        Definition: Receives an theta angle and returns the rotation matrix for the given angle at the *Z* axis.
        If the angle is given in radian degrees should be False.

        :type beta: string
        :param beta: Rotation Angle around the Y axis

        Returns: The Rotational Matrix at the Y axis by an *given* angle
        """
        if type(beta) is not str:
            self._y_angle = sympy.sympify(beta)
        else:
            self._y_angle = sympy.Symbol(beta, real=True)

        rot_y = sympy.Matrix([[sympy.cos(self._y_angle), 0, 0, sympy.sin(self._y_angle)],
                              [0, 0, 0, 0],
                              [-sympy.sin(self._y_angle), 0, 1, sympy.cos(self._y_angle)],
                              [0, 0, 0, 1]])

        return rot_y

    def rot_z(self, alpha='alpha_i-1'):
        """
        Definition: Receives an theta angle and returns the rotation matrix for the given angle at the *Z* axis.
        If the angle is given in radian degrees should be False.

        :type alpha: string
        :param alpha: Rotation Angle around the Z axis

        Returns: The Rotational Matrix at the Z axis by an *given* angle
        """
        if type(alpha) is not str:
            self._z_angle = sympy.sympify(alpha)
        else:
            self._z_angle = sympy.Symbol(alpha, real=True)

        rot_z = sympy.Matrix([[sympy.cos(self._z_angle), -sympy.sin(self._z_angle), 0, 0],
                              [sympy.sin(self._z_angle), sympy.cos(self._z_angle), 0, 0],
                              [0, 0, 1, 0],
                              [0, 0, 0, 1]])

        return rot_z


def main():
    """
    Example 6:

    Calculates the Three-link manipulator kinematics.
    At the end we can express a Transform from link 0 to link 3.
    """
    print('Example 6:')

    a1 = MatrixSymbolicHybrid()       # Rx(a_i-1)
    a2 = MatrixSymbolicHybrid()       # Dx(a_i-1)
    a3 = MatrixSymbolicHybrid()       # Dz(d_i)
    a4 = MatrixSymbolicHybrid()       # Rz(theta_i)

    print()
    print('Rx(0):')
    print(sympy.pretty(a1.rot_x(0)))
    print()

    print()
    print('Dx(a_i-1):')
    print(sympy.pretty(a2.trans_x('a_i-1')))
    print()

    print()
    print('Rz(theta_i):')
    print(sympy.pretty(a3.rot_z('theta_i')))
    print()

    print()
    print('Dz(d_i):')
    print(sympy.pretty(a4.trans_z('d_i')))
    print()

    print()
    print('t_0_1:')
    t_0_1 = (a1.rot_x(0)) * (a2.trans_x(0)) * (a3.trans_z(0)) * (a4.rot_z('theta_1'))
    print(sympy.pretty(t_0_1))

    print()
    print('t_1_2:')
    t_1_2 = (a1.rot_x(0)) * (a2.trans_x('l1')) * (a3.trans_z(0)) * (a4.rot_z('theta_2'))
    print(sympy.pretty(t_1_2))

    print()
    print('t_2_3:')
    t_2_3 = (a1.rot_x(0)) * (a2.trans_x('l2')) * (a3.trans_z(0)) * (a4.rot_z('theta_3'))
    print(sympy.pretty(t_2_3))

    t_0_2 = t_0_1 * t_1_2
    print()
    print('t_0_2:')
    print(sympy.pretty(t_0_2))

    print()
    print('Simplified t_0_2:')
    print(sympy.pretty(sympy.simplify(t_0_2)))

    t_0_3 = t_0_2 * t_2_3
    print()
    print('t_0_3:')
    print(sympy.pretty(sympy.simplify(t_0_3)))

    return


if __name__ == '__main__':
    main()
