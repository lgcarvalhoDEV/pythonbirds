class Pessoa: #definição de Classe
    olhos = 2 # -Atributo default (atributo de classe) - criá-lo quando o valor será o mesmo para todos os objetos. Se não, criar como atributo de instância (INIT).

    def __init__(self, *filhos, nome=None, idade=27):
        self.idade = idade # -Atributo de dado
        self.nome = nome # -Atributo de dado
        self.filhos = list(filhos) # -Atributo complexo - quantidade variável

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
    lucas.sobrenome = 'Carvalho' # -Inserindo atributo dinâmico - em tempo de execução (Não definido no método D.under init) - não aconselhável
    del lucas.filhos # -Deletando atributo em tempo de execução (não aconselhável)
    lucas.olhos = 1
    del lucas.olhos #apagando o atributo dinânico do objeto e tornando-o default
    print(lucas.__dict__) # -Atributo especial para conferir atributos de instância e apenas instância e nao classe (criados no D.under init e também dinamicamente)
    print(jamile.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos) # -Acessando o att através da classe Pessoa
    print(jamile.olhos) # -Acessando o att através do objeto
    print(lucas.olhos)
    print(id(Pessoa.olhos), id(lucas.olhos), id(jamile.olhos))