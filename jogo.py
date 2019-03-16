# jogo.py

import random
from baralho import Baralho
from jogador import Jogador
import pygame

def tela(jogador):
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont(None, 18)
    text = font.render("Valor da aposta: R$15,00. Você tem: R$"+str(jogador.getDinheiro())+",00", True, (0, 0, 0))
    screen.blit(text, [5, 5])
    linha = 20
    for i in jogador.getJogo():
        screen.blit(pygame.image.load(i), (linha, 20))
        linha += 80
    font = pygame.font.SysFont(None, 18)
    text = font.render("Pontos: "+str(jogador.getPontos()), True, (0, 0, 0))
    screen.blit(text, [5, 550])
    pygame.display.update()

def pegaCartas(jogador, quantidade):
    for i in range(0, quantidade):
        carta = baralho.getCarta()
        jogador.setCarta(carta,baralho.cartas[carta])


baralho = Baralho()
baralho.embaralhar()
jogador = Jogador()
aposta = 15
while True:
    pygame.init()
    pygame.display.set_caption("Black Jack")
    screen = pygame.display.set_mode((700, 600))
    jogador.reseta()
    pegaCartas(jogador, 2)
    tela(jogador)
    status=""
    run = True
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            pegaCartas(jogador, 1)
            tela(jogador)

            if jogador.getPontos() == 21:
                font = pygame.font.SysFont(None, 18)
                text = font.render("BLACK JACK!!!", True, (0, 0, 0))
                screen.blit(text, [200, 500])
                pygame.display.update()
                jogador.adicionaDinheiro(aposta)
                status = "ganhou"
                run = False
            elif jogador.getPontos() > 21:
                font = pygame.font.SysFont(None, 18)
                text = font.render("ESTOUROU!!!", True, (0, 0, 0))
                screen.blit(text, [200, 500])
                pygame.display.update()
                jogador.subtraiDinheiro(aposta)
                status = "perdeu"
                run = False
        elif keys[pygame.K_n]:
            run = False

    # Joga banca
    if status != "ganhou" and status != "perdeu":
        pontosBanca = random.randint(jogador.getPontos(),30)
        font = pygame.font.SysFont(None, 18)
        text = font.render("Banca jogando... fez " + str(pontosBanca), True, (0, 0, 0))
        screen.blit(text, [200, 400])
        # pygame.display.update()
        if jogador.pontos > pontosBanca or pontosBanca > 21:
            font = pygame.font.SysFont(None, 18)
            text = font.render('Você Ganhou!', True, (0, 0, 0))
            screen.blit(text, [200, 500])
            # pygame.display.update()
            jogador.adicionaDinheiro(aposta)
        else:
            font = pygame.font.SysFont(None, 18)
            text = font.render('Você Perdeu!', True, (0, 0, 0))
            screen.blit(text, [200, 500])
            # pygame.display.update()
            jogador.subtraiDinheiro(aposta)
        pygame.display.update()


    novamente = ""
    run = True
    while run:
        pygame.time.delay(100)
        font = pygame.font.SysFont(None, 18)
        text = font.render("Jogar novamente (S/N)?", True, (0, 0, 0))
        screen.blit(text, [200, 550])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            novamente = "S"
            run = False
        if keys[pygame.K_n]:
            novamente = "N"
            run = False

    if novamente.upper() != "S":
        break
pygame.quit()
