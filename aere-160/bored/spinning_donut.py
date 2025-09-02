import math
import os

SIZE = 35
OUTER_RADIUS = int(SIZE / 2)
INNER_RADIUS = int(OUTER_RADIUS / 4)
SPEED_X = 1
SPEED_Y = 1 / 2

index = 1

while True:
  os.system('cls')

  for y in range(int(-SIZE / 2), int(SIZE / 2)):
    row = ''

    for x in range(int(-SIZE / 2), int(SIZE / 2)):
      theta = index * math.pi / 180
      scaleX =  math.cos(SPEED_X * theta)
      scaleY =  math.sin(SPEED_Y * theta)
      hypot = math.hypot(y / scaleY, x / scaleX)
      row += '##' if hypot <= OUTER_RADIUS and hypot >= INNER_RADIUS else '  '

    print(row)

  index += 1
