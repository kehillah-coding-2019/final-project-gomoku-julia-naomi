# Final Project - Gomoku

Gomoku, also called Five in A Row, is a board game played on a 15 x 15 default grid. Players alternate turns placing their a piece of their color on a intersection. The winner is the first to achieve five pieces in a row either horizantally, vertically, or diagonally. The program may be run unlimited times and resets for each win.

**Requirements:**
***Before running, you must install the prerequisite programs in the requirements.txt file like so:*** 
``
pip install -r requirements.txt
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

### Main Functions

class Gomoku

 #### `def __init__(self, player_1, player_2, width, height):`
  Initiates the function and sets up players

 #### `def execute(self):`
 Runs on execute, draws the board

 #### `def event(self, event):`
 Detects mouse clicks, assigns a number to the player

 #### `def render(self):`
 Draws each piece and the turn info

 #### `def drawBoard(self):`
 Draws the Gomoku board

 #### `def drawPiece(self):`
 Draws the game pieces

 #### `def turnInfo(self):`
 Displays whose turn it is

 #### `def createButton(self, msg,x,y,w,h,ic,ac, tc, action=None):`
 Creates a button template for future use

 #### `def displayButton(self):`
 Shows the button in order to start the game

 #### `def checkWin(self, pos, player):`
 Determines who wins (checks after every turn)

**Watch the Game in Action!**

![image](https://github.com/kehillah-coding-2019/final-project-gomoku-julia-naomi/blob/master/game_example.png)

