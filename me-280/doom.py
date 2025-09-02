import os
import time
import math


FRAMERATE = 30


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector3(Vector2):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Vector4:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w


class Quaternion(Vector4):
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w


class PerspectiveCamera:
    position = Vector3(0, 0, 0)
    orientation = Quaternion(0, 0, 0, 1)

    fov = math.pi / 2

    near_clip = 2**0
    far_clip = 2**10


def fragment(u, v):
    return math.sin(10 * math.pi * u) * math.cos(10 * math.pi * v)


colors = ["  ", "░░", "▒▒", "▓▓", "██"]
color_len = len(colors)


def shade(b):
    i = max(0.0, min(1.0, b))
    idx = int(i * (color_len - 1))
    return colors[idx]


def frame():
    terminal_size = os.get_terminal_size()
    width = math.floor(terminal_size.columns / 2)
    height = terminal_size.lines - 1
    image = ""

    for y in range(height):
        for x in range(width):
            u = x / terminal_size.columns
            v = y / terminal_size.lines
            f = fragment(u, v)
            c = shade(f)
            image += c

        image += "\n"

    return image


def draw():
    image = frame()
    print(image, end="")


def loop():
    dt = 1 / FRAMERATE

    while True:
        start = time.time()
        draw()
        elapsed = time.time() - start
        wait = max(0, dt - elapsed)
        time.sleep(wait)


loop()
