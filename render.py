"""
This modules functions handle the game enviornment
Functions:
  draw_grid(screen, positions)
    render the grid and tiles on screen
  adjust_grid(positions)
    update tiles based on if they should be alive or not
  get_neighbours(pos)
    get the positions of the nighbours of the alive tiles
Author: Martin Allerdissen
Date: Jun 20, 2024
"""
#== Imports ==
import pygame
import constents

def draw_grid(screen, positions):
  """
  This function uses constents to draw grid with a 0,0 pos system starting in the top left.
  Paramater: 
    screen: window properties
      dateType: surface (pygame)
    pos: set of (x, y) coridates for grid
      dataType: int
  Return: n/a
  """
  screen.fill(constents.DARK_GRAY)

  for row in range(constents.GRID_HEIGHT):
    pygame.draw.line(screen, constents.LIGHT_GRAY, (0, row * constents.TILE_SIZE), (constents.WIDTH, row * constents.TILE_SIZE))

  for col in range(constents.GRID_WIDTH):
    pygame.draw.line(screen, constents.LIGHT_GRAY, (col * constents.TILE_SIZE, 0), (col * constents.TILE_SIZE, constents.HEIGHT))

  for pos in positions: #highlight every tile which position is saved
    (col, row) = pos
    top_left = (col * constents.TILE_SIZE, row * constents.TILE_SIZE)
    pygame.draw.rect(screen, constents.YELLOW, (*top_left, constents.TILE_SIZE, constents.TILE_SIZE))
    
def adjust_grid(positions):
  """
  This function applies the logic of Conways game of life to the tiles on the grid
    1. If a dead tile has 3 alive tiles around it, it becomes alive
    2. An alive tile dies if it has less or more then 2-3 tiles around it
  Paramater: 
    positions: set of the (x, y) cordinates of tiles on grid that are alive
      dataType: set[tupple]
  Return:
    new_positions: position of the tiles which are alive after logic is applied
      dataType: set[tupple]
  """
  all_neighbours = set()
  new_positions = set()
  
  for pos in positions:
    neighbours = get_neighbours(pos)
    all_neighbours.update(neighbours)
    
    neighbours = list(filter(lambda x: x in positions, neighbours))
    
    if len(neighbours) in [2, 3]:
      new_positions.add(pos)
  
  for pos in all_neighbours:
    neighbours = get_neighbours(pos)
    neighbours = list(filter(lambda x: x in positions, neighbours))
    
    if len(neighbours) == 3:
      new_positions.add(pos)
  
  return new_positions

def get_neighbours(pos):
  """
  This function gets the neighbours of the position with time complexity n^2 by iterating through each possible combination of the x-displacment (dx) and y-displacment (dy) on the grid
    | dx:-1,dy: 1 | dx:0,dy: 1 | dx:1,dy: 1 |
    | dx:-1,dy: 0 | dx:0,dy: 0 | dx:1,dy: 0 |
    | dx:-1,dy:-1 | dx:0,dy:-1 | dx:1,dy:-1 |
  Paramater: 
    pos: (x, y) cordinates of an alive tile
      dataType: tupple
  Return:
    neighbours: list of neighbouring tiles that are on the grid and not negative
      dataType: list[tupple]
  """
  x, y = pos
  neighbours = []
  
  for dx in [-1, 0, 1]:
    if x + dx < 0 or x + dx > constents.GRID_WIDTH: #if the dx pos is outside grid bounds skip
      continue
    
    for dy in [-1, 0, 1]:
      if y + dy < 0 or y + dy > constents.GRID_HEIGHT: #if the dy pos is outside grid bounds skip
        continue
      
      if dx == 0 and dy == 0: #if pos has no displacment skip
        continue
      
      neighbours.append((x + dx, y + dy))
  
  return neighbours