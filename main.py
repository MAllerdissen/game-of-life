"""
This program runs conways game of life
Functions:
  main()
    initalizes game and handles events using modules and constents
Author: Martin Allerdissen
Date: Jun 20, 2024
"""
import pygame
import constents, render, actions

#initalize game logic
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
  paused = True
  count = 0
  positions = set()
  
  screen.fill(constents.DARK_GRAY) #set background
  
  while running:
    clock.tick(constents.FPS)
    
    if not paused:
      count += 1
      
    if count >= constents.UPDATE_FREQ: #time until logic applied
      count = 0
      positions = render.adjust_grid(positions)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
        
      if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        actions.mdown(x, y, positions)
      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          paused = actions.spacebar(paused)
          
        if event.key == pygame.K_c:
          positions, paused, count = actions.c(positions, paused, count)
          
        if event.key == pygame.K_g:
          positions = actions.g(positions)
    
    pygame.display.set_caption("Paused" if paused else "Playing") #update gameplay state 
    render.draw_grid(screen, positions)
    pygame.display.update()
  
  pygame.quit()

if __name__ == "__main__":
  main()


