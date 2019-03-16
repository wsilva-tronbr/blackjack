import pygame

pygame.init()

win = pygame.display.set_mode((100,100))

pygame.display.set_caption("FirstGame")


x= 50
y = 425


run = True
palavra = ""
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            # gets the key name
            key_name = pygame.key.name(event.key)
            print(u'"{}" key pressed'.format(key_name))
            palavra+= str(key_name)


    # keys = pygame.key.get_pressed()


    # win.fill((0,0,0))
    # pygame.draw.rect(win, (255, 0, 0), (x,y, width, height))
    # pygame.display.update()
pygame.quit()
print(palavra)
