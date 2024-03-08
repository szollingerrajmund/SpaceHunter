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
text_x, text_y = WIDTH - text_rect.width, 100

# Set up the ship
ship_img = pygame.Surface((50, 50))
ship_img.fill((255, 0, 0))
ship_rect = ship_img.get_rect(center=(WIDTH//2, HEIGHT//2))

# Movement speed of the ship
ship_speed = 5

# Main loop
show_text = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the ship
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship_rect.x -= ship_speed
    if keys[pygame.K_RIGHT]:
        ship_rect.x += ship_speed

    # Check if ship passes through the window
    if ship_rect.right >= WIDTH and not show_text:
        show_text = True
    
    # Fill the screen with black
    screen.fill((0, 0, 0))
    
    # Draw the ship
    screen.blit(ship_img, ship_rect)
    
    # Draw the text if it should be shown
    if show_text:
        screen.blit(text, (text_x, text_y))
    
    # Update the display
    pygame.display.flip()
    
    # Control the frame rate
    pygame.time.Clock().tick(60)
