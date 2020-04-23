import numpy as np
import sympy as sympy


def T_trans_x(a=0):
    """
    Definition: Translate the matrix a given amount `a` on the *X* axis by Defining a matrix T 4x4 identity
    matrix with *a* (1,4) element position.

    np.float32: creates the array with 16 float32 elements

    np.reshape: np.reshape rearrange the array into a matrix with 4 lines and 4 columns

    :type a: float
    :param a: Distance translated on the X-axis

    Returns: The Translation Matrix on the *X* axis by a distance *a*
    """
    T_trans_x = np.float32([1, 0, 0, a,
                            0, 1, 0, 0,
                            0, 0, 1, 0,
                            0, 0, 0, 1])
    T_trans_x = np.reshape(T_trans_x, (4, 4))

    return T_trans_x


def T_rot_x(alpha=0, degrees=True):
    """
    Definition: Receives an alpha angle and returns the rotation matrix for the given angle at the *X* axis.
    If the angle is given in radian degrees should be False.

    :type alpha: float
    :param alpha: Rotation Angle around the X axis
    :type degrees: bool
    :param degrees: Indicates if the provided angle is in degrees, if yes It will be converted to radians

    Returns: The Rotational Matrix at the X axis by an *alpha* angle
    """
    if degrees is True:
        alpha = np.deg2rad(alpha)

    T_rot_x = np.float32([1, 0, 0, 0,
                          0, np.cos(alpha), -np.sin(alpha), 0,
                          0, np.sin(alpha), np.cos(alpha), 0,
                          0, 0, 0, 1])
    T_rot_x = np.reshape(T_rot_x, (4, 4))

    return T_rot_x


def T_trans_z(d=0):
    """
    Definition: Translate the matrix a given amount `d` on the *Z* axis. by Defining a matrix T 4x4 identity
    matrix with *d* (3,4) element position.

    :type d: float
    :param d: Distance translated on the Z-axis

    Returns: The Translation Matrix on the *Z* axis by a distance *d*
    """
    T_trans_z = np.float32([1, 0, 0, 0,
                            0, 1, 0, 0,
                            0, 0, 1, d,
                            0, 0, 0, 1])
    T_trans_z = np.reshape(T_trans_z, (4, 4))

    return T_trans_z


def T_rot_z(theta=0, degrees=True):
    """
    Definition: Receives an theta angle and returns the rotation matrix for the given angle at the *Z* axis.
    If the angle is given in radian degrees should be False.

    :type theta: float
    :param theta: Rotation Angle around the Z axis
    :type degrees: bool
    :param degrees: Indicates if the provided angle is in degrees, if yes It will be converted to radians

    Returns: The Rotational Matrix at the Z axis by an *theta* angle
    """
    if degrees is True:
        theta = np.deg2rad(theta)

    T_rot_z = np.float32([np.cos(theta), -np.sin(theta), 0, 0,
                          np.sin(theta), np.cos(theta), 0, 0,
                          0, 0, 1, 0,
                          0, 0, 0, 1])
    T_rot_z = np.reshape(T_rot_z, (4, 4))

    return T_rot_z


def T(alpha=0, a=0, d=0, theta=0, degrees=True):
    """
    Definition: Receives four arguments, *alpha* and *a*, being angle for rotation in the X axis and translation on
    the X axis. Also *d* and *theta*, being translation on the Z axis and Rotation on the Z axis. And returns the
    Multiplication of (Rotation matrix in X and the Translation in X) multiplied by (Rotation matrix in Z and the
    Translation in Z) . It utilizes the np.matmul for matrix multiplication.

    :type alpha: float
    :param alpha: Rotation Angle around the X axis
    :type degrees: bool
    :type a: float
    :param a: Distance translated on the X-axis
    :type d: float
    :param d: Distance translated on the Z-axis
    :type theta: float
    :param theta: Rotation Angle around the Z axis
    :type degrees: bool
    :param degrees: Indicates if the provided angle is in degrees, if yes It will be converted to radians

    Returns: A matrix with the Rotations and translations set.
    """
    T = np.matmul(np.matmul(T_rot_x(alpha, degrees=degrees), T_trans_x(a)),
                  np.matmul(T_rot_z(theta, degrees=degrees), T_trans_z(d)))

    return T


def main():
    """
    Definition: Complete a series of operations using the functions defined including:
        Defines a matrix with no rotation and no translation (Identity)
        Translation of a given distance on the X axis
        Second Translation of a given distance on the X axis
        Identity matrix multiplied by the first X translation multiplied by the second translation
        Rotation Matrix in X by a given angle
        Rotation Matrix in Z by a given angle
        Printe them all
    """
    T_01 = T(0, 0, 0, 0, True)

    print("Matrix with no rotation and no translation (Identity):\n{}\n".format(T_01))

    trans_x = 100
    T_12 = T(0, trans_x, 0, 0, True)

    print("Translation of {} on the X axis:\n{}\n".format(trans_x, T_12))

    trans_x_2 = 100
    T_23 = T(0, trans_x_2, 0, 0, True)

    print("Second Translation of {} on the X axis:\n{}\n".format(trans_x_2, T_23))

    T_02 = np.matmul(T_01, T_12)
    T_03 = np.matmul(T_02, T_23)

    print("Identity matrix multiplied by the first X translation multiplied by the second translation:\n{}".format(
        T_03))

    # Rotation on the X axis

    angle_x = 60
    print("\nRotation Matrix in X by {} degrees:".format(angle_x))
    print(T_rot_x(angle_x, True))

    # Rotation on the Z axis

    angle_z = 45
    print("\nRotation Matrix in Z by {} degrees:".format(angle_z))
    print(T_rot_z(angle_z, True))

    return


if __name__ == '__main__':
    main()
