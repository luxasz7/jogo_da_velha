import random
from Tabuleiro import Tabuleiro
from Jogada_pc import Jogada_pc

jogada_pc = Jogada_pc()
class Jogada:
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro

    def usr(self):
        self.slot = input("Digite o espaço que deseja jogar: ")

        while self.slot not in "123456789" or self.slot == "":
            print("Digite um valor válido.")
            self.slot = input("Digite o espaço que deseja jogar: ")
        return int(self.slot)
    
    def pc(self, nivel_dificuldade):
        self.slot = jogada_pc.jogada(nivel_dificuldade, self.tabuleiro)
        return self.slot