import numpy as np
import sympy as sympy


def T_trans_x(a=0):

    """
    Defining a matrix T 4x4 identity with a = 0, where a is the :math:'a_1_4' element.

    np.float32: creates the array with 16 float32 elements

    np.reshape: np.reshape rearrange the array into a matrix with 4 lines and 4 columns

    Return: The matrix
    """

    T_trans_x = np.float32([1, 0, 0, a,
                            0, 1, 0, 0,
                            0, 0, 1, 0,
                            0, 0, 0, 1])
    T_trans_x = np.reshape(T_trans_x, (4, 4))

    return T_trans_x


def T_rot_x(alpha=0, degrees=True):
    """
    Definition: receives an alpha angle and returns

    Parameters: alpha=0, degrees=True

    Return: T_rot_x - The Rotational matrix at the X axis
    """

    if degrees == True:

        alpha = np.deg2rad(alpha)

    T_rot_x = np.float32([1, 0, 0, 0,
                            0, np.cos(alpha), -np.sin(alpha), 0,
                            0, np.sin(alpha), np.cos(alpha), 0,
                            0, 0, 0, 1])
    T_rot_x = np.reshape(T_rot_x, (4, 4))

    return T_rot_x


def T_trans_z(d=0):

    T_trans_z = np.float32([1, 0, 0, 0,
                            0, 1, 0, 0,
                            0, 0, 1, d,
                            0, 0, 0, 1])
    T_trans_z = np.reshape(T_trans_z, (4,4))

    return T_trans_z 


def T_rot_z(theta=0, degrees=True):

    if degrees == True:

        theta = np.deg2rad(theta)

    T_rot_z = np.float32([np.cos(theta), -np.sin(theta), 0, 0,
                            np.sin(theta), np.cos(theta), 0, 0,
                            0, 0, 1, 0,
                            0, 0, 0, 1])
    T_rot_z = np.reshape(T_rot_z, (4, 4))

    return T_rot_z


def T(alpha=0, a=0, d=0, theta=0, degrees=True):

    T = np.matmul(np.matmul(T_rot_x(alpha, degrees=degrees), T_trans_x(a)), np.matmul(T_rot_z(theta, degrees=degrees), T_trans_z(d)))

    return T

    
def main():

    T_01 = T(0, 0, 0, 0, True)

    print("T_01=\n{}".format(T_01))

    T_12 = T(0, 100, 0, 0, True)

    print("T_01=\n{}".format(T_12))

    T_23 = T(0, 100, 0, 0, True)

    print("T_23=\n{}".format(T_23))

    T_02 = np.matmul(T_01, T_12)
    T_03 = np.matmul(T_02, T_23)

    print("T_03=\n{}".format(T_03))

    # Rotation on the X axis

    angle_x = 60
    print()
    print("Matrix rotating in X:")
    print()
    print(T_rot_x(angle_x, True))

    # Rotation on the Z axis

    angle_z = 30
    print()
    print("Matrix rotating in Z:")
    print()
    print(T_rot_z(angle_z, True))

    return


if __name__ == "__main__":

    main()
