#Python 3.4.3 with Pygame
import pygame

pygame.init()
pygame.display.set_caption('Crash!')
window = pygame.display.set_mode((300, 300))
running = True

# Draw Once
Rectplace = pygame.draw.rect(window, (255, 0, 0),(100, 100, 100, 100))
pygame.display.update()
# Main Loop
while running:
    # Mouse position and button clicking.
    pos = pygame.mouse.get_pos()
    pressed3 = pygame.mouse.get_pressed()[0]
    # Check if the rect collided with the mouse pos
    # and if the left mouse button was pressed.
    if Rectplace.collidepoint(pos) and pressed3:
        print("You have opened a chest!")
    # Quit pygame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False