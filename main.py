import pygame
import sys
import numpy as np
import time

# initializing the constructor
pygame.init()

# screen resolution
res = (1366, 768)

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
    png = pygame.image.load(r"Sprites\idle_" + str(i) + ".png")
    png = pygame.transform.scale(png, (png.get_width() // 2, png.get_height() // 2))  # Resize the image
    pngs.append(png)

# Button position and size
button_width = 140
button_height = 40
button_x = width // 2 - button_width // 2
button_y = height - 100  # Adjust this value to move the button higher

# Load the 10 images
images_not_hovering = [
    pygame.image.load('unhover_1.png'),
    pygame.image.load('unhover_2.png'),
    pygame.image.load('unhover_3.png'),
    pygame.image.load('unhover_3.png'),
    pygame.image.load('unhover_5.png')
]

images_hovering = [
    pygame.image.load('hover_1.png'),
    pygame.image.load('hover_2.png'),
    pygame.image.load('hover_3.png'),
    pygame.image.load('hover_4.png'),
    pygame.image.load('hover_5.png')
]

# Set the initial image index
image_index_not_hovering = 0
image_index_hovering = 0

# Load the audio file
pygame.mixer.music.load('Lament.mp3')
pygame.mixer.music.play(-1)  # Play in infinite loop

# Add a new variable to track whether the mouse has been clicked while hovering
hover_clicked = False

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Check if the mouse is hovering over the middle of the window
    if (width / 2 - 150 < mouse_pos[0] < width / 2 + 150 and
        height / 2 - 50 < mouse_pos[1] < height / 2 + 50):
        current_image = images_hovering[image_index_hovering]
        image_index_hovering = (image_index_hovering + 1) % 5  # Cycle through the hovering images
        # checks if a mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            hover_clicked = True
            background_image = pygame.image.load('Dyzanges.png')  # Load the background image
            screen.blit(background_image, (0, 0))  # Draw the background image on the screen
            pygame.mixer.music.stop()  # Stop the audio
            pygame.mixer.music.load('Ascend.mp3')  # Load the new music (Ascend)
            pygame.mixer.music.play(-1)  # Play the new music on loop
    else:
        current_image = images_not_hovering[image_index_not_hovering]
        image_index_not_hovering = (image_index_not_hovering + 1) % 5  # Cycle through the not hovering images

    # fills the screen with a color
    if hover_clicked:
        # Start the simulation
        for i, png in enumerate(pngs):
            screen.blit(png, (300, height // 2 - png.get_height() // 4))
            pygame.display.update()
            time.sleep(0.1)  # Control the animation speed
    else:
        # Draw the current image on the screen
        screen.blit(current_image, (0, 0))  # Draw the current image

    # updates the frames of the game
    pygame.display.update()

    # Control the frame rate
    time.sleep(0.1)
