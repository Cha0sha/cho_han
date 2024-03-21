import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FONT_SIZE = 20
FONT_NAME = "Courier New"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create a Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix Rain")

# Load font
font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)

# Define characters for the rain
characters = [""">\" )
                 ( >)
                  ^^"""]  # ASCII characters from '!' to '~'

# Create raindrop class
class Raindrop(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = font.render(random.choice(characters), True, WHITE)
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        self.rect.y += 2
        if self.rect.y > HEIGHT:
            self.rect.y = random.randint(-HEIGHT, 0)

# Create sprite groups
all_sprites = pygame.sprite.Group()

# Create initial raindrops
for _ in range(100):
    raindrop = Raindrop(random.randint(0, WIDTH), random.randint(0, HEIGHT))
    all_sprites.add(raindrop)

# Main loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update
    all_sprites.update()

    # Draw
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Refresh the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
