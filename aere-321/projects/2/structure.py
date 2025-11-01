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


class Structure:
    def __init__(
        self,
        E: float,
        I: float,
        A: float,
        joints: list[Joint],
        members: list[tuple[int, int]],
    ):
        for member in members:
            pass


lecture_example_1 = Structure(
    29000,
    310,
    11.8,
    [
        Joint(JointType.FIXED, 0, 0),
        Joint(JointType.FREE, 10, 20, 50, 0, -125),
        Joint(JointType.FIXED, 10 + 20, 20),
    ],
    [
        (0, 1),
        (1, 2),
    ],
)
