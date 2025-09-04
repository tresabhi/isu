import os
import time
import math
import random


def component_property(i):
    return property(
        lambda self: self.components[i],
        lambda self, v: self.components.__setitem__(i, v),
    )


class Vector:
    components = []

    def magnitude(self):
        return math.sqrt(sum(c * c for c in self.components))

    def normalize(self):
        m = self.magnitude()

        if m == 0:
            return self

        self.components = [c / m for c in self.components]

        return self

    def __str__(self):
        return f"<{', '.join(str(c) for c in self.components)}>"

    def __add__(self, other):
        return self.__class__(
            *(a + b for a, b in zip(self.components, other.components))
        )

    def __sub__(self, other):
        return self.__class__(
            *(a - b for a, b in zip(self.components, other.components))
        )

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(*(c * other for c in self.components))

        elif isinstance(other, Vector):
            return sum(a * b for a, b in zip(self.components, other.components))

        else:
            return NotImplemented


class Vector2(Vector):
    def __init__(self, x, y):
        self.components = [x, y]

    def rotate_90_cw(self):
        return self.__class__(self.y, -self.x)

    x = component_property(0)
    y = component_property(1)

    u, v = x, y


class Vector3(Vector2):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.components.append(z)

    z = component_property(2)


class Vector4(Vector3):
    def __init__(self, x, y, z, w):
        super().__init__(x, y, z)
        self.components.append(w)

    w = component_property(3)


class Quaternion(Vector4):
    def __init__(self, x, y, z, w):
        super().__init__(x, y, z, w)


class WorldObject:
    position = Vector3(0, 0, 0)
    scale = Vector3(1, 1, 1)
    orientation = Quaternion(0, 0, 0, 1)


class PerspectiveCamera(WorldObject):
    fov = math.pi / 2

    near_clip = 2**0
    far_clip = 2**10


class DebugTriangle2D:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        self.E1 = (b - a).rotate_90_cw()
        self.E2 = (c - b).rotate_90_cw()
        self.E3 = (a - c).rotate_90_cw()

    def contains(self, P):
        V1 = P - self.a
        V2 = P - self.b
        V3 = P - self.c

        d1 = self.E1 * V1
        d2 = self.E2 * V2
        d3 = self.E3 * V3

        b1 = d1 >= 0
        b2 = d2 >= 0
        b3 = d3 >= 0

        return b1 == b2 == b3


test_triangle = DebugTriangle2D(
    Vector2(0.2, 0.2),
    Vector2(0.7, 0.4),
    Vector2(0.4, 0.8),
)


class ConsoleRenderer:
    framerate = 10

    _shader_colors = ["  ", "░░", "▒▒", "▓▓", "██"]
    _shader_colors_len = len(_shader_colors)

    _fragment_position = Vector2(0, 0)

    def fragment(self, uv):
        return 1 if test_triangle.contains(uv) else 0.5

    def shade(self, b):
        i = math.floor(b * self._shader_colors_len)
        i = max(0, min(i, self._shader_colors_len - 1))
        return self._shader_colors[i]

    def frame(self):
        terminal_size = os.get_terminal_size()
        width = math.floor(terminal_size.columns / 2)
        height = terminal_size.lines - 1
        image = ""

        for y in range(height):
            for x in range(width):
                self._fragment_position.u = x / width
                self._fragment_position.v = 1 - y / height

                f = self.fragment(self._fragment_position)
                c = self.shade(f)

                image += c

            image += "\n"

        return image

    def draw(self):
        image = self.frame()
        print(image, end="")

    def loop(self):
        dt = 1 / self.framerate

        while True:
            start = time.time()
            self.draw()
            elapsed = time.time() - start
            wait = max(0, dt - elapsed)
            time.sleep(wait)


# ConsoleRenderer().frame()
ConsoleRenderer().draw()
