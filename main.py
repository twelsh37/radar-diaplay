# -*- coding: utf-8 -*-
"""
 Expanded on from work  from simpson.edu.
 Added backgrounds, text, labels, images, etc.

 Show how to do a radar sweep.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""
import pygame
import math
import random

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
NEONGREEN = (57, 255, 20)

# Define constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
SWEEP_LENGTH = 450
CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2
PI = math.pi
RADAR_AREA = PI * 900 * 900

# Set up the font
FS = pygame.font.Font('freesansbold.ttf', 32)

# Set window title
pygame.display.set_caption('Robert Watson-Watt would be proud ...')

# Set the screen size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the clock
clock = pygame.time.Clock()

# Load background image
bg = pygame.image.load('bak_radar.png').convert()

# Define box dimensions
box_dimensions = [
    [400, 400, 100, 100],  # Center circle Ground 0
    [350, 350, 200, 200],  # 5 mile marker
    [299, 299, 300, 300],  # 10 mile marker
    [250, 250, 400, 400],  # 15 mile marker
    [199, 199, 500, 500],  # 20 mile marker
    [150, 150, 600, 600],  # 25 mile marker
    [99, 99, 700, 700],  # 30 mile marker
    [50, 50, 800, 800],  # 35 mile marker
    [0, 0, 900, 900]  # 40 mile marker
]

# Define line coordinates
line_coordinates = [
    [(0, 450), (900, 450)],  # Horizontal line
    [(450, 0), (450, 900)],  # Vertical line
    [(132, 768), (768, 132)],  # Diagonal line 1
    [(132, 132), (768, 768)]  # Diagonal line 2
]

# Define text coordinates
text_coordinates = [
    [(308, 438), (208, 438), (108, 438), (5, 438)],  # West
    [(555, 438), (655, 438), (755, 438), (855, 438)],  # East
    [(435, 310), (432, 210), (432, 110), (432, 9)],  # North
    [(435, 560), (432, 660), (432, 760), (432, 860)]  # South
]

# Define text values
text_values = ['10', '20', '30', '40']

# Define angle
angle = 0

# Load sprite
dot = pygame.image.load('dot.png').convert_alpha()
dot_rect = dot.get_rect()

# Set initial position of sprite
dot_rect.x = random.randint(0, SCREEN_WIDTH)
dot_rect.y = random.randint(0, SCREEN_HEIGHT)

# Define sprite speed and direction
dot_speed = 1
dot_direction = [1, 1]

# Main loop
while True:
    # Draw background
    screen.blit(bg, (1, 1))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Draw circles
    for i, dimensions in enumerate(box_dimensions):
        if i == 0:
            pygame.draw.ellipse(screen, WHITE, dimensions, 1)
        else:
            pygame.draw.ellipse(screen, GREEN, dimensions, 1 if i % 2 == 0 else 2)

    # Draw lines
    for coordinates in line_coordinates:
        pygame.draw.line(screen, WHITE, coordinates[0], coordinates[1], 1)

    # Draw text
    for i, coordinates in enumerate(text_coordinates):
        for j, coordinate in enumerate(coordinates):
            text = FS.render(text_values[j], True, WHITE)
            screen.blit(text, coordinate)

    # Draw radar line
    x = SWEEP_LENGTH * math.sin(angle) + CENTER_X
    y = SWEEP_LENGTH * math.cos(angle) + CENTER_Y
    pygame.draw.line(screen, NEONGREEN, [CENTER_X, CENTER_Y], [x, y], 5)

    # Move sprite
    dot_rect.x += dot_speed * dot_direction[0]
    dot_rect.y += dot_speed * dot_direction[1]

    # Change sprite direction if it hits an edge
    if dot_rect.x < 0 or dot_rect.x > SCREEN_WIDTH - dot_rect.width or dot_rect.y < 0 or dot_rect.y > SCREEN_HEIGHT - dot_rect.height:
        # Change sprite direction randomly
        dot_direction = [random.choice([-1, 2]), random.choice([-1, 1])]

        # Move sprite back inside the radar area
        dot_rect.x = random.randint(0, SCREEN_WIDTH - dot_rect.width)
        dot_rect.y = random.randint(0, SCREEN_HEIGHT - dot_rect.height)

    # Draw sprite
    screen.blit(dot, dot_rect)

    # Increase angle
    angle -= 0.02

    # Reset angle
    if angle > 2 * PI:
        angle -= 2 * PI

    # Flip the display
    pygame.display.flip()

    # Set the clock tick
    clock.tick(40)

# Be IDLE friendly. If you forget this line, the program will 'hang' on exit.
pygame.quit()