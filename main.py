import pygame
import sys
import numpy as np
import time

# initializing the constructor
pygame.init()

# screen resolution
res = (720, 720)

# opens up a window
screen = pygame.display.set_mode(res)

# color definitions
white_color = (255, 255, 255)
color_black = (0, 0, 0)

# stores the width and height of the screen
width, height = screen.get_width(), screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)

# rendering texts
text_start = smallfont.render('Start', True, white_color)
text_stop = smallfont.render('Stop', True, white_color)

# variable to store the state of the button
start_button_state = False

# Load the PNG images
pngs = []
for i in range(5):
    i+=1
    pngs.append(pygame.image.load(r"Sprites\idle_" + str(i) + ".png"))

# Button position and size
button_width = 140
button_height = 40
button_x = width // 2 - button_width // 2
button_y = height - 100  # Adjust this value to move the button higher

# Game loop
while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if button_x <= mouse[0] <= button_x + button_width and button_y <= mouse[1] <= button_y + button_height:
                start_button_state = not start_button_state

    # fills the screen with a color
    screen.fill(color_black)

    # Draw the button and text
    button_color = (255, 0, 0) if start_button_state else (0, 255, 0)
    pygame.draw.rect(screen, button_color, [button_x, button_y, button_width, button_height])
    screen.blit(text_start if not start_button_state else text_stop, (button_x + 30, button_y + 5))

    # Animation logic (only run when simulation is running)
    if start_button_state:
        for i, png in enumerate(pngs):
            screen.blit(png, (width // 2 - png.get_width() // 2, height // 2 - png.get_height() // 2))
            pygame.display.update()
            time.sleep(0.1)  # Control the animation speed

    # updates the frames of the game
    pygame.display.update()

    # Control the frame rate
    time.sleep(0.1)