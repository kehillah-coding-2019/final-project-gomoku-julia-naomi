import pygame
from pygame import *

class Gomoku:

    def __init__(self):
        self.grid = [[0 for x in range(15)] for y in range(15)]
        self.player_1 = player_1
        self.player_2 = player_2
        self.num_rows = rows
        self.num_cols = cols

        self.num_turns = 0

        pygame.init()
        pygame.font.init()

        self._display_surf = pygame.display.set_mode((100,100), pygame.HWSURFACE | pygame.DOUBLEBUF)

        pygame.display.set_caption('Gomoku')

        self.run = True
        self.play = False
        self.win = False
