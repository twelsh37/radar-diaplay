# -*- coding: utf-8 -*-
"""
 Show how to do a radar sweep.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Expanded on from work above.
 Added backgrounds, text, labels, images, etc.
"""
# Import a library of functions called 'pygame'
import pygame
import math

# Initialize the game engine
pygame.init()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
NEONGREEN = (57, 255, 20)
ORANGE = (255, 165, 0)


PI = 3.141592653

# Set up the constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900

SWEEP_LENGTH = 450

CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2

FS = pygame.font.Font('freesansbold.ttf', 48)
text_1 = FS.render('5', True, WHITE)

# Set the height and width of the screen
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

my_clock = pygame.time.Clock()

# Loop until the user clicks the close button.
done = False

angle = 0

# load our background image
bg = pygame.image.load('bak_radar.png')


while not done:
    screen.blit(bg, (1, 1))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pygame.display.update()

    # # Set Background
    # background = bg
    # Draw the radar sweep
    sysfont = pygame.font.get_default_font()
    font1 = pygame.font.SysFont(None, 32)
    # img1 = font.render(sysfont, True, RED)
    ten = font1.render('10', True, WHITE)
    twenty = font1.render('20', True, WHITE)
    thirty = font1.render('30', True, WHITE)
    fourty = font1.render('40', True, WHITE)

    # Draw the outline of a circle to 'sweep' the line around
    # Center circle Ground 0
    box_dimensions0 = [400, 400, 100, 100]
    # 5 mile marker
    box_dimensions1 = [350, 350, 200, 200]
    # 10 mile marker
    box_dimensions11 = [299, 299, 300, 300]
    box_dimensions111 = [296, 296, 305, 305]
    # 15 mile marker
    box_dimensions2 = [250, 250, 400, 400]
    # 20 mile marker
    box_dimensions22 = [199, 199, 500, 500]
    box_dimensions222 = [196, 196, 505, 505]
    # 25 mile marker
    box_dimensions3 = [150, 150, 600, 600]
    # 30 mile marker
    box_dimensions33 = [99, 99, 700, 700]
    box_dimensions333 = [96, 96, 705, 705]
    # 35 mile marker
    box_dimensions4 = [50, 50, 800, 800]
    # 40 mile marker
    box_dimensions5 = [0, 0, 900, 900]
    box_dimensions55 = [3, 3, 895, 895]

    # Draw the outline of a circle to 'sweep' the line around
    pygame.draw.ellipse(screen, WHITE, box_dimensions0, 1)
    pygame.draw.ellipse(screen, GREEN, box_dimensions1, 1)
    pygame.draw.ellipse(screen, GREEN, box_dimensions11, 2)
    pygame.draw.ellipse(screen, GREEN, box_dimensions2, 1)
    pygame.draw.ellipse(screen, GREEN, box_dimensions22, 2)
    pygame.draw.ellipse(screen, GREEN, box_dimensions3, 1)
    pygame.draw.ellipse(screen, GREEN, box_dimensions33, 2)
    pygame.draw.ellipse(screen, GREEN, box_dimensions4, 1)
    pygame.draw.ellipse(screen, GREEN, box_dimensions5, 5)

    #  Draw our quarants
    # Drawing a red line from (0, 100) to (200, 100) of thickness 5
    pygame.draw.line(screen, pygame.Color(WHITE), (0, 450), (900, 450), 1)
    pygame.draw.line(screen, pygame.Color(WHITE), (450, 0), (450, 900), 1)
    pygame.draw.line(screen, pygame.Color(WHITE), (132, 768), (768,132), 1)
    pygame.draw.line(screen, pygame.Color(WHITE), (132, 132), (768, 768), 1)

    # Draw the radar line
    x = SWEEP_LENGTH * math.sin(angle) + CENTER_X
    y = SWEEP_LENGTH * math.cos(angle) + CENTER_Y

    # Draw the line from the center at 450, 450 to the calculated end spot
    pygame.draw.line(screen, NEONGREEN, [CENTER_X, CENTER_Y], [x, y], 5)

    # Increase the angle by 0.02 radians
    # Setting this to '+' causes the sweep to go anti-clockwise
    angle = angle - .02

    # If we have done a full sweep, reset the angle to 0
    if angle > 2 * PI:
        angle = angle - 2 * PI


    # West
    screen.blit(ten, (310, 440))
    screen.blit(twenty, (210, 440))
    screen.blit(thirty, (110, 440))
    screen.blit(fourty, (10, 440))
    # East
    screen.blit(ten, (560, 440))
    screen.blit(twenty, (660, 440))
    screen.blit(thirty, (760, 440))
    screen.blit(fourty, (860, 440))
    # North
    screen.blit(ten, (440, 315))
    screen.blit(twenty, (440, 215))
    screen.blit(thirty, (440, 115))
    screen.blit(fourty, (440, 15))
    # South
    screen.blit(ten, (440, 565))
    screen.blit(twenty, (440, 665))
    screen.blit(thirty, (440, 765))
    screen.blit(fourty, (440, 865))

    # Flip the display, wait out the clock tick
    pygame.display.flip()
    my_clock.tick(40)

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
