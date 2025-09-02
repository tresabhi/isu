import os
import time
import math

FRAMERATE = 30


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
