#baralho.py

import random

class Baralho(object):
    asOuros      = "./cartas/as_ouros.png"
    asEspadas     = "./cartas/as_espadas.png"
    asCopas      = "./cartas/as_copas.png"
    asPaus       = "./cartas/as_paus.png"
    doisOuros    = "./cartas/dois_ouros.png"
    doisEspadas   = "./cartas/dois_espadas.png"
    doisCopas    = "./cartas/dois_copas.png"
    doisPaus     = "./cartas/dois_paus.png"
    tresOuros    = "./cartas/tres_ouros.png"
    tresEspadas   = "./cartas/tres_espadas.png"
    tresCopas    = "./cartas/tres_copas.png"
    tresPaus     = "./cartas/tres_paus.png"
    quatroOuros  = "./cartas/quatro_ouros.png"
    quatroEspadas = "./cartas/quatro_espadas.png"
    quatroCopas  = "./cartas/quatro_copas.png"
    quatroPaus   = "./cartas/quatro_paus.png"
    cincoOuros   = "./cartas/cinco_ouros.png"
    cincoEspadas  = "./cartas/cinco_espadas.png"
    cincoCopas   = "./cartas/cinco_copas.png"
    cincoPaus    = "./cartas/cinco_paus.png"
    seisOuros    = "./cartas/seis_ouros.png"
    seisEspadas   = "./cartas/seis_espadas.png"
    seisCopas    = "./cartas/seis_copas.png"
    seisPaus     = "./cartas/seis_paus.png"
    seteOuros    = "./cartas/sete_ouros.png"
    seteEspadas   = "./cartas/sete_espadas.png"
    seteCopas    = "./cartas/sete_copas.png"
    setePaus     = "./cartas/sete_paus.png"
    oitoOuros    = "./cartas/oito_ouros.png"
    oitoEspadas   = "./cartas/oito_espadas.png"
    oitoCopas    = "./cartas/oito_copas.png"
    oitoPaus     = "./cartas/oito_paus.png"
    noveOuros    = "./cartas/nove_ouros.png"
    noveEspadas   = "./cartas/nove_espadas.png"
    noveCopas    = "./cartas/nove_copas.png"
    novePaus     = "./cartas/nove_paus.png"
    dezOuros     = "./cartas/dez_ouros.png"
    dezEspadas    = "./cartas/dez_espadas.png"
    dezCopas     = "./cartas/dez_copas.png"
    dezPaus      = "./cartas/dez_paus.png"
    valeteOuros  = "./cartas/valete_ouros.png"
    valeteEspadas = "./cartas/valete_espadas.png"
    valeteCopas  = "./cartas/valete_copas.png"
    valetePaus   = "./cartas/valete_paus.png"
    damaOuros    = "./cartas/dama_ouros.png"
    damaEspadas   = "./cartas/dama_espadas.png"
    damaCopas    = "./cartas/dama_copas.png"
    damaPaus     = "./cartas/dama_paus.png"
    reiOuros    = "./cartas/rei_ouros.png"
    reiEspadas   = "./cartas/rei_espadas.png"
    reiCopas    = "./cartas/rei_copas.png"
    reiPaus     = "./cartas/rei_paus.png"

    cartas = {asOuros:1, asEspadas:1, asCopas:1, asPaus:1, doisOuros:2, doisEspadas:2, doisCopas:2, doisPaus:2, tresOuros:3, tresEspadas:3, tresCopas:3, tresPaus:3, quatroOuros:4, quatroEspadas:4, quatroCopas:4, quatroPaus:4, cincoOuros:5, cincoEspadas:5, cincoCopas:5, cincoPaus:5, seisOuros:6, seisEspadas:6, seisCopas:6, seisPaus:6, seteOuros:7, seteEspadas:7, seteCopas:7, setePaus:7, oitoOuros:8, oitoEspadas:8, oitoCopas:8, oitoPaus:8, noveOuros:9, noveEspadas:9, noveCopas:9, novePaus:9, dezOuros:10, dezEspadas:10, dezCopas:10, dezPaus:10, valeteOuros:10, valeteEspadas:10, valeteCopas:10, valetePaus:10, damaOuros:10, damaEspadas:10, damaCopas:10, damaPaus:10, reiOuros:10, reiEspadas:10, reiCopas:10, reiPaus:10}

    cartasEmbaralhadas = []

    def __init__(self):
        pass

    def embaralhar(self):
        self.cartasEmbaralhadas = [i for i in self.cartas]
        random.shuffle(self.cartasEmbaralhadas)


    def getCarta(self):
        return self.cartasEmbaralhadas.pop()
