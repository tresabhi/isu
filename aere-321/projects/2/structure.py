import math
import numpy as np
from enum import Enum
import matplotlib.pyplot as plt

np.set_printoptions(linewidth=1600)


class Material:
    def __init__(self, E: float, I: float, A: float):
        self.E = E
        self.I = I
        self.A = A


class JointType(Enum):
    FREE = 1
    FIXED = 2


class Joint:
    id = -1

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
        self,
        id: int,
        material: Material,
        joint_0: Joint,
        joint_1: Joint,
        max_joint_id: int,
    ):
        self.id = id
        self.joint_0 = joint_0
        self.joint_1 = joint_1

        theta, L = joint_1.relative_to(joint_0)
        c, s = math.cos(theta), math.sin(theta)

        E, I, A = material.E, material.I, material.A

        T = self.T = np.matrix(
            [
                [c, s, 0, 0, 0, 0],
                [-s, c, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, c, s, 0],
                [0, 0, 0, -s, c, 0],
                [0, 0, 0, 0, 0, 1],
            ]
        )
        k = self.k = ((E * I) / L**3) * np.matrix(
            [
                [(A * L**2) / I, 0, 0, -(A * L**2) / I, 0, 0],
                [0, 12, 6 * L, 0, -12, 6 * L],
                [0, 6 * L, 4 * L**2, 0, -6 * L, 2 * L**2],
                [-(A * L**2) / I, 0, 0, (A * L**2) / I, 0, 0],
                [0, -12, -6 * L, 0, 12, -6 * L],
                [0, 6 * L, 2 * L**2, 0, -6 * L, 4 * L**2],
            ]
        )
        K = self.K = T.T * k * T

        K_padded = self.K_padded = np.zeros(
            shape=(3 * (max_joint_id + 1), 3 * (max_joint_id + 1))
        )

        indices = [
            joint_0.id * 3,
            joint_0.id * 3 + 1,
            joint_0.id * 3 + 2,
            joint_1.id * 3,
            joint_1.id * 3 + 1,
            joint_1.id * 3 + 2,
        ]

        for u, i in enumerate(indices):
            for v, j in enumerate(indices):
                K_padded[i, j] += K[u, v]


class Structure:
    def __init__(
        self, material: Material, joints: list[Joint], _members: list[tuple[int, int]]
    ):
        self.material = material
        self.joints = joints

        max_joint_id = len(joints) - 1
        max_member_id = len(_members) - 1

        members: list[Member] = []
        member_id = 0
        for joint_id_0, joint_id_1 in _members:
            joint_0 = joints[joint_id_0]
            joint_1 = joints[joint_id_1]

            joint_0.id = joint_id_0
            joint_1.id = joint_id_1

            member = Member(member_id, material, joint_0, joint_1, max_joint_id)

            members.append(member)
            member_id += 1

        self.members = members

        s_padded = sum(member.K_padded for member in members)

        free_indices: list[int] = []
        fixed_indices: list[int] = []
        P_padded: list[list[float]] = []

        for joint_id in range(max_joint_id + 1):
            joint = joints[joint_id]
            external_indices = [joint_id * 3, joint_id * 3 + 1, joint_id * 3 + 2]

            P_padded += [[joint.force_x], [joint.force_y], [joint.moment]]

            if joint.type == JointType.FREE:
                free_indices += external_indices
            elif joint.type == JointType.FIXED:
                fixed_indices += external_indices

        s = s_padded[np.ix_(free_indices, free_indices)]
        P_padded = np.matrix(P_padded)
        P = P_padded[np.ix_(free_indices)]
        d = np.linalg.solve(s, P)

        d_padded = self.d_padded = np.zeros((3 * (max_joint_id + 1), 1))
        d_padded[np.ix_(free_indices)] = d

        for member in members:
            joint_indices = [
                *[member.joint_0.id * 3 + i for i in range(3)],
                *[member.joint_1.id * 3 + i for i in range(3)],
            ]

            v = d_padded[np.ix_(joint_indices)]
            u = member.T * v
            Q = member.k * u

            sigma_a = Q[3].item() / material.A
            epsilon_a = sigma_a / material.E


# lecture_example_1 = Structure(
#     Material(29000, 310, 11.8),
#     [
#         Joint(JointType.FIXED, 0, 0),
#         Joint(JointType.FREE, 10 * 12, 20 * 12, 50, 0, -125 * 12),
#         Joint(JointType.FIXED, (10 + 20) * 12, 20 * 12),
#     ],
#     [
#         (0, 1),
#         (1, 2),
#     ],
# )

structure = Structure(
    Material(10200, (1 * 0.25**3) / 12, 1 * 0.25),
    [
        Joint(JointType.FIXED, 0, 0),
        Joint(JointType.FREE, 0, 8, 0, 0, 100 * 1e-3),
        Joint(JointType.FREE, 0, 8 + 8),
        Joint(JointType.FIXED, 16.25, 0),
        Joint(JointType.FREE, 16.25, 8),
        Joint(JointType.FREE, 16.25, 8 + 8, 10 * 1e-3, 0, 0),
    ],
    [
        (0, 1),
        (1, 2),
        (3, 4),
        (4, 5),
        (1, 4),
        (2, 5),
    ],
)
