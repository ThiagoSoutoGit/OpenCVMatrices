import sympy


def disp(expr, ans, dp=3.0):

    print("{} =\n\n{}\n".format(expr, sympy.pretty(ans.evalf(dp))))

    return


def main():

    sympy.init_printing(
        num_columns=240,
        use_unicode=True,
        pretty_printer=ascii
    )

    # Example 1
    print("Example 1\n")

    l1, l2, theta1, theta2 = sympy.symbols('l_1, l_2, theta_1, theta_2')

    T_01 = sympy.Matrix([[sympy.cos(theta1), -sympy.sin(theta1), 0, 0],
                         [sympy.sin(theta1), sympy.cos(theta1), 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])
    disp("T_01", T_01)

    T_12 = sympy.Matrix([[sympy.cos(theta2), -sympy.sin(theta2), 0, l1],
                         [sympy.sin(theta2), sympy.cos(theta2), 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])
    disp("T_12", T_12)

    T_23 = sympy.Matrix([[1, 0, 0, l2],
                         [0, 1, 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])
    disp("T_23", T_23)

    T_02 = T_01 * T_12
    disp("T_02", T_02)

    T_03 = T_02 * T_23
    disp("T_03", T_03)

    disp("T_03", sympy.simplify(T_03))

    return


if __name__ == "__main__":

    main()
