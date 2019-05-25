import pygame

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

    def __init__(self, width, height, player_1=None, player_2=None):
        self.board = [[0 for x in range(15)] for y in range(15)]
        self.player_1 = player_1
        self.player_2 = player_2

        if self.player_1 == None:
            self.player_1 = "Player1"

        if self.player_2 == None:
            self.player_2 = "Player2"

        self.gamewidth = width
        self.gameheight = height
        self.lastpos = [-1, -1]

        self.num_turns = 0
        self.mouse_on_button = None

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
            events = pygame.event.get()
            for event in events:
                self.event(event)

            self.displayButton()
            self.render()
            self.clock.tick(60)

        pygame.quit()

    def event(self, event):
        """On event"""

        global player

        if event.type == pygame.QUIT:
            self.run = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()

            if self.mouse_on_button:

                if not self.play:
                    self.start()
                    if player:
                        player = not player

            elif self.play:

                #print(self.board)

                x = (pos[0] - 35 + 35 // 2) // (36)
                y = (pos[1] - 35 + 35 // 2) // (36)

                if 0 <= x < 15 and 0 <= y < 15:
                    if self.board[x][y] == 0:
                        self.lastpos = [x,y]

                        self.board[x][y] = 1 if player else 2
                        self.num_turns += 1

                        if self.checkWin([x,y], player):
                            self.win = True
                            self.play = False
                            self.num_turns = 0

                            info = "%s has won the game!" % (player_name)
                            info_font = pygame.font.SysFont('Helvetica', 25)
                            text1 = info_font.render(info, True, black)
                            self.gameDisplay.blit(text1,(400,500))

                        else:

                            player = not player

    def render(self):
        self.drawPiece()
        self.turnInfo()
        pygame.display.update()

    def start(self):
        """Start/reset game"""
        self.play = True
        self.board = [[0 for x in range(15)] for y in range(15)]
        self.lastpos = [-1,-1]
        self.win = False

    def drawBoard(self):
        """Draw the gomoku board"""

        self.gameDisplay.fill(white) #background
        pygame.draw.rect(self.gameDisplay, black, [35, 35, 505, 505])

        for x in range(15): #tiles
            for y in range(15):
                pygame.draw.rect(self.gameDisplay, white, [36 * x + 36, 36 * y + 36, 35, 35])

    def drawPiece(self):
        """Draw each gomoku piece"""

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

    def turnInfo(self):
        """Display who's turn it is"""
        global player_name

        if player == False:
            player_name = self.player_1
        else:
            player_name = self.player_2

        info = "It's your turn, %s" % (player_name) if not self.win else "%s has won the game!" % (player_name)
        info_font = pygame.font.SysFont('Helvetica', 25)
        text = info_font.render(info, True, black)
        self.gameDisplay.blit(text,(200,660))

        info = "Turn #%s" % (self.num_turns)
        info_font = pygame.font.SysFont('Helvetica', 25)
        text = info_font.render(info, True, black)
        self.gameDisplay.blit(text,(500,660))

    def createButton(self, msg,x,y,w,h,ic,ac,tc, action=None):
        """Create button with mouse over and clicking functionality"""
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            self.mouse_on_button = True
            pygame.draw.rect(self.gameDisplay, ac,(x,y,w,h))
            if click[0] == 1 and action != None:
                if action == "play":
                    self.play = True

                if action == "surrender":
                    self.play = False

        else:
            self.mouse_on_button = False
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
        info = "Surrender" if self.play else "Start"
        action = "surrender" if self.play else "play"

        mouse = pygame.mouse.get_pos()

        self.createButton(info, 240, 600, 100, 50, color, color2, white, action)

    def checkWin(self, pos, player):
        """Check win"""

        piece = 1 if player else 2
        if self.board[pos[0]][pos[1]] != piece:
            return False
        directions = [([0,1] , [0,-1]) , ([1,0] , [-1,0]) , ([-1,1] , [1,-1]) , ([1,1] , [-1,-1])]
        for direction in directions:
            streak = 0
            for i in range(2):
                p = pos[:]
                while 0 <= p[0] < 15 and 0 <= p[1] < 15:
                    if self.board[p[0]][p[1]] == piece:
                        streak += 1

                    else:
                        break
                    p[0] += direction[i][0]
                    p[1] += direction[i][1]
            if streak >= 6:
                return True
        return False
