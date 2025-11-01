import math
import numpy as np
from enum import Enum

np.set_printoptions(linewidth=200)


class Material:
    def __init__(self, E: float, I: float, A: float):
        self.E = E
        self.I = I
        self.A = A


class JointType(Enum):
    FREE = 1
    FIXED = 2


class Joint:
    def __init__(
        self,
        type: JointType,
        x: float,
        y: float,
        force_x=0.0,
        force_y=0.0,
        moment=0.0,
    ):
        self.type = type
        self.x = x
        self.y = y
        self.force_x = force_x
        self.force_y = force_y
        self.moment = moment

    def relative_to(self, other: "Joint"):
        dx = self.x - other.x
        dy = self.y - other.y

        theta = math.atan2(dy, dx)
        L = math.sqrt(dx**2 + dy**2)

        return theta, L


class Member:
    def __init__(
        self, id: int, material: Material, joint_0: Joint, joint_1: Joint, max_id: int
    ):
        theta, L = joint_1.relative_to(joint_0)
        c, s = math.cos(theta), math.sin(theta)

        E, I, A = material.E, material.I, material.A
        K = self.K = ((E * I) / L**3) * np.matrix(
            [
                [
                    (A * L**2 / I) * c**2 + 12 * s**2,
                    ((A * L**2 / I) - 12) * c * s,
                    -6 * L * s,
                    -((A * L**2 / I) * c**2 + 12 * s**2),
                    -((A * L**2 / I) - 12) * c * s,
                    -6 * L * s,
                ],
                [
                    ((A * L**2 / I) - 12) * c * s,
                    (A * L**2 / I) * s**2 + 12 * c**2,
                    6 * L * c,
                    -((A * L**2 / I) - 12) * c * s,
                    -((A * L**2 / I) * s**2 + 12 * c**2),
                    6 * L * c,
                ],
                [-6 * L * s, 6 * L * c, 4 * L**2, 6 * L * s, -6 * L * c, 2 * L**2],
                [
                    -((A * L**2 / I) * c**2 + 12 * s**2),
                    -((A * L**2 / I) - 12) * c * s,
                    6 * L * s,
                    (A * L**2 / I) * c**2 + 12 * s**2,
                    ((A * L**2 / I) - 12) * c * s,
                    6 * L * s,
                ],
                [
                    -((A * L**2 / I) - 12) * c * s,
                    -((A * L**2 / I) * s**2 + 12 * c**2),
                    -6 * L * c,
                    ((A * L**2 / I) - 12) * c * s,
                    (A * L**2 / I) * s**2 + 12 * c**2,
                    -6 * L * c,
                ],
                [-6 * L * s, 6 * L * c, 2 * L**2, 6 * L * s, -6 * L * c, 4 * L**2],
            ]
        )

        top_left_padding = 3 * id
        bottom_right_padding = 3 * (max_id - id)

        K_padded = self.K_padded = np.pad(
            K,
            pad_width=(
                (top_left_padding, bottom_right_padding),
                (top_left_padding, bottom_right_padding),
            ),
        )


class Structure:
    def __init__(
        self, material: Material, joints: list[Joint], members: list[tuple[int, int]]
    ):
        member_id = 0
        joints_count = len(joints)
        max_joint_id = joints_count - 1
        max_member_id = max_joint_id - 1

        S_padded = np.zeros((3 * joints_count, 3 * joints_count))

        for joint_id_0, joint_id_1 in members:
            joint_0 = joints[joint_id_0]
            joint_1 = joints[joint_id_1]
            member = Member(member_id, material, joint_0, joint_1, max_member_id)

            S_padded += member.K_padded
            member_id += 1

        free_indices: list[int] = []
        fixed_indices: list[int] = []
        P_padded: list[list[float]] = []

        for joint_id in range(joints_count):
            joint = joints[joint_id]
            external_indices = [joint_id * 3, joint_id * 3 + 1, joint_id * 3 + 2]

            P_padded += [[joint.force_x], [joint.force_y], [joint.moment]]

            if joint.type == JointType.FREE:
                free_indices += external_indices
            elif joint.type == JointType.FIXED:
                fixed_indices += external_indices

        S = S_padded[np.ix_(free_indices, free_indices)]
        P_padded = np.matrix(P_padded)
        P = P_padded[np.ix_(free_indices)]
        d = np.linalg.solve(S, P)

        d_padded = np.zeros((3 * joints_count, 1))
        d_padded[np.ix_(free_indices)] = d


lecture_example_1 = Structure(
    Material(29000, 310, 11.8),
    [
        Joint(JointType.FIXED, 0, 0),
        Joint(JointType.FREE, 10 * 12, 20 * 12, 50, 0, -125 * 12),
        Joint(JointType.FIXED, (10 + 20) * 12, 20 * 12),
    ],
    [
        (0, 1),
        (1, 2),
    ],
)
