import random

class Jogada_pc:

    def jogada(self, nivel_dificuldade, Tabuleiro):
        match nivel_dificuldade:
            case 1:
                return random.randint(1,10)
            case 2:
                return self.jogada_2(Tabuleiro)
            case 3:
                return random.randint(1,10)
            
    def jogada_2(self, Tabuleiro):
        tabuleiro = Tabuleiro.tabuleiro
        if self.func(tabuleiro, "vencer") != None:
            return self.func(tabuleiro, "vencer")
        else:
            return self.func(tabuleiro, "bloquear")

    def func(self,tabuleiro, string):
        match string:
            case "vencer":
                string1 = "OOO"
                string2 = "OOO"
                string3 = "OOO"
            case "bloquear":
                string1 = "OXX"
                string2 = "XOX"
                string3 = "XXO"

        for array in tabuleiro:
            if "O" + str(array[1]) + str(array[2]) == string1 and array[0] != "O" and array[0] != "X":
                match tabuleiro.index(array):
                    case 0: return 1
                    case 1: return 4
                    case 2: return 7 
            elif str(array[0]) + "O" + str(array[2]) == string2 and array[1] != "O" and array[1] != "X":
                match tabuleiro.index(array):
                    case 0: return 2
                    case 1: return 5
                    case 2: return 8
            elif str(array[0]) + str(array[1]) + "O" == string3 and array[2] != "O" and array[2] != "X":
                match tabuleiro.index(array):
                    case 0: return 3
                    case 1: return 6
                    case 2: return 9

        for i in range(3):
            if "O" + str(tabuleiro[1][i]) + str(tabuleiro[2][i]) == string1 and tabuleiro[0][i] != "O" and tabuleiro[0][i] != "X":
                match tabuleiro[0].index(tabuleiro[0][i]):
                    case 0: return 1
                    case 1: return 2
                    case 2: return 3
            elif str(tabuleiro[0][i]) + "O" + str(tabuleiro[2][i]) == string2 and tabuleiro[1][i] != "O" and tabuleiro[1][i] != "X":
                match tabuleiro[1].index(tabuleiro[1][i]):
                    case 0: return 4
                    case 1: return 5
                    case 2: return 6
            elif str(tabuleiro[0][i]) + str(tabuleiro[1][i]) + "O" == string3 and tabuleiro[2][i] != "O" and tabuleiro[2][i] != "X":
                match tabuleiro[2].index(tabuleiro[2][i]):
                    case 0: return 7
                    case 1: return 8
                    case 2: return 9
        if "O" + str(tabuleiro[1][1]) + str(tabuleiro[2][2]) == string1 and tabuleiro[0][0] != "O" and tabuleiro[0][0] != "X":
            return 1
        elif str(tabuleiro[0][0]) + "O" + str(tabuleiro[2][2]) == string2 and tabuleiro[1][1] != "O" and tabuleiro[1][1] != "X":
            return 5
        elif str(tabuleiro[0][0]) + str(tabuleiro[1][1]) + "O" == string3 and tabuleiro[2][2] != "O" and tabuleiro[2][2] != "X":
            return 9
        elif "O" + str(tabuleiro[1][1]) + str(tabuleiro[2][0]) == string1 and tabuleiro[0][2] != "O" and tabuleiro[0][2] != "X":
            return 3
        elif str(tabuleiro[0][2]) + "O" + str(tabuleiro[2][0]) == string2 and tabuleiro[1][1] != "O" and tabuleiro[1][1] != "X":
            return 5
        elif str(tabuleiro[0][2]) + str(tabuleiro[1][1]) + "O" == string3 and tabuleiro[2][0] != "O" and tabuleiro[2][0] != "X":
            return 7
        if string == "bloquear":
            return self.func2(tabuleiro)
        else:  
            return None
    
    def func2(self, tabuleiro):
        def linhas_func2():
            for array in tabuleiro:
                if array[0] == "O" and type(array[1]) == int and type(array[2]) == int:
                    match tabuleiro.index(array):
                        case 0: return random.choice([2,3])
                        case 1: return random.choice([5,6])
                        case 2: return random.choice([8,9])
                elif type(array[0]) == int and array[1] == "O" and type(array[2]) == int:
                    match tabuleiro.index(array):
                        case 0: return random.choice([1,3])
                        case 1: return random.choice([4,6])
                        case 2: return random.choice([7,9])
                elif type(array[0]) == int and type(array[1]) == int and array[2] == "O":
                    match tabuleiro.index(array):
                        case 0: return random.choice([1,2])
                        case 1: return random.choice([4,5])
                        case 2: return random.choice([7,8])
                else:
                    return None
        def colunas_func2():
            for i in range(3):
                if tabuleiro[0][i] == "O" and type(tabuleiro[1][i]) == int and type(tabuleiro[2][i]) == int:
                    match tabuleiro[0][i]:
                        case 0: return random.choice([4,7])
                        case 1: return random.choice([5,8])
                        case 2: return random.choice([6,9])
                elif type(tabuleiro[0][i]) == int and tabuleiro[1][i] == "O" and type(tabuleiro[2][i]) == int:
                    match tabuleiro[0][i]:
                        case 0: return random.choice([1,7])
                        case 1: return random.choice([2,8])
                        case 2: return random.choice([3,9])
                elif type(tabuleiro[0][i]) == int and type(tabuleiro[1][i]) == int and tabuleiro[2][i] == "O":
                    match tabuleiro[0][i]:
                        case 0: return random.choice([1,4])
                        case 1: return random.choice([2,5])
                        case 2: return random.choice([3,6])
                else:
                    return None
        def diagonais_func2():
            if tabuleiro[0][0] == "O" and type(tabuleiro[1][1]) == int and type(tabuleiro[2][2]) == "O":
                valor = random.choice([5,9])
                return valor
            elif type(tabuleiro[0][0]) == int and tabuleiro[1][1] == "O" and type(tabuleiro[2][2]) == int:
                valor = random.choice([1,9])
                return valor
            elif type(tabuleiro[0][0]) == int and type(tabuleiro[1][1]) == int and tabuleiro[2][2] == "O":
                valor = random.choice([1,5])
                return valor
            elif tabuleiro[0][2] == "O" and type(tabuleiro[1][1]) == int and type(tabuleiro[2][0]) == int:
                valor = random.choice([5,7])
                return valor
            elif type(tabuleiro[0][2]) == int and tabuleiro[1][1] == "O" and type(tabuleiro[2][0]) == int:
                valor = random.choice([3,7])
                return valor
            elif type(tabuleiro[0][2]) == int and type(tabuleiro[1][1]) == int and tabuleiro[2][0] == "O":
                valor = random.choice([1,5])
                return valor
            else:
                return None
            
        chave = random.choice([1,2,3])
        match chave:
            case 1:
                if linhas_func2() != None:
                    return linhas_func2()
                elif colunas_func2() != None:
                    return colunas_func2()
                elif diagonais_func2() != None:
                    return diagonais_func2()
                else:
                    return random.randint(1,10)
            case 2:
                if colunas_func2() != None:
                    return colunas_func2()
                elif linhas_func2() != None:
                    return linhas_func2()
                elif diagonais_func2() != None:
                    return diagonais_func2()
                else:
                    return random.randint(1,10)
            case 3:
                if diagonais_func2() != None:
                    return diagonais_func2()
                elif linhas_func2() != None:
                    return linhas_func2
                elif colunas_func2() != None:
                    return colunas_func2()