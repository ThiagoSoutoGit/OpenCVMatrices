import sympy


def disp(expr, ans, dp=3.0):

    print("{} =\n\n {}\n".format(expr, sympy.pretty(ans.evalf(dp))))

    return


def main():

    sympy.init_printing(
        num_columns=240,
        use_unicode=False,
        pretty_printer=ascii
    )

    x = sympy.symbols('x')

    # Example 1
    print("Example 1\n")

    f = sympy.sin(x ** 2)
    disp("f", f)

    df_dx = sympy.diff(f, x)
    disp("df/dx", df_dx)

    # Example 2
    print("Example 2\n")

    f = (6 * x ** 2 + 7 * x) ** 4
    disp("f", f)

    df_dx = sympy.diff(f, x)
    disp("df/dx", df_dx)

    df_dx = sympy.expand(df_dx)
    disp("df/dx", df_dx)
    
    # Example 3
    print("Example 3\n")

    f = (4 * x ** 2 -3 * x + 2) ** -2
    disp("f", f)

    df_dx = sympy.diff(f, x)
    disp("df/dx", df_dx)

    df_dx = sympy.expand(df_dx)
    disp("df/dx", df_dx)

    df_dx = sympy.simplify(df_dx)
    disp("df/dx", df_dx)

    # Example 4
    print("Example 4\n")

    f = (1 - 8 * x) ** (1/3)

    print("f =\n {}\n".format(f))

    df_dx = sympy.diff(f, x)
    disp("df/dx", df_dx)

    return


if __name__ == "__main__":

    main()
