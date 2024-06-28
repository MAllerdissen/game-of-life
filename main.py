"""
This program runs conways game of life
  Game:
    tiles - binary state | alive[yellow] or dead[gray]
    grid - 46x46 grid of square tiles
    turn - rules of game applied to grid
    rules:
      1. 1 turn per sec
      2. if a alive tile neighbours 2-3 alive tiles it remains alive
      3. if a dead tile neighbours 3 alive tiles it becomes alive
      4. if no previous conditions are met the tile becomes dead
Functions:
  main()
    initalizes game and handles events using modules and constents
Author: Martin Allerdissen
Date: Jun 20, 2024
"""
#=== Imports ===
import pygame 
import constents, render, actions

#=== Initalize Game ===
pygame.init()
screen = pygame.display.set_mode((constents.WIDTH, constents.HEIGHT))
clock = pygame.time.Clock()

def main():
  """
  main function initalizes the game and updates on a 60 FPS clock.
  Paramater: n/a
  Return: n/a
  """
  running = True
  playing = False
  count = 0
  positions = set()
  
  screen.fill(constents.DARK_GRAY) #set background
  
  while running:
    #---- clock ----
    clock.tick(constents.FPS)
    
    if playing:
      count += 1
      
    if count >= constents.UPDATE_FREQ: #time until logic applied
      count = 0
      positions = render.adjust_grid(positions)
    
    #---- logic ----
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
        
      if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        actions.mdown(x, y, positions)
      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          playing = actions.spacebar(playing)
          
        if event.key == pygame.K_c:
          positions, playing, count = actions.clear(positions, playing, count)
          
        if event.key == pygame.K_g:
          positions = actions.generate(positions)
    
    #---- update screen ----
    pygame.display.set_caption("Paused" if not playing else "Playing") #update gameplay state 
    render.draw_grid(screen, positions)
    pygame.display.update()
  
  pygame.quit()

if __name__ == "__main__":
  main()