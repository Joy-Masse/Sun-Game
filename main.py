# Hello, this took under an hour of work, including image and sound
# searching. I'm kinda slow, yeah.
# Was inspired by this: https://netsuu.itch.io/rain-game-thing

import pygame
from random import randint
from pygame import key
from pygame import mixer
import math

# Pygame init
pygame.init()

# Screen
SCREEN = pygame.display.set_mode((640, 640))

# Text and font
# Font
font = pygame.font.Font("Roboto-Black.ttf", 12)
font2 = pygame.font.Font("Roboto-Black.ttf", 64)
# Text
text = font.render("you win :0", True, (0, 0, 0))
text2 = ""

# Background image
background = pygame.image.load("background.png")

# Droplet sound
sound = mixer.Sound("sound.wav")

class Sun():
    def __init__(self, x, y, vel_x, vel_y):
        self.image = pygame.image.load("sun.png")
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y

class Drop():
    def __init__(self, x, y):
        self.image = pygame.image.load("drop.png")
        self.x = x
        self.y = y

# Draws things
def draw(sun, drops):

    # Draws usual background when there are drops left and
    # displays "you win :0" when there are none left
    if (len(drops) > 0): 
        SCREEN.blit(background, (0, 0))
        SCREEN.blit(sun.image, (sun.x, sun.y))
        text2 = font2.render(str(len(drops)), True, (0, 0, 0))
        SCREEN.blit(text2, (100, 100))
    else:
        SCREEN.fill((255, 255, 255))
        SCREEN.blit(text, (300, 300))

    # Drops loop
    for i in range(len(drops)):
        SCREEN.blit(drops[i].image, (drops[i].x, drops[i].y))

    pygame.display.update()

# Find distance 
def dist(x1, x2, y1, y2):
    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

# Main
def main():
    # Clock
    clock = pygame.time.Clock()

    # Sun
    sun = Sun(0, 0, 0, 0)

    # Create drops
    drops = []
    for i in range(15):
        drops.append(Drop(randint(0, 600), randint(0, 600)))

    # Game loop
    run = True
    while run:
        # Limits FPS to 60
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Keystroke handling            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            if sun.vel_y > -10:
                sun.vel_y -= 2
        if keys[pygame.K_s]:
            if sun.vel_y < 10:
                sun.vel_y += 2
        if keys[pygame.K_a]:
            if sun.vel_x > -10:
                sun.vel_x -= 2
        if keys[pygame.K_d]:
            if sun.vel_x < 10:
                sun.vel_x += 2

        # Movement system for weird physics emulation
        if sun.vel_y > 0:
            sun.vel_y -= 1
        elif sun.vel_y < 0:
            sun.vel_y += 1
        if sun.vel_x > 0:
            sun.vel_x -= 1
        elif sun.vel_x < 0:
            sun.vel_x += 1

        sun.x += sun.vel_x
        sun.y += sun.vel_y

        # Detecting collision with drops
        for i in range(len(drops)):
            if dist(sun.x, drops[i].x, sun.y, drops[i].y) < 64:
                drops.pop(i)
                sound.play()
                break

        draw(sun, drops)

main()
