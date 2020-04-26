import numpy as np


def main():
    """
    Example 4
    """
    np.set_printoptions(precision=3, suppress=True)

    print('Example 4:')
    print()

    print('Matrix A:')
    ma = np.float32([0.866, -0.5, 0,
                     0.5, 0.866, 0,
                     0, 0, 1])
    ma = np.reshape(ma, (3, 3))

    print(ma)

    print()
    print('Matrix I:')
    mi = np.float32([1, 0, 0,
                     0, 1, 0,
                     0, 0, 1])
    mi = np.reshape(mi, (3, 3))
    print(mi)

    print()
    print('Matrix I - A:')
    print(mi - ma)

    print()
    print('Matrix I + A:')
    print(mi + ma)

    print()
    print('Matrix (I + A)^-1:')
    print(np.linalg.inv(mi + ma))

    print()
    print('Matrix Q = (I-A)((I + A)^-1):')
    print(np.matmul((mi - ma), (np.linalg.inv(mi + ma))))

    return


if __name__ == '__main__':
    main()
