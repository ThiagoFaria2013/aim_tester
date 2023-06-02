# importações
import pygame as pg
import random
import time
pg.init()

#parametros
tela = pg.display.set_mode((950, 700), 0)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

class alvos():

    def __init__(self):
        #posição do alvo
        self.posicaox_alvo = random.randint(50,900)
        self.posicaoy_alvo = random.randint(50,650)
        self.posicao_alvo = self.posicaoy_alvo, self.posicaox_alvo
        self.altura_alvo = 20
        self.largura_alvo = 20

    def pintar_alvo(self, tela):
        posicao_alvo = pg.draw.rect(tela, BRANCO, (self.posicaox_alvo, self.posicaoy_alvo, self.altura_alvo, self.largura_alvo))

    def acertar_alvo(self,tela):
        botoes_mouse = pg.mouse.get_pressed()
        if botoes_mouse[0] == 1:
            posicao_mouse = pg.mouse.get_pos()
            print(posicao_mouse)
        else:
            pass


#looping
while True :
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    tela.fill(PRETO)
    alvo = alvos()
    alvo.pintar_alvo(tela)
    alvo.acertar_alvo(tela)
    time.sleep(0.7)
    pg.display.update()