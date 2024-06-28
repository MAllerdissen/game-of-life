"""
This module stores the constents used for the game
Author: Martin Allerdissen
Date: Jun 20, 2024
"""
#--- colors --- 
#RGB colors
LIGHT_GRAY = (140, 140, 140)
DARK_GRAY = (64, 64, 64)
YELLOW = (204, 204, 0)

#--- game settings ---
WIDTH, HEIGHT = 900, 900 #should be evenly divisable by TILE_SIZE
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60
UPDATE_FREQ = 60