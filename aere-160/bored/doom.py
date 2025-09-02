import shutil
import math
import time
from types import SimpleNamespace
import os

rendering = SimpleNamespace()
rendering.frame_rate = 30
rendering.pixel_ascii_map = " ░▒▚▓█"
rendering.pixel_ascii_map_length = len(rendering.pixel_ascii_map)
rendering.padding_x = 0
rendering.padding_y = 2
width = 1
height = 1

player = SimpleNamespace()
player.x = 0
player.y = 0
player.rotation = 0


def fragment(x, y, width, height, current_time):
  return x / width
  return math.sin(current_time) * y / height / 2 + math.cos(current_time) * x / width / 2


def render():
  global width, height

  os.system('cls')

  frame = ''
  current_time = time.time()
  width = round(shutil.get_terminal_size().columns / 2) - \
      2 * rendering.padding_x
  height = shutil.get_terminal_size().lines - rendering.padding_y

  for y in range(height):
    frame += '\n'

    for x in range(width):
      brightness = fragment(x, y, width, height, current_time)
      ascii_index = round(brightness * (rendering.pixel_ascii_map_length - 1))
      half_pixel = rendering.pixel_ascii_map[ascii_index]

      frame += half_pixel + half_pixel

  print(frame)


while True:
  time.sleep(1 / rendering.frame_rate)
  render()
