# blackjack.py


import random
from baralho import Baralho
from jogador import Jogador
import pygame

def mostraJogo(jogador):
    screen.fill((255, 255, 255))
    text = font.render("Você tem: R$"+str(jogador.getDinheiro())+",00", True, (255, 0, 0))
    screen.blit(text, [5, 5])
    linha = 20
    for i in jogador.getJogo():
        screen.blit(pygame.image.load(i), (linha, 20))
        linha += 80

    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            pass
        break

def pegaCartas(jogador, quantidade):
    for i in range(0, quantidade):
        carta = baralho.getCarta()
        jogador.setCarta(carta,baralho.cartas[carta])

def iniciaJogada():
    print("Voce tem R$", jogador.getDinheiro(), ",00")
    try:
        aposta = int(input("Aposta (sem centavos):"))
    except:
        aposta = 10
    jogador.reseta()
    pegaCartas(jogador, 2)
    mostraJogo(jogador)
    return aposta

pygame.init()
pygame.display.set_caption('BlackJack')
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))

baralho = Baralho()
baralho.embaralhar()
jogador = Jogador()
font = pygame.font.SysFont(None, 18)
text = font.render("Você tem: R$"+str(jogador.getDinheiro())+",00", True, (255, 0, 0))
screen.blit(text, [5, 5])
pygame.display.flip()
while True:
    aposta = iniciaJogada()
    maisCarta = "s"
    status = ""
    while maisCarta.upper() == "S":
        maisCarta = input("Mais cartas (S/N)?")
        if maisCarta.upper() == "S":
            pegaCartas(jogador, 1)
#            mostraJogo(jogador)
            screen.fill((255, 255, 255))
            text = font.render("Você tem: R$"+str(jogador.getDinheiro())+",00", True, (255, 0, 0))
            screen.blit(text, [5, 5])
            print("**********************************")
            linha = 20
            for i in jogador.getJogo():
                screen.blit(pygame.image.load(i), (linha, 20))
                linha += 80

            pygame.display.flip()
            while True:
                for event in pygame.event.get():
                    pass
                break
                # tecla_pressionada = pygame.key.get_pressed()
                # if tecla_pressionada[K_END]:
                #     break

            print("Pontos: ",jogador.getPontos())
            print("**********************************")


            if jogador.getPontos() == 21:
                text = font.render("BLACK JACK!!!", True, (255, 0, 0))
                screen.blit(text, [200, 400])
                pygame.display.flip()
                while True:
                    for event in pygame.event.get():
                        pass
                    break
                jogador.adicionaDinheiro(aposta)
                status = "ganhou"
                break
            elif jogador.getPontos() > 21:
                text = font.render("ESTOUROU!!!", True, (255, 0, 0))
                screen.blit(text, [200, 10])
                text = font.render("Você tem: R$"+str(jogador.getDinheiro())+",00", True, (255, 0, 0))
                screen.blit(text, [5, 5])
                pygame.display.flip()
                while True:
                    for event in pygame.event.get():
                        pass
                    break
                jogador.subtraiDinheiro(aposta)
                status = "perdeu"
                break

    # Joga banca
    if status != "ganhou" and status != "perdeu":
        pontosBanca = random.randint(jogador.getPontos(),30)
        print("Banca jogando... fez ", pontosBanca)
        if jogador.pontos > pontosBanca or pontosBanca > 21:
            jogador.adicionaDinheiro(aposta)
            text = font.render('Você Ganhou!', True, (255, 0, 0))
            screen.blit(text, [100, 400])
            pygame.display.flip()
            while True:
                for event in pygame.event.get():
                    pass
                break
        else:
            jogador.subtraiDinheiro(aposta)
            text = font.render('Você Perdeu!', True, (255, 0, 0))
            screen.blit(text, [100, 400])
            pygame.display.flip()
            while True:
                for event in pygame.event.get():
                    pass
                break
