# blackjack.py

import random
from baralho import Baralho
from jogador import Jogador

def mostraJogo(jogador):
    print("**********************************")
    for i in jogador.getJogo():
        print(i)
    print("Pontos: ",jogador.getPontos())
    print("**********************************")

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
    jogador.setPontos(0)
    pegaCartas(jogador, 2)
    mostraJogo(jogador)
    return aposta

baralho = Baralho()
baralho.embaralhar()
jogador = Jogador()
while True:
    aposta = iniciaJogada()
    maisCarta = "s"
    status = ""
    while maisCarta.upper() == "S":
        maisCarta = input("Mais cartas (S/N)?")
        if maisCarta.upper() == "S":
            pegaCartas(jogador, 1)
            mostraJogo(jogador)
            if jogador.getPontos() == 21:
                print("BLACK JACK!!!")
                jogador.adicionaDinheiro(aposta)
                status = "ganhou"
                break
            elif jogador.getPontos() > 21:
                print("Estourou!")
                jogador.subtraiDinheiro(aposta)
                status = "perdeu"
                break

    # Joga banca
    if status != "ganhou" and status != "perdeu":
        pontosBanca = random.randint(jogador.getPontos(),30)
        print("Banca jogando... fez ", pontosBanca)
        if jogador.pontos > pontosBanca or pontosBanca > 21:
            jogador.adicionaDinheiro(aposta)
            print("Você Ganhou! ")
        else:
            jogador.subtraiDinheiro(aposta)
            print("Você Perdeu! ")
