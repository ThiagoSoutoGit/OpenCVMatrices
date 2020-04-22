import numpy as np
import sympy as sympy




def main():
    """
    This code will prints several Matrices like like Dot products, Rotational Matrix in a symbolic form.
    Refer to :ref: Example_6 for details on the matrices operations.
    """

    np.set_printoptions(precision=3,
                        suppress=True)

    sympy.init_printing(use_unicode=True,
                        num_columns=240)

    # Example 1

    print("Example 1\n")

    x = sympy.Symbol('x')
    y = sympy.Symbol('y')

    print("x*y=\n{}\n".format(sympy.pretty(x*y)))

    # Example 2

    print("Example 2\n")

    X = sympy.MatrixSymbol('X', 3, 3)
    Y = sympy.MatrixSymbol('Y', 3, 3)
    
    X = sympy.Matrix(X)
    Y = sympy.Matrix(Y)

    print("X*Y=\n{}\n".format(sympy.pretty(X*Y)))

    # Example 3

    print("Example 3\n")

    alpha_i_1 = sympy.Symbol('alpha_i-1', real=True)
    a_i_1 = sympy.Symbol('a_i-1', real=True)
    d_i = sympy.Symbol('d_i', real=True)
    theta_i = sympy.Symbol('theta_i', real=True)

    rot_x = sympy.Matrix([[1, 0, 0, 0],
                          [0, sympy.cos(alpha_i_1), -sympy.sin(alpha_i_1), 0],
                          [0, sympy.sin(alpha_i_1), sympy.cos(alpha_i_1), 0],
                          [0, 0, 0, 1]])

    print("Rot_X(alpha_i)=\n{}\n".format(sympy.pretty(rot_x)))

    trans_x = sympy.Matrix([[1, 0, 0, a_i_1],
                            [0, 1, 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]])

    print("Trans_X(d_i)=\n{}\n".format(sympy.pretty(trans_x)))

    rot_z = sympy.Matrix([[sympy.cos(theta_i), -sympy.sin(theta_i), 0, 0],
                          [sympy.sin(theta_i), sympy.cos(theta_i), 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1]])

    print("Rot_Z(theta_i)=\n{}\n".format(sympy.pretty(rot_z)))

    trans_z = sympy.Matrix([[1, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, 1, d_i],
                            [0, 0, 0, 1]])

    print("Trans_Z(d_i)=\n{}\n".format(sympy.pretty(trans_z)))

    T = rot_x * trans_x * rot_z * trans_z

    print("T=\n{}\n".format(sympy.pretty(T)))

    T01 = T.subs([(alpha_i_1, 0), (a_i_1, 0), (d_i, 0)])

    print("01_T=\n{}\n".format(sympy.pretty(T01)))

    angle = -90
    theta = np.deg2rad(angle)

    T12 = T.subs([(alpha_i_1, theta)])

    print("12_T=\n{}\n".format(sympy.pretty(T12)))

    T23 = T.subs([(alpha_i_1, 0), (d_i, 0)])

    print("23_T=\n{}\n".format(sympy.pretty(T23)))

    T34 = T.subs([(alpha_i_1, 0), (d_i, 0)])

    print("34_T=\n{}\n".format(sympy.pretty(T34)))

    return


if __name__ == "__main__":

    main()