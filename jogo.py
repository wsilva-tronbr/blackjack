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
    text = font.render("Pontos: "+str(jogador.getPontos()), True, (0, 0, 0))
    screen.blit(text, [5, 550])
    text = font.render("Outra carta (S/N)?", True, (0, 0, 0))
    screen.blit(text, [200, 550])
    linha = 20
    for i in jogador.getJogo():
        screen.blit(pygame.image.load(i), (linha, 20))
        linha += 80
    pygame.display.update()

def pegaCartas(jogador, quantidade):
    for i in range(0, quantidade):
        carta = baralho.getCarta()
        jogador.setCarta(carta,baralho.cartas[carta])

def gameOver(mensagem,mult):
    font = pygame.font.SysFont(None, 18)
    text = font.render(mensagem, True, (0, 0, 0))
    screen.blit(text, [200, 500])
    pygame.display.update()
    jogador.resultado(aposta*mult)

pygame.init()
pygame.display.set_caption("Black Jack")
screen = pygame.display.set_mode((700, 600))
baralho = Baralho()
jogador = Jogador()
aposta = 15
while True:
    baralho.embaralhar()
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

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_s]:
                pegaCartas(jogador, 1)
                tela(jogador)

                if jogador.getPontos() == 21:
                    status = "ganhou"
                    gameOver("Black Jack",1)
                    run = False

                elif jogador.getPontos() > 21:
                    status = "perdeu"
                    gameOver("ESTOUROU!!!",-1)
                    run = False

            elif keys[pygame.K_n]:
                run = False

    # Joga banca
    if status != "ganhou" and status != "perdeu":
        pontosBanca = random.randint(jogador.getPontos(),30)
        font = pygame.font.SysFont(None, 18)
        text = font.render("Banca jogando... fez " + str(pontosBanca), True, (0, 0, 0))
        screen.blit(text, [200, 400])
        if jogador.pontos > pontosBanca or pontosBanca > 21:
            gameOver("Você Ganhou!",1)
        else:
            gameOver("Você perdeu!",-1)

    font = pygame.font.SysFont(None, 18)
    text = font.render("Outra carta (S/N)?", True, (255, 255, 255)) # Apaga mensagem
    screen.blit(text, [200, 550])
    text = font.render("Jogar novamente (S/N)?", True, (0, 0, 0))
    screen.blit(text, [200, 550])
    pygame.display.update()
    novamente = ""
    run = True
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
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
