#jogador.py

class Jogador(object):

    jogo = []
    pontos = 0
    dinheiro = 100

    def __init__(self):
        pass

    def getJogo(self):
        return self.jogo

    def reseta(self):
        self.jogo=[]
        self.pontos = 0

    def setCarta(self, carta, indice):
        self.jogo.append(carta)
        self.pontos += indice

    def getPontos(self):
        return self.pontos

    def setPontos(self, pontos):
        self.pontos = pontos

    def getDinheiro(self):
        return self.dinheiro

    def resultado(self, valor):
        self.dinheiro += valor
