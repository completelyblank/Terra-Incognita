import pygame
import sys
import time
import random

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
    png = pygame.transform.scale(png, (png.get_width() // 1.1, png.get_height() // 1.1))  # Resize the image
    pngs.append(png)

index = 0
# Button position and size
button_width = 140
button_height = 40
button_x = width // 2 - button_width // 2
button_y = height - 100  # Adjust this value to move the button higher

# Load the 10 images
images_not_hovering = [
    pygame.image.load(r"Utilities\unhover_1.png"),
    pygame.image.load(r"Utilities\unhover_2.png"),
    pygame.image.load(r"Utilities\unhover_3.png"),
    pygame.image.load(r"Utilities\unhover_4.png"),
    pygame.image.load(r"Utilities\unhover_5.png")
]

images_hovering = [
    pygame.image.load(r"Utilities\hover_1.png"),
    pygame.image.load(r"Utilities\hover_2.png"),
    pygame.image.load(r"Utilities\hover_3.png"),
    pygame.image.load(r"Utilities\hover_4.png"),
    pygame.image.load(r"Utilities\hover_5.png")
]

# Set the initial image index
image_index_not_hovering = 0
image_index_hovering = 0

# Load the audio file
pygame.mixer.music.load(r"Soundtracks\Lament.mp3")
pygame.mixer.music.play(-1)  # Play in infinite loop

# Add a new variable to track whether the mouse has been clicked while hovering
hover_clicked = False

grid_size = 10
grid_width = 10
grid_height = 10
# Calculate the center of the screen
center_x = width // 2
center_y = height // 2
player_x = center_x
player_y = center_y

# Draw the player at the center of the screen
screen.blit(pngs[index], (center_x, center_y))

# Load the enemy mob images
enemy_pngs = []
for i in range(2):
    i+=1
    enemy_png = pygame.image.load(r"Sprites\skidle_" + str(i) + ".png")
    enemy_png = pygame.transform.scale(enemy_png, (pngs[0].get_width(), pngs[0].get_height()))  # Resize the image to match the player PNG size
    enemy_pngs.append(enemy_png)

# List to store the enemy positions
enemy_positions = []

# Randomly allocate locations for 5 iterations of the mob on the map
for _ in range(20):
    enemy_x = random.randint(0, width - enemy_pngs[0].get_width())
    enemy_y = random.randint(0, height - enemy_pngs[0].get_height())
    enemy_positions.append((enemy_x, enemy_y))

# Initialize health and experience variables
health = 100
experience = 0

# Initialize player stats
player_stats = {'attack': 10, 'defense': 10, 'speed': 10}

# Initialize skeleton stats
skeleton_stats = []
for _ in range(20):
    skeleton_stats.append({'attack': random.randint(5, 15), 'defense': random.randint(5, 15), 'speed': random.randint(5, 15)})

# Load the skerrior animations
skerrior_win_animation = []
skerrior_lose_animation = []
for i in range(1, 7):
    win_image = pygame.image.load(r"Utilities/a_win_" + str(i) + ".jpg")
    lose_image = pygame.image.load(r"Utilities/s_win_" + str(i) + ".jpg")
    skerrior_win_animation.append(win_image)
    skerrior_lose_animation.append(lose_image)

# Load the health bar images
health_bars = []
for i in range(10, 0, -1):
    file_path = f"Utilities/health_{i}.png"  # Use a formatted string for the file path
    health_bar = pygame.image.load(file_path).convert_alpha()  # Use convert_alpha to preserve transparency
    health_bar = pygame.transform.scale(health_bar, (health_bar.get_width() // 3, health_bar.get_height() // 3))
    health_bars.append(health_bar)

# Load the experience bar images
experience_bars = []
for i in range(10):
    experience_bar = pygame.image.load(r"Utilities\exp_" + str(i) + ".png")
    experience_bar = pygame.transform.scale(experience_bar, (experience_bar.get_width() // 3, experience_bar.get_height() // 3))
    experience_bars.append(experience_bar)
    
# Load the death animation images
death_animation = []
for i in range(100):  # 100 is 25s times the number of images
    death_image = pygame.image.load(r"Utilities\death_" + str(i % 5 + 1) + ".png")
    death_animation.append(death_image)
    
# Load the clearing animation images
clear_animation = []
for i in range(100):  # 100 is 25s times the number of images
    clear_image = pygame.image.load(r"Utilities\dyznages_" + str(i % 5 + 1) + ".png")
    clear_animation.append(clear_image)
    
 # Load the food image and resize it
food_image = pygame.image.load(r"Utilities/food.png")
food_image = pygame.transform.scale(food_image, (pngs[0].get_width(), pngs[0].get_height()))

# Generate random food positions
food_positions = []
for _ in range(5):
    food_x = random.randint(0, grid_width - 1)
    food_y = random.randint(0, grid_height - 1)
    food_positions.append((food_x, food_y))

# Check for overlapping positions with skeletons
for i, (food_x, food_y) in enumerate(food_positions):
    while (food_x, food_y) in enemy_positions:
            food_x = random.randint(0, grid_width - 1)
            food_y = random.randint(0, grid_height - 1)
            food_positions[i] = (food_x, food_y)


# Load the chest image and resize it
chest_image = pygame.image.load(r"Utilities\chest.png")
chest_image = pygame.transform.scale(chest_image, (pngs[0].get_width(), pngs[0].get_height()))

# Generate random chest positions
chest_positions = []
for _ in range(5):
    chest_x = random.randint(0, width - chest_image.get_width())
    chest_y = random.randint(0, height - chest_image.get_width())
    while (chest_x, chest_y) in food_positions or (chest_x, chest_y) in enemy_positions:
        chest_x = random.randint(0, width - chest_image.get_width())
        chest_y = random.randint(0, height - chest_image.get_width())
    chest_positions.append((chest_x, chest_y))

# Add a variable to track whether the death animation has finished
death_animation_finished = False
clear_animation_finished = False
range_x=20
range_y=20
r_x=200
r_y=200
def check_interaction(player_x, player_y):
    global health, experience, player_stats
    print("In the function")
    # Check for collisions with chests
    for i, (chest_x, chest_y) in enumerate(chest_positions):
       print(chest_x, chest_y, "and", player_x, player_y)
       if (abs(player_x - chest_x) < r_x) and (abs(player_y - chest_y) < r_y):
            print("In the chest if!")
            stat_increase = random.choice(['attack', 'defense', 'speed'])
            player_stats[stat_increase] += random.randint(1, 5)
            print("Stats increased:", stat_increase)
            chest_positions.pop(i)
            break

    # Check for collisions with enemies
    for i, (enemy_x, enemy_y) in enumerate(enemy_positions):
       if (abs(player_x - enemy_x) < range_x) and (abs(player_y - enemy_y) < range_y):
        
            print("Enemy collision!")
            skeleton = skeleton_stats[i]
            outcome = determine_fight_outcome(player_stats, skeleton)
            if outcome == 'win':
                experience += 10
                play_animation(skerrior_win_animation)
                enemy_positions.pop(i)
                skeleton_stats.pop(i)
            else:
                health -= 20
                play_animation(skerrior_lose_animation)
            break
        
def determine_fight_outcome(player, skeleton):
    player_score = (player['attack'] - skeleton['defense']) + player['speed']
    skeleton_score = (skeleton['attack'] - player['defense']) + skeleton['speed']
    return 'win' if player_score > skeleton_score else 'lose'

def play_animation(animation):
    for frame in animation:
        screen.blit(frame, (center_x, center_y))
        pygame.display.flip()
        pygame.time.delay(100)

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
            background_image = pygame.image.load(r"Utilities\Dyzanges.png")
            screen.blit(background_image, (0, 0))
            pygame.mixer.music.stop()  # Stop the audio
            pygame.mixer.music.load(r"Soundtracks\Ascend.mp3")  # Load the new music (Ascend)
            pygame.mixer.music.play(-1)  # Play the new music on loop
    else:
        current_image = images_not_hovering[image_index_not_hovering]
        image_index_not_hovering = (image_index_not_hovering + 1) % 5  # Cycle through the not hovering images

    # fills the screen with a color
    if hover_clicked:
        # Start the simulation
        for i, png in enumerate(pngs):
            # Get a random direction (up, down, left, right)
            direction = random.choice(['Up', 'Down', 'Left', 'Right'])

            index = (index + 1) % len(pngs)
            
            # Move the player in the random direction
            if direction == 'Up' and player_y > 0:
                player_y -= 5
                # Clear the screen
                screen.fill((0, 0, 0))
                background_image = pygame.image.load(r"Utilities\Dyzanges.png")
                screen.blit(background_image, (0, 0))
                screen.blit(pngs[index], (player_x, player_y))
                for enemy_x, enemy_y in enemy_positions:
                    screen.blit(enemy_pngs[i % 2], (enemy_x, enemy_y))

                # redraw the food image at the random positions
                for food_x, food_y in food_positions:
                    screen.blit(food_image, (food_x * pngs[0].get_width()/2, food_y * pngs[0].get_height()/2))

                # redraw the chests at the random positions
                for chest_x, chest_y in chest_positions:
                    screen.blit(chest_image, (chest_x, chest_y))
                
                 # Check interactions
                check_interaction(player_x, player_y)
                
                # Draw the health bar
                health_bar_index = int((health - 1) / 10)  # Calculate the health bar index from 10 to 0
                if health_bar_index >= 0 and health_bar_index < len(health_bars):
                    screen.blit(health_bars[health_bar_index], (15, 10))  # Draw the health bar

                # Draw the experience bar
                experience_bar_index = int((experience % 100) * 0.1)  # Use modulo to keep experience in range 0-100
                screen.blit(experience_bars[experience_bar_index], (40, 60))  # Draw the experience bar
                # Update the display
                pygame.display.update()

                # Control the frame rate
                time.sleep(0.1)
            elif direction == 'Down' and player_y < grid_height - 1:
                player_y += 5
                # Clear the screen
                screen.fill((0, 0, 0))
                background_image = pygame.image.load(r"Utilities\Dyzanges.png")
                screen.blit(background_image, (0, 0))
                screen.blit(pngs[index], (player_x, player_y))
                # redraw the enemies
                for enemy_x, enemy_y in enemy_positions:
                    screen.blit(enemy_pngs[i % 2], (enemy_x, enemy_y))

                # redraw the food image at the random positions
                for food_x, food_y in food_positions:
                    screen.blit(food_image, (food_x * pngs[0].get_width()/2, food_y * pngs[0].get_height()/2))

                # redraw the chests at the random positions
                for chest_x, chest_y in chest_positions:
                    screen.blit(chest_image, (chest_x, chest_y))
                    
                # Check interactions
                check_interaction(player_x, player_y)
                        
                # Draw the health bar
                health_bar_index = int((health - 1) / 10)  # Calculate the health bar index from 10 to 0
                if health_bar_index >= 0 and health_bar_index < len(health_bars):
                    screen.blit(health_bars[health_bar_index], (15, 10))  # Draw the health bar

                # Draw the experience bar
                experience_bar_index = int((experience % 100) * 0.1)  # Use modulo to keep experience in range 0-100
                screen.blit(experience_bars[experience_bar_index], (40, 60))  # Draw the experience bar
                # Update the display
                pygame.display.update()

                # Control the frame rate
                time.sleep(0.1)
            elif direction == 'Left' and player_x > 0:
                player_x -= 5
                # Clear the screen
                screen.fill((0, 0, 0))
                background_image = pygame.image.load(r"Utilities\Dyzanges.png")
                screen.blit(background_image, (0, 0))
                # Flip the image horizontally
                flipped_png = pygame.transform.flip(pngs[index], True, False)
                screen.blit(flipped_png, (player_x, player_y))
                for enemy_x, enemy_y in enemy_positions:
                    screen.blit(enemy_pngs[i % 2], (enemy_x, enemy_y))

                # redraw the food image at the random positions
                for food_x, food_y in food_positions:
                    screen.blit(food_image, (food_x * pngs[0].get_width()/2, food_y * pngs[0].get_height()/2))

                # redraw the chests at the random positions
                for chest_x, chest_y in chest_positions:
                    screen.blit(chest_image, (chest_x, chest_y))
                    
                 # Check interactions
                check_interaction(player_x, player_y)
                
                # Draw the health bar
                health_bar_index = int((health - 1) / 10)  # Calculate the health bar index from 10 to 0
                if health_bar_index >= 0 and health_bar_index < len(health_bars):
                    screen.blit(health_bars[health_bar_index], (15, 10))  # Draw the health bar

                # Draw the experience bar
                experience_bar_index = int((experience % 100) * 0.1)  # Use modulo to keep experience in range 0-100
                screen.blit(experience_bars[experience_bar_index], (40, 60))  # Draw the experience bar
                # Update the display
                pygame.display.update()

                # Control the frame rate
                time.sleep(0.1)
            elif direction == 'Right' and player_x < grid_width - 1:
                player_x += 5
                # Clear the screen
                screen.fill((0, 0, 0))
                background_image = pygame.image.load(r"Utilities\Dyzanges.png")
                screen.blit(background_image, (0, 0))
                screen.blit(pngs[index], (player_x, player_y))
                for enemy_x, enemy_y in enemy_positions:
                    screen.blit(enemy_pngs[i % 2], (enemy_x, enemy_y))

                # redraw the food image at the random positions
                for food_x, food_y in food_positions:
                    screen.blit(food_image, (food_x * pngs[0].get_width()/2, food_y * pngs[0].get_height()/2))

                # redraw the chests at the random positions
                for chest_x, chest_y in chest_positions:
                    print(chest_x, chest_y)
                    screen.blit(chest_image, (chest_x, chest_y))
                
                 # Check interactions
                check_interaction(player_x, player_y)
                
                # Draw the health bar
                health_bar_index = int((health - 1) / 10)  # Calculate the health bar index from 10 to 0
                if health_bar_index >= 0 and health_bar_index < len(health_bars):
                    screen.blit(health_bars[health_bar_index], (15, 10))  # Draw the health bar

                # Draw the experience bar
                experience_bar_index = int((experience % 100) * 0.1)  # Use modulo to keep experience in range 0-100
                screen.blit(experience_bars[experience_bar_index], (40, 60))  # Draw the experience bar
                # Update the display
                pygame.display.update()

                # Control the frame rate
                time.sleep(0.1)

            # Decrease health over time
            #health -= 1
            
             # Increase experience over time
            #experience += 1

            # Clear the screen
            screen.fill((0, 0, 0))
            background_image = pygame.image.load(r"Utilities\Dyzanges.png")
            screen.blit(background_image, (0, 0))

            # Draw the health bar
            health_bar_index = int((health - 1) / 10)  # Calculate the health bar index from 10 to 0
            if health_bar_index >= 0 and health_bar_index < len(health_bars):
                screen.blit(health_bars[health_bar_index], (15, 10))  # Draw the health bar

            # Draw the experience bar
            experience_bar_index = int((experience % 100) * 0.1)  # Use modulo to keep experience in range 0-100
            screen.blit(experience_bars[experience_bar_index], (40, 60))  # Draw the experience bar

            # Draw the player at the new position
            screen.blit(pngs[0], (player_x, player_y))

            # Draw the enemies
            for enemy_x, enemy_y in enemy_positions:
                screen.blit(enemy_pngs[i % 2], (enemy_x, enemy_y))

            # Draw the food image at the random positions
            for food_x, food_y in food_positions:
                screen.blit(food_image, (food_x * pngs[0].get_width()/2, food_y * pngs[0].get_height()/2))

            # Draw the chests at the random positions
            for chest_x, chest_y in chest_positions:
                screen.blit(chest_image, (chest_x, chest_y))

            # Update the display
            pygame.display.update()

            # Control the frame rate
            time.sleep(0.1)
    else:
        # Draw the current image on the screen
        screen.blit(current_image, (0, 0))  # Draw the current image
        
    # Check if health is 0
    if health <= 0:
        # Stop the music
        pygame.mixer.music.stop()

        # Clear the screen
        screen.fill(("black"))
        
        # Load and play the "Sorrow" music in an infinite loop
        pygame.mixer.music.load(r"Soundtracks\Sorrow.mp3")
        pygame.mixer.music.play(-1)  # Play in infinite loop

        # Play the death animation
        for death_image in death_animation:

            # Draw the death image in the center of the screen
            screen.blit(death_image, (0, 0))

            # Update the display
            pygame.display.update()

            # Wait for a short time before displaying the next image
            time.sleep(0.4)

        # Set the flag to indicate that the death animation has finished
        death_animation_finished = True

    # Check if the death animation has finished
    if death_animation_finished:
        pygame.quit()


    # Check if health is 0
    if experience >= 100:
        # Stop the music
        pygame.mixer.music.stop()

        # Clear the screen
        screen.fill(("black"))
        
        # Load and play the "Sorrow" music in an infinite loop
        pygame.mixer.music.load(r"Soundtracks\Clearing.mp3")
        pygame.mixer.music.play(-1)  # Play in infinite loop

        # Play the death animation
        for clear_image in clear_animation:

            # Draw the death image in the center of the screen
            screen.blit(clear_image, (0, 0))

            # Update the display
            pygame.display.update()

            # Wait for a short time before displaying the next image
            time.sleep(0.4)

        # Set the flag to indicate that the death animation has finished
        clear_animation_finished = True

    # Check if the death animation has finished
    if clear_animation_finished:
        pygame.quit()

    # updates the frames of the game
    pygame.display.update()

    # Control the frame rate
    time.sleep(0.1)
