import numpy as np

def main():
    np.set_printoptions(precision=3)

    # Example 1

    angle = 30.0
    theta = np.deg2rad(angle)

    rot_z = np.float32([np.cos(theta), -np.sin(theta), 0, np.sin(theta), np.cos(theta), 0, 0, 0, 1])
    rot_z = np.reshape(rot_z, (3, 3))

    print("R_Z({}) =\n {}".format(angle, rot_z))

    # Example 2

    t_rot_z = np.transpose(rot_z)

    print("R_Z^T({}) =\n {}".format(angle, t_rot_z))

    inv_rot_z = np.linalg.inv(rot_z)

    print("R_Z^-1({}) =\n {}".format(angle, inv_rot_z))

    print("R_Z * T_Z^T = \n{}".format(np.matmul(rot_z, t_rot_z)))

    # Example 3

    angle = 45
    theta = np.deg2rad(angle)

    BC_R = np.float32([np.cos(theta), -np.sin(theta), 0, np.sin(theta), np.cos(theta), 0, 0, 0, 1])
    BC_R = np.reshape(BC_R, (3, 3))

    B_P = np.float32([0.5, 0.25, 0.0])
    B_P = np.reshape(B_P, (3, 1))

    C_P = np.matmul(np.transpose(BC_R), B_P)

    print("^B_CR = \n{}".format(BC_R))
    print("^BP = \n{}".format(B_P))
    print("^CP = \n{}".format(C_P))

    return


if __name__ == "__main__":

    main()
