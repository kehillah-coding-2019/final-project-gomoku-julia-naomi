import pygame
from pygame import *

black = (0, 0, 0)
white = (245, 245, 245)
beige = (208, 176, 144)
red    = (133, 42, 44)
green  = (26, 81, 79)
blue = (31, 135, 215)
bright_red = (220, 0, 0)
bright_blue = (0, 100, 255)


player = False


class Gomoku:

    def __init__(self, player_1, player_2, width, height):
        self.board = [[0 for x in range(15)] for y in range(15)]
        self.player_1 = player_1
        self.player_2 = player_2
        self.gamewidth = width
        self.gameheight = height
        self.lastpos = [-1, -1]

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
                self.event(event)

            self.displayButton()

            #print(event)

            self.render()

            pygame.display.update()

            self.clock.tick(60)

        pygame.quit()

    def event(self, event):

        global player

        if event.type == pygame.QUIT:
            self.run = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()

            if self.play:

                print(self.board)

                x = (pos[0] - 35 + 35 // 2) // (36)
                y = (pos[1] - 35 + 35 // 2) // (36)

                if 0 <= x < 15 and 0 <= y < 15:
                    if self.board[x][y] == 0:
                        self.lastpos = [x,y]

                        self.board[x][y] = 1 if player else 2

                        if self.win == True:

                            print('You won!')

                        else:
                            
                            player = not player

    def render(self):
        self.drawPiece()

    def drawBoard(self):
        """Draw the gomoku board"""

        self.gameDisplay.fill(white) #background
        pygame.draw.rect(self.gameDisplay, black, [35, 35, 505, 505])

        for x in range(15): #tiles
            for y in range(15):
                pygame.draw.rect(self.gameDisplay, white, [36 * x + 36, 36 * y + 36, 35, 35])

    def drawPiece(self):

        for x in range(15):
            for y in range(15):
                center = (36 * x + 36), (36 * y + 36)
                if self.board[x][y] > 0:
                    if self.board[x][y] == 1:
                        color = white

                    elif self.board[x][y] == 2:
                        color = black

                    pygame.draw.circle(self.gameDisplay, color, center, 35//2 - 1, 0)
                    pygame.draw.circle(self.gameDisplay, black, center, 35//2 - 1, 1)


    def createButton(self, msg,x,y,w,h,ic,ac, tc, action=None):
        """Create button with mouse over and clicking functionality"""
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self.gameDisplay, ac,(x,y,w,h))
            if click[0] == 1 and action != None:
                if action == "play":
                    self.play = True

                if action == "quit":
                    self.play = False


        else:
            pygame.draw.rect(self.gameDisplay, ic,(x,y,w,h))

        smallText = pygame.font.SysFont("Helvetica",25)
        textSurf = smallText.render(msg, True, tc)
        textRect = textSurf.get_rect()

        textRect.centerx = x+ (w/2)
        textRect.centery = y+ (h/2)
        self.gameDisplay.blit(textSurf, textRect)

    def displayButton(self):
        """Display start button"""

        color = red if self.play else blue
        color2 = bright_red if self.play else bright_blue
        info = "Quit" if self.play else "Start"
        action = "quit" if self.play else "play"

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

        self.createButton(info, 240, 600, 100, 50, color, color2, white, action)


        #if 240 + 100 > mouse[0] > 240 and 600 + 50 > mouse[1] > 600:
        #print('The mouse is over the button')
