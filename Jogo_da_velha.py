board = list()
rows = list()
vez = 1
fim = False
fimG = False
jogadas = 0

#Funções:
def fimdejogo():
    print('FIM DE JOGO!!')
    print('Board:')
    print()
    for r in range(0, 3):
        for c in range(0, 3):
            print(f'[{board[r][c]}]', end='')
        print()
    print('=-'*40)

def jogarNovamente():
    print('FIM DE JOGO!!')
    print('Board:')
    print()
    for r in range(0, 3):
        for c in range(0, 3):
            print(f'[{board[r][c]}]', end='')
        print()
    print('=-'*40)
    r = str(input('Deseja jogar novamente?[S/N]')).upper()
    while True:
        if r != 'S' and r != 'N':
            print('Opção inválida!!')
            r = str(input('Deseja jogar novamente?[S/N]')).upper()
        if r == 'N':
            fimG = True
            return fimG
            break
        if r == 'S':
            board.clear()
            break
#INÍCIO DO JOGO
while True:
    jogadas = 0
    fim = False
    #Pergunta o nome dos jogadores:
    print('-'*40)
    jogador1 = str(input('Jogador1: '))
    jogador2 = str(input('Jogador2: '))
    
    #Criação do tabuleiro:
    for c in range(0, 3):
        for r in range(0, 3):
            rows.append('-')
        board.append(rows[:])
        rows.clear()

    #Jogo:
    while True:
        #Exibe o tabuleiro:
        print('Board:')
        print()
        for r in range(0, 3):
            for c in range(0, 3):
                print(f'[{board[r][c]}]', end='')
            print()
        print()
        
        #exibe qual jogador está na vez
        if vez == 1:
            print(f'Vez do(a) {jogador1}')
        else:
            print(f'Vez do(a) {jogador2}')
        
        #Pergunta onde será a jogada:
        r = int(input('Digite a linha da jogada: '))
        c = int(input('Digite a coluna da sua jogada: '))
        print('-'*30)

        #Joga na posição definida
        if vez == 1:
            while True:
                if board[r-1][c-1] == '-':
                    board[r-1][c-1] = 'X'
                    jogadas += 1
                    break
                else:
                    while board[r-1][c-1] != '-':
                        print('Jogada inválida!!')
                        r = int(input('Digite a linha da jogada: '))
                        c = int(input('Digite a coluna da sua jogada: '))
        if vez == 2:
            while True:
                if board[r-1][c-1] == '-':
                    board[r-1][c-1] = 'O'
                    jogadas += 1
                    break
                else:
                    while board[r-1][c-1] != '-':
                        print('Jogada inválida!!')
                        r = int(input('Digite a linha da jogada: '))
                        c = int(input('Digite a coluna da sua jogada: '))
                        
        #Variáveis que verifica a vitória do jogador           
        vitoriaX = 0
        vitoriaO = 0

        #Vitória na horizontal:
        for linha in board:
            if vitoriaX or vitoriaO == 3:
                break
            for coluna in linha:
                if coluna == 'X':
                    vitoriaX += 1
                elif coluna == 'O':
                    vitoriaO += 1
                if vitoriaX == 3:
                    print(f'{jogador1.upper()} VENCEU NA HORIZONTAL!!!')
                    fim = True
                    break
                if vitoriaO == 3:
                    print(f'{jogador2.upper()} VENCEU NA HORIZONTAL!!!')
                    fim = True
                    break
        vitoriaX = 0
        vitoriaO = 0

        #Condição de fim de jogo:
        if fim == True:
            jogarNovamente()
            break
        
        #Vitória na vertical:
        for c in range(0, 3):
            if vitoriaX or vitoriaO == 3:
                break
            for ordeml, valorl in enumerate(board): #Entra na linha
                for ordemc, valorc in enumerate(valorl): #Entra na coluna
                    if valorc == 'X' and ordemc == c:
                        vitoriaX += 1
                    if vitoriaX == 3:
                        print(f'{jogador1.upper()} VENCEU NA VERTICAL!!!')
                        fim = True
                        break
                    if valorc == 'O' and ordemc == c:
                        vitoriaO += 1
                    if vitoriaO == 3:
                        print(f'{jogador2.upper()} VENCEU NA VERTICAL!!!')
                        fim = True
                        break
            vitoriaX = 0
            vitoriaO = 0

        #Condição de fim de jogo:
        if fim == True:
            jogarNovamente()
            break  

        #Vitória na diagonal:
        if board[1][1] == 'X':
            if board[0][0] == 'X' and board[2][2] == 'X':
                print(f'{jogador1.upper()} VENCEU NA DIAGONAL!!!')
                fim = True
            if board[2][2] == 'X' and board[2][0] == 'X':
                print(f'{jogador1.upper()} VENCEU NA DIAGONAL!!!')
                fim = True
        if board[1][1] == 'O':
            if board[0][0] == 'O' and board[2][2] == 'O':
                print(f'{jogador2.upper()} VENCEU NA DIAGONAL!!!')
                fim = True
            if board[2][2] == 'O' and board[2][0] == 'O':
                print(f'{jogador2.upper()} VENCEU NA DIAGONAL!!!')
                fim = True   

        #Condição de fim de jogo:
        if fim == True:
            jogarNovamente()
            break 

        #Condição para dar velha:
        if jogadas == 9:
            print('VELHOU!!!')
            jogarNovamente()
            break

        #altera o jogador que irá fazer a próxima jogada:
        if vez == 1:
            vez = 2
        else:
            vez = 1
    
    #Fim do jogo:
    print(fimG)
    if jogarNovamente() == True:
        fimdejogo()
        break

    
    

