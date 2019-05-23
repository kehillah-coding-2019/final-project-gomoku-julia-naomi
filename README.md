# Final Project - Gomoku

**Requirements:**

``
pip install pygame
``

**How to Run**
First cd into class:
``
cd final-project-gomoku-julia-naomi
``
Then run the main file:
``
python3 main.py
``

class Gomoku
 def __init__(self, player_1, player_2, width, height):
  Initiates the function and sets up players

 def execute(self):
 Runs on execute, draws the board

 def event(self, event):
 Detects mouse clicks, assigns a number to the player

 def render(self):
 Draws each piece and the turn info

 def drawBoard(self):
 Draws the Gomoku board

 def drawPiece(self):
 Draws the game pieces

 def turnInfo(self):
 Displays whose turn it is

 def createButton(self, msg,x,y,w,h,ic,ac, tc, action=None):
 Creates a button template for future use

 def displayButton(self)
 Shows the button in order to start the game

 def checkWin(self, pos, player)
 Determines who wins (checks after every turn)
