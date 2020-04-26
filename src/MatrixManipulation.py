import numpy as np


class Matrix:
    """
    Definition: This class generates Homogeneous transform matrices,
    that can be used to multiply any matrix and obtain the translation or rotation.

    It uses `numpy` to generate the matrices:

        np.float32: creates the array with 16 float32 elements

        np.reshape: np.reshape rearrange the array into a 4X4 matrix

    Returns: It returns Rotation and translation matrices.

    Obs: **kwargs (keyword arguments) are used to facilitate the identification of the parameters, so initiate the
    object
    like: Matrix(x_angle='45', x_dist='100', z_angle='60', z_dist='100'), if an argument is not provided,
    the default 0 will be put to the argument.
    """
    np.set_printoptions(precision=3, suppress=True)

    def __init__(self, **kwargs):
        """
        Initializes the Object.
        """
        self._x_angle = kwargs['x_angle'] if 'x_angle' in kwargs else '0'
        self._x_dist = kwargs['x_dist'] if 'x_dist' in kwargs else '0'
        self._y_angle = kwargs['y_angle'] if 'y_angle' in kwargs else '0'
        self._y_dist = kwargs['y_dist'] if 'y_dist' in kwargs else '0'
        self._z_angle = kwargs['z_angle'] if 'z_angle' in kwargs else '0'
        self._z_dist = kwargs['z_dist'] if 'z_dist' in kwargs else '0'
        self._m_degrees = kwargs['m_degrees'] if 'm_degrees' in kwargs else 'True'

    def trans_x(self, a=0):
        """
        Definition: Translates the matrix a given amount `a` on the *X* axis by Defining a 4x4 identity
        matrix with `a` as the (1,4) element.

        :type a: float
        :param a: Distance translated on the X-axis

        Returns: The Translation Matrix on the *X* axis by a distance *a*
        """
        if a:
            self._x_dist = a
        trans_x = np.float32([1, 0, 0, self._x_dist,
                              0, 1, 0, 0,
                              0, 0, 1, 0,
                              0, 0, 0, 1])
        trans_x = np.reshape(trans_x, (4, 4))

        return trans_x

    def trans_y(self, b=0):
        """
        Definition: Translate the matrix a given amount `d` on the *Z* axis. by Defining a matrix T 4x4 identity
        matrix with *b* (3,4) element position.

        :type b: float
        :param b: Distance translated on the Z-axis

        Returns: The Translation Matrix on the *Z* axis by a distance *b*
        """
        if b:
            self._y_dist = b
        trans_y = np.float32([1, 0, 0, 0,
                              0, 1, 0, self._y_dist,
                              0, 0, 1, 0,
                              0, 0, 0, 1])
        trans_y = np.reshape(trans_y, (4, 4))

        return trans_y

    def trans_z(self, d=0):
        """
        Definition: Translate the matrix a given amount `d` on the *Z* axis. by Defining a matrix T 4x4 identity
        matrix with *c* (3,4) element position.

        :type d: float
        :param d: Distance translated on the Z-axis

        Returns: The Translation Matrix on the *Z* axis by a distance *c*
        """
        if d:
            self._z_dist = d
        trans_z = np.float32([1, 0, 0, 0,
                              0, 1, 0, 0,
                              0, 0, 1, self._z_dist,
                              0, 0, 0, 1])
        trans_z = np.reshape(trans_z, (4, 4))

        return trans_z

    def rot_x(self, gamma=0, degrees=True):
        """
        Definition: Receives an alpha angle and returns the rotation matrix for the given angle at the *X* axis.
        If the angle is given in radian degrees should be False.

        :type gamma: float
        :param gamma: Rotation Angle around the X axis
        :type degrees: bool
        :param degrees: Indicates if the provided angle is in degrees, if yes It will be converted to radians

        Returns: The Rotational Matrix at the X axis by an *gamma* angle
        """
        if gamma:
            self._x_angle = gamma
        if degrees:
            self._m_degrees = degrees

            self._x_angle = np.deg2rad(gamma)

        rot_x = np.float32([1, 0, 0, 0, 0,
                            np.cos(self._x_angle),
                            -np.sin(self._x_angle), 0, 0,
                            np.sin(self._x_angle),
                            np.cos(self._x_angle), 0,
                            0, 0, 0, 1])

        rot_x = np.reshape(rot_x, (4, 4))

        return rot_x

    def rot_y(self, beta=0, degrees=True):
        """
        Definition: Receives an theta angle and returns the rotation matrix for the given angle at the *Z* axis.
        If the angle is given in radian degrees should be False.

        :type beta: float
        :param beta: Rotation Angle around the Z axis
        :type degrees: bool
        :param degrees: Indicates if the provided angle is in degrees, if yes It will be converted to radians

        Returns: The Rotational Matrix at the Z axis by an *beta* angle
        """
        if beta:
            self._y_angle = beta
        if degrees:
            self._m_degrees = degrees

            self._y_angle = np.deg2rad(beta)

        rot_y = np.float32([np.cos(self._y_angle), 0, 0,
                            np.sin(self._y_angle),
                            0, 0, 0, 0,
                            -np.sin(self._y_angle), 0, 1,
                            np.cos(self._y_angle),
                            0, 0, 0, 1])

        rot_y = np.reshape(rot_y, (4, 4))

        return rot_y

    def rot_z(self, alpha=0, degrees=True):
        """
        Definition: Receives an theta angle and returns the rotation matrix for the given angle at the *Z* axis.
        If the angle is given in radian degrees should be False.

        :type alpha: float
        :param alpha: Rotation Angle around the Z axis
        :type degrees: bool
        :param degrees: Indicates if the provided angle is in degrees, if yes It will be converted to radians

        Returns: The Rotational Matrix at the Z axis by an *alpha* angle
        """
        if alpha:
            self._z_angle = alpha
        if degrees:
            self._m_degrees = degrees

            self._z_angle = np.deg2rad(alpha)

        rot_z = np.float32([np.cos(self._z_angle),
                            -np.sin(self._z_angle), 0, 0,
                            np.sin(self._z_angle),
                            np.cos(self._z_angle), 0, 0,
                            0, 0, 1, 0,
                            0, 0, 0, 1])

        rot_z = np.reshape(rot_z, (4, 4))

        return rot_z


