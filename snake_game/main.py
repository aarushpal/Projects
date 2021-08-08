import pygame
import time
import random
from pygame.locals import *

SIZE = 40 
BACKGROUND_COLOR = (200,50,130) # RGB value of background  

class Apple:
    def __init__(self,parent_screen):
        self.image = pygame.image.load("snake_game\Resources\sapple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = SIZE*3
        self.y = SIZE*3

    def draw(self):
        self.parent_screen.blit(self.image,(self.x , self.y)) # Blit function draws the image on the screen at the postion defined by self.x and self.y
        pygame.display.flip()

    def move(self): # Initializes the position of the apple to some random coordinates on the screen
        self.x = random.randint(1,24) * SIZE 
        self.y = random.randint(1,19) * SIZE



class Snake:

    def __init__(self,parent_screen,length):
        
        self.parent_screen = parent_screen
        self.block = pygame.image.load("snake_game\Resources\snakeblock.jpg").convert()
        self.direction = 'right'

        self.length = length
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        

    def increase_length(self): # increases length of snake by 1 unit
        self.length+=1
        self.x.append(-1) # Adding to the last element
        self.y.append(-1)

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i], self.y[i]))
            
        pygame.display.flip()

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_right(self):
        self.direction = 'right'

    def move_left(self):
        self.direction = 'left'
    
    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'left':
            self.x[0] -= SIZE

        self.draw()





class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Game by Aarush Pal")
        


        self.surface = pygame.display.set_mode((1000,800))# initializes a window or screen to display. Height and width are passed as parameter
        self.surface.fill(BACKGROUND_COLOR) # fill function fills the screen with a solid color
        self.snake = Snake(self.surface, 1 )
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()


    def is_collission(self,x1,y1,x2,y2): # mechanism for detecting collision 
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def render_background(self):
        bg = pygame.image.load("snake_game\Resources\dbackground.jpg")
        self.surface.blit(bg, (0,0)) # sets the background image    
    
    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        #collision with apple
        if self.is_collission(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()
        # if collision with apple is detected, then increase the length of snake by 1 unit and reposition the apple to some random coordinates

        #collision with itself
        for i in range(3,self.snake.length):
            if self.is_collission(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Game over"
        # if snake collides with itself , then initiate game over mechanism
    
    def display_score(self):
        font = pygame.font.SysFont('arial', 30) # setting the font 
        score = font.render(f"Score: {self.snake.length}" , True , (255,255,255)) 
        self.surface.blit(score , (800,10)) # displaying the score

    def show_game_over(self):
        self.render_background()
        self.surface.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game over!!! Your score is {self.snake.length}", True, (255,255,255))
        self.surface.blit(line1, (325,300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True , (255,255,255))
        self.surface.blit(line2, (325,350))

        pygame.display.flip()

    def reset(self): # resets all the values to initial state
        self.snake = Snake(self.surface , 1)
        self.apple = Apple(self.surface)

    def run(self):
        running = True
        pause = False # will be used to prevent playing the game after gameover

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN: # keyboard strokes
                    if event.key == K_ESCAPE: # pressing esc key exits the game
                        running = False
                    
                    if event.key == K_RETURN: # pressing enter key restarts the game
                        pause = False

                    if not pause:    # controlling the snake based on up, down, right and left arrow key
                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                elif event.type == QUIT:
                    running = False


            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(0.2) # delays the processing 



if __name__ == '__main__':
    game = Game()
    game.run()


