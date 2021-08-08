import pygame , sys
import numpy as np
from pygame.constants import K_r

pygame.init() # We have to initialize pygame always before the start of the game

# Defining dimensions of the game window
WIDTH = 600
HEIGHT = 600

# Defining grid size
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH//BOARD_COLS
BG_COLOR = (28 , 170 , 156) 
RED = (255 , 0 , 0)

# Defining grid lines properties
LINE_WIDTH = 15
LINE_COLOR = (23 , 145 , 135)

# Defining circle properties
CIRCLE_RADIUS = SQUARE_SIZE//3
CIRCLE_WIDTH = 15
CIRCLE_COLOR = (239 , 231 , 200)

# Defining cross properties
CROSS_WIDTH = 25
CROSS_COLOR = (66 , 66 , 66)
SPACE = SQUARE_SIZE//4

# Initializing to first player
player = 1
game_over = False # Will be used for game over mechanism

screen = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption('TIC TAC TOE by Aarush Pal') # Setting title at the top of the window
screen.fill(BG_COLOR) # Fills the background color on the display window

######## STRAIGHT LINE FUNCTION DESCRIPTION ########
# pygame.draw.line( screen , RED , (10 , 10) , (300 , 300) , 10)
# Draws a straight line 
# Param 1 - display screen
# Param 2 - color of the line
# Param 3 - starting coordinates of the line
# Param 4 - ending coordinates of the line
# Param 5 - thickness or width of the line
board  = np.zeros((BOARD_ROWS , BOARD_COLS)) # Creates a 3*3 zero matrix 

def mark_square(row , col , player): # Marks a particular square
    board[row][col] = player


def available_square(row , col): # Checks if a single, particular square is filled or not
    if board[row][col] == 0:
        return True
    else:
        return False

def is_board_full(): # Checks if there is a square available to fill or not on the whole board
    for row in BOARD_ROWS:
        for col in BOARD_COLS:
            if board[row][col] == 0:
                return False
    return True

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:  # If player 1 , then draws circle
                pygame.draw.circle( screen , CIRCLE_COLOR , (int(col * SQUARE_SIZE + SQUARE_SIZE//2) , int(row * SQUARE_SIZE + SQUARE_SIZE//2)) , CIRCLE_RADIUS , CIRCLE_WIDTH)

            elif board[row][col] == 2: # If player 2 , then draws cross
                pygame.draw.line(screen , CROSS_COLOR , (col * SQUARE_SIZE + SPACE , row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE , row * SQUARE_SIZE + SPACE) , CROSS_WIDTH)
                pygame.draw.line(screen , CROSS_COLOR , (col * SQUARE_SIZE + SPACE , row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE , row * SQUARE_SIZE + SQUARE_SIZE  - SPACE) , CROSS_WIDTH)    


######## CIRCLE FUNCTION DESCRIPTION ########
# Param 1 - display screen
# Param 2 - color of the circle
# Param 3 - X coordinate of the radius
# Param 4 - Y coordinate of the radius
# Param 5 - thickness or width of the circle


def draw_lines(): # Drawing the grid lines
    # First horizontal line
    pygame.draw.line( screen , LINE_COLOR , (0 , SQUARE_SIZE) , (WIDTH , SQUARE_SIZE) , LINE_WIDTH)
    # Second horizontal line
    pygame.draw.line( screen , LINE_COLOR , (0 , 2 * SQUARE_SIZE) , (WIDTH , 2 * SQUARE_SIZE) , LINE_WIDTH)
    # First vertical line
    pygame.draw.line( screen , LINE_COLOR , (SQUARE_SIZE , 0) , (SQUARE_SIZE , HEIGHT) , LINE_WIDTH)
    # Second vertical line
    pygame.draw.line( screen , LINE_COLOR , (2 * SQUARE_SIZE , 0) , (2 * SQUARE_SIZE , HEIGHT) , LINE_WIDTH)

draw_lines()



def check_win(player): # Checking different winning situations
    # Vertical win check 
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col , player)
            return True

    # Horizontal win check 
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row , player)
            return True

    # Ascending diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    # Descending diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False



# Drawing the lines after winning
def draw_vertical_winning_line(col , player): 
    posX = col * SQUARE_SIZE + SQUARE_SIZE//2

    if player == 1:
        color = CIRCLE_COLOR
    if player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen ,color ,  (posX , 15) , (posX , HEIGHT - 15) , 15)



def draw_horizontal_winning_line(row , player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE//2

    if player == 1:
        color = CIRCLE_COLOR
    if player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen , color , (15 , posY) , ( WIDTH -15 , posY) , 15)

def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    if player == 2:
        color = CROSS_COLOR
    
    pygame.draw.line(screen , color , (15 , HEIGHT - 15 ) , (WIDTH - 15 , 15) , 15)

def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    if player == 2:
        color = CROSS_COLOR
    
    pygame.draw.line(screen , color , (15 , 15 ) , (WIDTH - 15 , HEIGHT - 15) , 15)

# Defining a function that resets the various functions and properties to initial state after a player wins
def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

# Main loop. Game starts here
while True:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Exiting the game if the exit button is clicked
            sys.exit() 
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over: # Checking if the mouse is clicked

            mouseX = event.pos[0] # Stores the value of X coordinate where mouse is clicked
            mouseY = event.pos[1] # Stores the value of Y coordinate where mouse is clicked

            clicked_row =  int(mouseY // SQUARE_SIZE) # Performs integer divison and gives the value of row of the square
            clicked_col = int(mouseX // SQUARE_SIZE) # 200 is the width and height of each square

            if available_square(clicked_row , clicked_col): # Checks if clicked square is available 
                    mark_square(clicked_row , clicked_col , player)
                    if check_win(player): # Marks the square with that player
                        game_over = True
                        
                    player = player % 2 + 1# Changes the player to next player 
                
                    draw_figures()

        if event.type == pygame.KEYDOWN: 
            if event.key == K_r: # If 'r' is pressed on the keyboard, then game resets 
                restart()
                player = 1
                game_over = False


    
    pygame.display.update() # Updates the screen