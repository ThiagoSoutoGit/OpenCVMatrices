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

    f = sympy.cos(x)
    g = x

    fg = f / g
    disp("f / g", fg)

    dfg_dx = sympy.diff(fg, x)
    disp("d(f / g)/dx", dfg_dx)

    dfg_dx = sympy.simplify(dfg_dx)
    disp("d(f / g)/dx", dfg_dx)

    # Example 2
    print("Example 2")

    f = x ** 2 + 1
    g = x ** 3

    fg = f / g
    disp("f / g", fg)

    dfg_dx = sympy.diff(fg, x)
    disp("d(f / g)/dx", dfg_dx)

    dfg_dx = sympy.simplify(dfg_dx)
    disp("d(f / g)/dx", dfg_dx)

    # Example 3
    print("Example 3")

    f = 5 * x ** 5 - x ** 7
    g = 20 * x ** 2 - 3 * x ** -7

    fg = f / g
    disp("f / g", fg)

    dfg_dx = sympy.diff(fg, x)
    disp("d(f / g)/dx", dfg_dx)

    dfg_dx = sympy.expand(dfg_dx)
    disp("d(f / g)/dx", dfg_dx)

    dfg_dx = sympy.simplify(dfg_dx)
    disp("d(f / g)/dx", dfg_dx)

    return


if __name__ == "__main__":

    main()
