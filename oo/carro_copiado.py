# Criação do carro
class Motor:

    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade >= 2:
            self.velocidade -= 2
        elif self.velocidade == 1:
            self.velocidade -= 1
        else:
            ...

class Direcao:
        direcao_direita={'Norte':'Leste', 'Leste':'Sul', 'Sul':'Oeste', 'Oeste':'Norte'}

        direcao_esquerda={'Norte':'Oeste', 'Oeste':'Sul', 'Sul':'Leste', 'Leste':'Norte'}

        def __init__(self, direcao='Norte'):
            self.direcao = direcao

        def girar_a_direita(self):
            self.direcao = self.direcao_direita[self.direcao]
            return self.direcao

        def girar_a_esquerda(self):
            self.direcao = self.direcao_esquerda[self.direcao]
            return self.direcao

class Carro:
    def __init__(self, motor=Motor(), direcao=Direcao()):
        self.motor = motor
        self.direcao = direcao
        self.sentido = 'Norte'

    def girar_a_direita(self):
        self.sentido = self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.sentido = self.direcao.girar_a_esquerda()

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def velocidade(self):
        print(self.motor.velocidade)



