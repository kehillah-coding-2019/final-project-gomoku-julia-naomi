import pygame
from pygame import *

black = (0, 0, 0)
white = (245, 245, 245)
beige = (208, 176, 144)
red    = (133, 42, 44)
green  = (26, 81, 79)
blue = (31, 135, 215)
bright_blue = (31, 135, 255)


class Gomoku:

    def __init__(self, player_1, player_2, width, height):
        self.grid = [[0 for x in range(15)] for y in range(15)]
        self.player_1 = player_1
        self.player_2 = player_2
        self.gamewidth = width
        self.gameheight = height

        self.num_turns = 0

        pygame.init()
        pygame.font.init()

        self.gameDisplay = pygame.display.set_mode((self.gamewidth,self.gameheight))

        pygame.display.set_caption('Gomoku')

        self.clock = pygame.time.Clock()

        self.run = True
        self.play = False
        self.win = False

    def execute(self):
        """Runs on execute"""

        while self.run:
            self.drawBoard()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            self.displayButton()

            #print(event)

            pygame.display.update()

            self.clock.tick(60)

        pygame.quit()

    def drawBoard(self):
        """Draw the gomoku board"""
        self.gameDisplay.fill(white) #background
        pygame.draw.rect(self.gameDisplay, beige, [25, 20, 525, 525])

        for row in range(14): #tiles
            for column in range(14):
                pygame.draw.rect(self.gameDisplay, white, [36 * column + 36, 36 * row + 36, 35, 35])

    def button(self, msg,x,y,w,h,ic,ac):
        mouse = pygame.mouse.get_pos()

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self.gameDisplay, ac,(x,y,w,h))
            print('The mouse is over the button')
        else:
            pygame.draw.rect(self.gameDisplay, ic,(x,y,w,h))

        smallText = pygame.font.SysFont("Helvetica",25)
        textSurf = smallText.render(msg, True, ic)
        textRect = textSurf.get_rect()

        textRect.centerx = x+ (w/2)
        textRect.centery = y+ (h/2)
        self.gameDisplay.blit(textSurf, textRect)

    def displayButton(self):
        """Display start button"""

        color = blue
        info = "Start"

        mouse = pygame.mouse.get_pos()


        # pygame.draw.rect(self.gameDisplay, color,
        #                  (240, 600, 100, 50))
        #
        # info_font = pygame.font.SysFont('Helvetica', 25)
        # text = info_font.render(info, True, white)
        # textRect = text.get_rect()
        # textRect.centerx = self.gamewidth // 2
        # textRect.centery = self.gameheight - 75
        # self.gameDisplay.blit(text, textRect)

        self.button("start",240,600,100,50,blue,bright_blue)


        #if 240 + 100 > mouse[0] > 240 and 600 + 50 > mouse[1] > 600:
        #print('The mouse is over the button')
        

    def play_turn(self):

        if event.type == pygame.QUIT:
            self.run = False

        global player
        if self.displayButton():
            if not self.play:
                self.start()
                print('Game started!')
                if player:
                    player = not PLAYER
