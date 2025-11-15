import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Get current display resolution
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h

# Create fullscreen window
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("DVD Bounce")

# Load the white DVD logo
logo = pygame.image.load("dvd.png").convert_alpha()
logo_rect = logo.get_rect()

# Starting position and velocity
x = random.randint(0, WIDTH - logo_rect.width)
y = random.randint(0, HEIGHT - logo_rect.height)
vx, vy = 3, 3

# Clock for FPS
clock = pygame.time.Clock()

def tint_image(image, color):
    """Apply a color tint to the white logo surface."""
    tinted = image.copy()
    tint_surface = pygame.Surface(image.get_size(), pygame.SRCALPHA)
    tint_surface.fill(color)
    tinted.blit(tint_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    return tinted

# Start with a random color
current_color = (random.randint(50,255), random.randint(50,255), random.randint(50,255))
tinted_logo = tint_image(logo, current_color)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Press ESC to quit fullscreen
                running = False

    # Move logo
    x += vx
    y += vy

    # Collision detection
    hit_wall = False
    if x <= 0 or x + logo_rect.width >= WIDTH:
        vx = -vx
        hit_wall = True
    if y <= 0 or y + logo_rect.height >= HEIGHT:
        vy = -vy
        hit_wall = True

    # On collision, pick a new random color
    if hit_wall:
        current_color = (random.randint(50,255), random.randint(50,255), random.randint(50,255))
        tinted_logo = tint_image(logo, current_color)

    # Draw everything
    screen.fill((0, 0, 0))  # black background
    screen.blit(tinted_logo, (x, y))
    pygame.display.flip()

    # Control FPS
    clock.tick(60)

pygame.quit()
sys.exit()
