"""
This modules functions are events which can occure 
Functions:
  mdown(x, y, positions)
    add or remove the position from list of positions to highlight
  spacebar(playing)
    play or pause the game when press spacebar key
  clear(position, playing, count)
    reset game and pause the game
  genearte(position)
    genearte pos to fill board with tiles
Author: Martin Allerdissen
Date: Jun 20, 2024
"""
#=== Imports ===
import random
import constents

#=== Functions ===
def mdown(x, y, positions):
  """
  This function handles the mouse down event by using the position of the mouse to either remove or add the position of the tile from position list.
  Paramater: 
    x: x coridinate of mouse
      dateType: int
    y: y coridinate of mouse
      dataType: int
    positions: array of set of x and y positions highlighted
      dataType: set[tupple]
  Return: n/a
  """
  col = x // constents.TILE_SIZE
  row = y // constents.TILE_SIZE
  pos = (col, row)
  
  if pos in positions:
    positions.remove(pos)
  else:
    positions.add(pos)

def spacebar(playing):
  """
  This function pauses or unpauses the game when spacebar key is pressed
  Paramater: 
    playing: if the game is running or not
      dataType: boolean
  Return: 
    playing: if the game is running or not
      dataType: boolean
  """
  if playing == True:
    playing = False
  else:
    playing = True
  return playing

def clear(positions, playing, count):
  """
  This function clears the game when c key is pressed as well as pausing and reseting the count
  Paramater: 
    positions: set of the (x, y) cordinates of tiles on grid that are alive
      dataType: set[tupple]
    playing: if the game is running or not
      dataType: boolean
    count: increment that resets when hitting 120
      dataType: int
  Return: 
    positions: set of the (x, y) cordinates of tiles on grid that are alive
      dataType: set[tupple]
    playing: if the game is running or not
      dataType: boolean
    count: increment that resets when hitting 120
      dataType: int
  """
  positions = set()
  playing = False
  count = 0
  return positions, playing, count

def generate(positions):
  """
  This function assigns random positions to be alive tiles determined using grid width and abitrary values
  Paramater: 
    positions: set of the (x, y) cordinates of tiles on grid that are alive
      dataType: set[tupple]
  Return: 
    positions: set of the (x, y) cordinates of tiles on grid that are alive
      dataType: set[tupple]
  """
  positions = set([(random.randrange(0, constents.GRID_HEIGHT), random.randrange(0, constents.GRID_WIDTH)) for i in range(random.randrange(4, 10) * constents.GRID_WIDTH)])
  return positions
  
