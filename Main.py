from Tabuleiro import Tabuleiro
from Jogada import Jogada
from Nivel_Dificuldade import Nivel_dificuldade

dificuldade = Nivel_dificuldade()
nivel_dificuldade = dificuldade.nivel_dificuldade()
tabuleiro = Tabuleiro()
jogada = Jogada(tabuleiro)

while True:

    while True:
        tabuleiro.print_tabuleiro()
        
        while not tabuleiro.aplicar_jogada(jogada.usr(), "X"):
            print("Digite um valor válido.")
            
        if tabuleiro.verificar_vitoria("X"):
            tabuleiro.print_tabuleiro()
            break

        while not tabuleiro.aplicar_jogada(jogada.pc(nivel_dificuldade), "O"):
            continue
        
        if tabuleiro.verificar_vitoria("O"):
            tabuleiro.print_tabuleiro()
            break    
    tabuleiro.vencedor_final()    
    
    jogar_dnv = input("Deseja jogar novamente? Digite N para não, ou qualquer coisa para sim: ").upper()
    if jogar_dnv == "N":
        break
    else:
        continue