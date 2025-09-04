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

    def __init__(self, *components: float):
        self.components = list(components)

    def __str__(self):
        return f"Vector{len(self.components)}({', '.join(str(c) for c in self.components)})"

    def clone(self):
        return self.__class__(*self.components)

    def copy(self, other: "Vector"):
        self.assert_dimension(other)
        self.components = other.components[:]
        return self

    def magnitude(self):
        return math.sqrt(sum(c * c for c in self.components))

    def normalize(self):
        m = self.magnitude()

        if m == 0:
            return self

        self.components = [c / m for c in self.components]

        return self

    def assert_dimension(self, other: "Vector"):
        if len(self.components) != len(other.components):
            raise ValueError("Vector dimension mismatch")

    def dot(self, other: "Vector"):
        self.assert_dimension(other)
        return sum(a * b for a, b in zip(self.components, other.components))

    def add(self, V: "Vector"):
        self.assert_dimension(V)
        self.components = [a + b for a, b in zip(self.components, V.components)]
        return self

    def subtract(self, V: "Vector"):
        self.assert_dimension(V)
        self.components = [a - b for a, b in zip(self.components, V.components)]
        return self

    def multiply(self, s: float):
        self.components = [c * s for c in self.components]
        return self


class Vector2(Vector):
    def rotate_90_cw(self):
        return self.__class__(self.y, -self.x)

    x = component_property(0)
    y = component_property(1)

    u, v = x, y


class Vector3(Vector2):
    z = component_property(2)


class Vector4(Vector3):
    w = component_property(3)


class Quaternion(Vector4):
    pass


class WorldObject:
    position = Vector3(0, 0, 0)
    scale = Vector3(1, 1, 1)
    orientation = Quaternion(0, 0, 0, 1)


class PerspectiveCamera(WorldObject):
    fov = math.pi / 2

    near_clip = 2**0
    far_clip = 2**10


class Triangle:
    E1 = Vector2(0, 0)
    E2 = Vector2(0, 0)
    E3 = Vector2(0, 0)

    min = Vector2(0, 0)
    max = Vector2(0, 0)

    def __init__(self, a: Vector2, b: Vector2, c: Vector2):
        self.a = a
        self.b = b
        self.c = c

        self.update_metadata()

    def __str__(self):
        return f"Triangle(\n  {self.a},\n  {self.b},\n  {self.c}\n)"

    def update_metadata(self):
        self.E1.copy(self.b).subtract(self.a).rotate_90_cw()
        self.E2.copy(self.c).subtract(self.b).rotate_90_cw()
        self.E3.copy(self.a).subtract(self.c).rotate_90_cw()

        self.min.x = min(self.a.x, self.b.x, self.c.x)
        self.min.y = min(self.a.y, self.b.y, self.c.y)
        self.max.x = max(self.a.x, self.b.x, self.c.x)
        self.max.y = max(self.a.y, self.b.y, self.c.y)

    relative_point = Vector2(0, 0)

    def contains(self, point: Vector2):
        b1 = self.relative_point.copy(point).subtract(self.a).dot(self.E1) >= 0
        b2 = self.relative_point.copy(point).subtract(self.b).dot(self.E2) >= 0
        b3 = self.relative_point.copy(point).subtract(self.c).dot(self.E3) >= 0
        return b1 == b2 == b3


scene: list[Triangle] = [
    Triangle(
        Vector2(0, 0),
        Vector2(1, 0.5),
        Vector2(0.5, 1),
    )
]
velocities: list[Vector2] = []

# for i in range(1):
#     a = Vector2(random.random(), random.random())
#     b = Vector2(random.random(), random.random())
#     c = Vector2(random.random(), random.random())

#     scene.append(Triangle(a, b, c))

#     velocities.append(
#         Vector2(random.random() - 0.5, random.random() - 0.5).multiply(0.01)
#     )


class ConsoleRenderer:
    framerate = 30

    def fragment(self, uv: Vector2, xy: Vector2):
        return 1

    def pre_frame(self):
        pass

    _shader_colors = ["  ", "░░", "▒▒", "▓▓", "██"]
    _shader_colors_len = len(_shader_colors)

    def shade(self, b: float):
        i = math.floor(b * self._shader_colors_len)
        i = max(0, min(i, self._shader_colors_len - 1))
        return self._shader_colors[i]

    _image_buffer: list[float] = []

    def target_resolution(self):
        terminal_size = os.get_terminal_size()
        width = math.floor(terminal_size.columns / 2)
        height = terminal_size.lines - 1

        return width, height

    def size_buffer(self):
        width, height = self.target_resolution()

        if len(self._image_buffer) != width * height:
            self._image_buffer = [0] * width * height

        return width, height

    _fragment_xy = Vector2(0, 0)
    _fragment_uv = Vector2(0, 0)

    def frame(self):
        self.pre_frame()
        width, height = self.size_buffer()

        for triangle in scene:
            screen_min_x = int(max(0, math.floor(triangle.min.x * width)))
            screen_max_x = int(min(width - 1, math.ceil(triangle.max.x * width)))
            screen_min_y = int(max(0, math.floor(triangle.min.y * height)))
            screen_max_y = int(min(height - 1, math.ceil(triangle.max.y * height)))

            for y in range(screen_min_y, screen_max_y + 1):
                for x in range(screen_min_x, screen_max_x + 1):
                    self._fragment_xy.x = x
                    self._fragment_xy.y = y
                    self._fragment_uv.u = x / width
                    self._fragment_uv.v = y / height

                    if triangle.contains(self._fragment_uv):
                        f = self.fragment(self._fragment_uv, self._fragment_xy)
                        self._image_buffer[x + y * width] = f

        # for y in range(height):
        #     for x in range(width):
        #         self._fragment_xy.x = x
        #         self._fragment_xy.y = y
        #         self._fragment_uv.u = x / width
        #         self._fragment_uv.v = 1 - y / height

        #         f = self.fragment(self._fragment_uv, self._fragment_xy)

        #         self._image_buffer[x + y * width] = f

        return width, height

    def draw(self):
        width, height = self.frame()
        image = ""

        for y in range(height):
            row = ""

            for x in range(width):
                fragment = self._image_buffer[x + y * width]
                row += self.shade(fragment)

            image += row + "\n"

        print(image, end="\r")

    def loop(self):
        dt = 1 / self.framerate

        while True:
            start = time.time()
            self.draw()
            elapsed = time.time() - start
            wait = max(0, dt - elapsed)
            time.sleep(wait)


# ConsoleRenderer().loop()
ConsoleRenderer().draw()
