import pygame
import sys

# Initialize Pygame
pygame.init()

# Load your background image
background_image = pygame.image.load("images/floor.jpg")  

# Set up a smaller window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Smart Ways To Die")  

background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Handles clicking the X icon
            running = False

    # Draw the background
    screen.blit(background_image, (0, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
