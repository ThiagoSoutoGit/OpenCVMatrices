import sympy


def disp(expr, ans, dp=2.0):

    print("{} =\n\n {}\n".format(expr, sympy.pretty(ans.evalf(dp))))

    return


def main():

    sympy.init_printing(
        num_columns=240,
        use_unicode=True,
        pretty_printer=ascii
    )

    x, y, z = sympy.symbols('x, y, z')

    # Example 1
    print("Example 1\n")

    f = x ** 4 + y ** 3
    disp("f", f)

    df_dx = sympy.diff(f, x)
    disp("df/dx", df_dx)

    df_dy = sympy.diff(f, y)
    disp("df/dy", df_dy)

    # Example 2
    print("Example 2\n")

    f = 2 * x ** 5 + 3 * y ** 5 - 8 * x ** 2 * y ** 2 * z ** 2
    disp("f", f)

    df_dx = sympy.diff(f, x)
    disp("df/dx", df_dx)

    df_dy = sympy.diff(f, y)
    disp("df/dy", df_dy)

    df_dz = sympy.diff(f, z)
    disp("df/dz", df_dz)

    # Example 3
    print("Example 3\n")

    f = 6 * y ** 2 * x
    disp("f", f)

    df_dy = sympy.diff(f, y)
    disp("df/dy", df_dy)

    # Example 4
    print("Example 4\n")

    R, r, pi = sympy.symbols('R, r, pi')

    f = 4 * pi ** 2 * R * r
    disp("f", f)

    df_dR = sympy.diff(f, R)
    disp("df/dR", df_dR)

    return


if __name__ == "__main__":

    main()
