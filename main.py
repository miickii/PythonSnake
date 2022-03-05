import math
import random
from typing import Sized
import pygame
import tkinter as tk
from tkinter import messagebox
from pygame.time import Clock
from pygame.locals import *

WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0,0,0)

BODY_SIZE = 20

class Snake:
    def __init__(self, parent_display, length, s):
        self.length = length
        self.parent_display = parent_display
        self.s = s
        self.expand = False

        # head position
        self.head_x = self.s//2
        self.head_y = self.s//2
        self.head = [self.head_x, self.head_y]
        self.body = [self.head]
        for i in range(1, self.length):
            self.body.append([self.head_x-BODY_SIZE*i, self.head_y])
        self.direction = "right"

    def draw(self):
        self.parent_display.fill((153,255,204))
        for pt in self.body:
            pygame.draw.rect(self.parent_display, BLUE2, pygame.Rect(pt[0], pt[1], BODY_SIZE, BODY_SIZE))
            pygame.draw.rect(self.parent_display, BLUE1, pygame.Rect(pt[0]+4, pt[1]+4, 12, 12))
        

    def turn_up(self):
        self.direction = "up"
    def turn_down(self):
        self.direction = "down"
    def turn_right(self):
        self.direction = "right"
    def turn_left(self):
        self.direction = "left"
    
    def move(self):

        if self.direction == "up":
            self.head_y -= BODY_SIZE
        elif self.direction == "down":
            self.head_y += BODY_SIZE
        elif self.direction == "left":
            self.head_x -= BODY_SIZE
        elif self.direction == "right":
            self.head_x += BODY_SIZE
        
        # updating the head position, and inserting the head as a new value at the start of the "body" list (without removing the previous head)
        self.head = [self.head_x, self.head_y]
        self.body.insert(0, self.head)

        if self.expand: # check to see if the snake has catched food and needs to grow
            self.expand = False
            print(len(self.body))
        else:
            # since we are basically just drawing a new body part at the new position of our snake, we have to delete the last body part so that the snake doesn't just keep getting longer
            self.body.pop()

        self.draw()

    def hit_edge(self):
        if self.head_x < 0 or self.head_x+BODY_SIZE > self.s or self.head_y < 0 or self.head_y > self.s:
            return True
        # snake head hits itself
        if self.head in self.body[1:]:
            return True
        return False
    
    def food_catched(self, food_pos):
        if food_pos[0] == self.head_x and food_pos[1] == self.head_y:
            self.expand = True
            return True

class Game:
    
    def __init__(self):
        pygame.init()
        
        #setting values for window size
        self.s = 640
        self.score = 0
        self.food = []
        self.game_speed = 70

        #init display of game
        self.display = pygame.display.set_mode((self.s, self.s))
        pygame.display.set_caption("Snake")

        self.clock = pygame.time.Clock()

        self.snake = Snake(self.display, 5, self.s)
        self.snake.draw()
        self.place_food()
    
    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_UP:
                        self.snake.turn_up()
                    elif event.key == K_DOWN:
                        self.snake.turn_down()
                    elif event.key == K_LEFT:
                        self.snake.turn_left()
                    elif event.key == K_RIGHT:
                        self.snake.turn_right()
                    pass
                elif event.type == QUIT:
                    running = False
            self.snake.move()

            if self.snake.food_catched(self.food):
                self.score += 1
                if self.game_speed > 20:
                    self.game_speed -= 5
                self.place_food()

            # draw food
            pygame.draw.rect(self.display, RED, pygame.Rect(self.food[0], self.food[1], BODY_SIZE, BODY_SIZE))
            pygame.display.flip()

            if self.snake.hit_edge():
                running = False
            pygame.time.delay(self.game_speed)
    
    def place_food(self):
        food_x = random.randint(0, (self.s-BODY_SIZE)//BODY_SIZE)*BODY_SIZE
        food_y = random.randint(0, (self.s-BODY_SIZE)//BODY_SIZE)*BODY_SIZE
        self.food = [food_x, food_y]
        # if food is placed inside our snake
        if self.food in self.snake.body:
            self.place_food()

    

if __name__ == "__main__":
    game = Game()
    game.run()

    
















































'''class cube(object):
    rows = 20
    w = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color
    
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
    
    def draw(self, surface):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1,dis-2,dis-2))


class snake(object):
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
    pass

def redrawWindow(surface):
    global rows, width, s
    surface.fill((0,0,0))
    cube.draw(surface)
    pass

def main():
    global width, rows, s
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255,0,0),(10,10))
    flag = True
    
    while flag:
        pygame.time.delay(50)
        Clock.tick(10)

        redrawWindow(win)

    pass


main()
def redrawWindow(surface):
    #drawGrid(surface)
def main():
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width, height))
    #s = snake((255,0,0), (10,10))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)

        redrawWindow(win)


    pass'''