def main():
    """
    Example 3
    """

    print('Example 3:')

    a1 = Matrix()       # Rotation in x by 90
    a2 = Matrix()       # Translation in X by 0.75
    a3 = Matrix()       # Rotation in Z by 30
    a4 = Matrix()       # Rotation in Z by -30
    a5 = Matrix()       # Translation in X by 0.5

    print()
    print('Rotation in X by 90:')
    print(a1.rot_x(45))
    print()

    print()
    print('Translation in X by 0.75:')
    print(a2.trans_x(0.75))
    print()
    print('Rotation in Z by 30')
    print(a3.rot_z(30))

    print()
    print('First Individual Transform:')
    print('Rotation in X by 90 x Translation in X by 0.75 x Rotation in Z by 30:')
    print(np.matmul((np.matmul(a1.rot_x(90), a2.trans_x(0.75))), a3.rot_z(30)))

    print()
    print('Rotation in Z by 30:')
    print(a4.rot_z(-30))
    print()
    print('Translation in X by 0.5:')
    print(a5.trans_x(0.55))
    print()
    print('Second Individual Transform:')
    print('Rotation in Z by 30 x Translation in X by 0.5')
    print(np.matmul(a4.rot_z(-30), a5.trans_x(0.55)))

    print()
    print('Product of both transforms:')
    a6 = np.matmul(np.matmul((np.matmul(a1.rot_x(90), a2.trans_x(0.75))), a3.rot_z(30)),
                   np.matmul(a4.rot_z(-30), a5.trans_x(0.55)))
    print(a6)

    print()
    print('G:')
    a7 = np.float32([0.1, 0.1, 0, 1])
    a7 = np.reshape(a7, (4, 1))
    print(a7)

    print()
    print('Final Countdown:')
    print(np.matmul(a6, a7))

    return


if __name__ == '__main__':
    main()
