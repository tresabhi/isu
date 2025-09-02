import os
import keyboard
import time
import math

RESOLUTION_X = 64
RESOLUTION_Y = 48
FRAME_RATE = 30


PLAYER_WIDTH = 2
PLAYER_HEIGHT = 4
GRAVITY = -2 ** 6
PLAYER_ACCELERATION_Y = 2 ** 9
PLAYER_ACCELERATION_X = 2 ** 7
player = {
    'x': 0,
    'y': 0,
    'x_velocity': 0,
    'y_velocity': 0,
    'is_touching_bottom': False,
    'is_touching_right': False
}

tiles = [
    '  ',
    '░░',
    '▒▒',
    '▓▓',
    '██',
]

boxes = [
    {
        'x1': -16,
        'y1': -16,
        'x2': 16,
        'y2': 0,
        'value': 2
    },
    {
        'x1': -3,
        'y1': -2,
        'x2': 3,
        'y2': 10,
        'value': 1
    }
]

currentTime = time.time()
lastTime = currentTime
deltaTime = 0


def fragment(x: int, y: int):
  # screen border
  if x == 0 or y == 0 or x == RESOLUTION_X - 1 or y == RESOLUTION_Y - 1:
    return 1

  # player
  if x - 1 <= RESOLUTION_X / 2 <= x + PLAYER_WIDTH - 1 and y + 1 <= RESOLUTION_Y / 2 <= y + 1 + PLAYER_HEIGHT:
    return 3

  # boxes
  for box in boxes:
    if box['x1'] - round(player['x']) <= x - RESOLUTION_X / 2 <= box['x2'] - round(player['x']) and box['y1'] - round(player['y']) <= -y + RESOLUTION_Y / 2 <= box['y2'] - round(player['y']):
      return box['value']

  return 0


def render():
  os.system('cls')
  frame = ''

  for y in range(RESOLUTION_Y):
    frame += '\n'

    for x in range(RESOLUTION_X):
      frame += tiles[fragment(x, y)]

  print(
      f"{frame}\n\n{player['x_velocity']} {player['y_velocity']} {player['is_touching_bottom']}")


def collisions():
  global player, boxes

  player['is_touching_bottom'] = False
  player['is_touching_right'] = False

  for box in boxes:
    minX = min(box['x1'], box['x2'])
    maxX = max(box['x1'], box['x2'])
    minY = min(box['y1'], box['y2'])
    maxY = max(box['y1'], box['y2'])

    if player['y_velocity'] < 0:
      bottomLeftX = player['x'] - PLAYER_WIDTH / 2
      bottomRightX = player['x'] + PLAYER_WIDTH / 2
      bottomY = player['y']

      # falling down check at the bottom of the player
      if (minX < bottomLeftX < maxX or minX < bottomRightX < maxX) and minY < bottomY < maxY:
        player['y'] = maxY
        player['y_velocity'] = 0
        player['is_touching_bottom'] = True

    if player['x_velocity'] > 0:
      rightX = player['x'] + PLAYER_WIDTH / 2
      topRightY = player['y'] + PLAYER_HEIGHT
      bottomRightY = player['y']

      if (minY < topRightY < maxY or minY < bottomRightY < maxY) and minX <= rightX <= maxX:
        player['x'] = minX - PLAYER_WIDTH
        player['x_velocity'] = 0
        player['is_touching_right'] = True


def physics():
  if player['is_touching_bottom']:
    player['y_velocity'] = 0
  else:
    player['y_velocity'] += GRAVITY * deltaTime
    player['y'] += player['y_velocity'] * \
        deltaTime + 0.5 * GRAVITY * deltaTime ** 2

  if player['is_touching_right'] and player['x_velocity'] > 0:
    player['x_velocity'] = 0

  player['x_velocity'] *= 0.8
  player['x'] += player['x_velocity'] * deltaTime


def inputs():
  global player

  if player['is_touching_bottom'] and keyboard.is_pressed('w'):
    player['y_velocity'] += PLAYER_ACCELERATION_Y * deltaTime
  if keyboard.is_pressed('s'):
    player['y_velocity'] -= PLAYER_ACCELERATION_Y * deltaTime
  if keyboard.is_pressed('a'):
    player['x_velocity'] -= PLAYER_ACCELERATION_X * deltaTime
  if not player['is_touching_right'] and keyboard.is_pressed('d'):
    player['x_velocity'] += PLAYER_ACCELERATION_X * deltaTime


while True:
  time.sleep(1 / FRAME_RATE)

  lastTime = currentTime
  currentTime = time.time()
  deltaTime = currentTime - lastTime

  inputs()
  collisions()
  physics()
  render()
