from Clear import Clear

class Nivel_dificuldade:

    def nivel_dificuldade(self):
        Clear.clear()
        while True:
            self.dificuldade = input("Digite o nivel de dificuldade do jogo. (1, 2 ou 3):")
            
            try:
                self.dificuldade = int(self.dificuldade)
                if self.dificuldade == 1 or self.dificuldade == 2 or self.dificuldade == 3:
                    break
                else:
                    print("Por favor, digite um dificuldade válida. (1, 2 ou 3)")
                    continue
            except:
                print("Por favor, digite um dificuldade válida. (1, 2 ou 3)")
        return self.dificuldade