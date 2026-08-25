import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Gremlin Game")

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Gremlin Game")

clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Gremlin box
gremlin_x = 250
gremlin_y = 150
gremlin_width = 100
gremlin_height = 60

score = 0

font = pygame.font.SysFont("Arial", 30)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = pygame.mouse.get_pos()

            if gremlin_rect.collidepoint(mouse_x, mouse_y):

                score += 1

                gremlin_x = random.randint(0, 500)
                gremlin_y = random.randint(60, 340)

    # Background
    screen.fill(BLACK)

    # Gremlin
    gremlin_rect = pygame.Rect(
        gremlin_x,
        gremlin_y,
        gremlin_width,
        gremlin_height
    )

    pygame.draw.rect(screen, GREEN, gremlin_rect)

    # Gremlin text
    gremlin_text = font.render("GREMLIN", True, BLACK)
    screen.blit(
        gremlin_text,
        (gremlin_x + 5, gremlin_y + 12)
    )

    # Score
    score_text = font.render(
        f"Captured: {score}",
        True,
        WHITE
    )

    screen.blit(score_text, (20, 20))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()