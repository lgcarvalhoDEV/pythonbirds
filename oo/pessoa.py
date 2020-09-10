class Pessoa:
    def __init__(self, *filhos, nome=None, idade=27):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    jamile = Pessoa(nome='Jamile')
    lucas = Pessoa(jamile, nome='Lucas')
    print(Pessoa.cumprimentar(lucas))
    print(id(lucas))
    print(lucas.cumprimentar())
    print(lucas.nome)
    print(lucas.idade)
    for filho in lucas.filhos:
        print(filho.nome)
    lucas.sobrenome = 'Carvalho'
    del lucas.filhos
    print(lucas.__dict__)
    print(jamile.__dict__)
