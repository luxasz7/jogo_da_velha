from Clear import Clear

class Tabuleiro:

    def __init__(self):
        self.tabuleiro = [[1,2,3],[4,5,6],[7,8,9]]
        self.usr_points = 0
        self.pc_points = 0
        self.vencedor = ""
    
    def print_tabuleiro(self):
        Clear.clear()
        for line in self.tabuleiro:
            for elemento in line:
                print(elemento, end = ' | ')
            print("\n----------|")

    def aplicar_jogada(self, slot, string):
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == slot:
                    self.tabuleiro[i][j] = string
                    return True
        return False
    
    def verificar_vitoria(self, string):
            for i in range(3):
                if str(self.tabuleiro[i][0]) + str(self.tabuleiro[i][1]) + str(self.tabuleiro[i][2]) == string+string+string:
                    self.atualizar_pontos(string)
                    self.vencedor = string
                    return True
                elif str(self.tabuleiro[0][i]) + str(self.tabuleiro[1][i]) + str(self.tabuleiro[2][i]) == string+string+string:
                    self.atualizar_pontos(string)
                    self.vencedor = string
                    return True
            if str(self.tabuleiro[0][0]) + str(self.tabuleiro[1][1]) + str(self.tabuleiro[2][2]) == string+string+string:
                    self.atualizar_pontos(string)
                    self.vencedor = string
                    return True
            elif str(self.tabuleiro[0][2]) + str(self.tabuleiro[1][1]) + str(self.tabuleiro[2][0]) == string+string+string:
                    self.atualizar_pontos(string)
                    self.vencedor = string
                    return True
            elif self.empate():
                self.vencedor = "empate"
                return True
    
    def atualizar_pontos(self, string):
        if string == "X":
            self.usr_points = self.usr_points + 1
        elif string == "O":
            self.pc_points = self.pc_points +  1

    def vencedor_final(self):
        if self.vencedor == "X":
            self.vencedor = "Usuário"
        elif self.vencedor == "O":
            self.vencedor = "Pc"
        elif self.vencedor == "empate":
            self.vencedor = "Empate"

        print(f"Vencedor: {self.vencedor}\nUsuário: {self.usr_points}\nPc: {self.pc_points}")
        self.tabuleiro = [[1,2,3],[4,5,6],[7,8,9]]

    def empate(self):
        str_q = 0
        for array in self.tabuleiro:
            for i in array:
                if type(i) == str:
                    str_q = str_q + 1
        if str_q == 9:
            return True
        return False