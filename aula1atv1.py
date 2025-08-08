# TODO: Use herança para diminuir a repetição de código entre classes relacionadas.
#Feito, código reduzido
class Inimigo:
    def __init__(self, nome, vida, defesa, velocidade, dano_base):
        self.nome = nome
        self.vida = vida
        self.defesa = defesa
        self.carga = 0
        self.velocidade = velocidade
        self.dano_base = dano_base

    def esta_vivo(self):
        if self.vida > 0:
            return True
        else:
            return False
    
    def atacar(self, jogador):
        dano_total = 0
        jogador.vida -= (self.dano_base * (1 - (jogador.defesa)/100) )
        return f"{self.nome}, o Monstro atacou {jogador.nome} causando {dano_total} de dado."



"""
DICA: Repare que as classes Guerreiro e Mago têm muitos atributos e métodos iguais.
"""

class Guerreiro(Inimigo):
    # TODO: Corrija o 'bug' no construtor
    #Nao achei
    def __init__(self, nome, vida, defesa, velocidade, forca):
        super().__init__(nome, vida, defesa, velocidade, forca)
        self.forca = forca


    def atacar(self, inimigo:Inimigo):
        dano_total = self.forca
        # TODO: Faça o Guerreiro(self) retirar vida do Inimigo(inimigo), se baseando na forca atual.
        #Feito
        return f"{self.nome}, o Guerreiro atacou {inimigo.nome} causando {dano_total} de dado."
    

class Mago(Inimigo):
    # TODO: Corrija o 'bug' no construtor
    #Nao achei o bug
    def __init__(self, nome, vida, defesa, velocidade, inteligencia):
        super().__init__(nome, vida, defesa, velocidade, inteligencia)
        self.inteligencia = inteligencia
    
    def atacar(self, inimigo:Inimigo):
        dano_total = self.inteligencia
        # TODO: Faça o Mago(self) retirar vida do Inimigo(inimigo), se baseando na inteligencia atual.
        #Feito!!
        return f"{self.nome}, o Mago atacou {inimigo.nome} causando {dano_total} de dado."

