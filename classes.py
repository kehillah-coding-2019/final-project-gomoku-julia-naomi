import pygame
from pygame import *

class Gomoku:

    def __init__(self, player_1, player_2):
        self.grid = [[0 for x in range(15)] for y in range(15)]
        self.player_1 = player_1
        self.player_2 = player_2

        self.num_turns = 0

        pygame.init()
        pygame.font.init()

        self.gameDisplay = pygame.display.set_mode((800,600))

        pygame.display.set_caption('Gomoku')

        self.clock = pygame.time.Clock()

        self.run = True
        self.play = False
        self.win = False

    def execute(self):
        """Runs on execute"""

        while self.run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                print(event)

            pygame.display.update()

            self.clock.tick(60)

        pygame.quit()

    def play_turn(self):
        if self.num_turns % 2 == 0:
            player = self.player_1
        else:
            player = self.player_2

        if event.type == pygame.QUIT:
            self._running = False
