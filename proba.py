import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Title")

# Set up the font
font = pygame.font.Font(None, 36)
text = font.render("Moving Title", True, (255, 255, 255))
text_rect = text.get_rect()

# Initial position of the text
x, y = 100, 100
speed = 2

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the position of the text
    x += speed
    if x >= WIDTH - text_rect.width or x <= 0:
        speed *= -1
    
    # Fill the screen with black
    screen.fill((0, 0, 0))
    
    # Draw the text at the current position
    screen.blit(text, (x, y))
    
    # Update the display
    pygame.display.flip()
    
    # Control the frame rate
    pygame.time.Clock().tick(60)
