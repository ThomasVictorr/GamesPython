from random import randint

#Função que gera uma linha
def linha(x):
    print('-='*x)

x = randint(0, 100) #Gera um número interio aleatório de 0 a 100
tentativas = 0 #Conta quantas vezes o jogador precisou palpitar para acertar o número
numeros = [] #Armazena os números que já foram usados como dica pra que eles não apareçam de novo
chutes = [] #Armazena os números que o jogador já chutou
maiorqX = [] #Armazena os números que são maiores que X
menorqX = [] #Armazena os números que são menores que X

#Título
linha(10)
print('ACERTE O NÚMERO')
linha(10)

print('Pensei em um número X, tente adivinhar!')

while True:
    #Adiciona uma tentativa 
    tentativas += 1
    #Instruções:
    print(f'TENTATIVA {tentativas}')
    print(f'Palpites anteriores: {chutes}')
    print(f'X é Maior que {menorqX}')
    print(f'X é Menor que {maiorqX}')
    #Recebe o palpite do jogador: 
    valor = int(input(''))

    #Condição de vitória:
    if valor == x:
        print('ACERTOU!!')
        print(f'n° tentativas:{tentativas}')
        break
    else:
        #Adiciona o papite aos números que o jogador já tentou
        chutes.append(valor)
        #Pensa em um número para comparar e dar como dica
        n2 = randint(0, 100)
        if menorqX == [] and maiorqX == []:
            while True:
                if n2 in numeros or n2 == x:
                    n2 = randint(0, 100)
                else:
                    break
        elif menorqX != [] and maiorqX == []:
            while True:
                if n2 in numeros or n2 == x or n2 < max(menorqX):
                    n2 = randint(0, 100)
                else:
                    break
        elif menorqX == [] and maiorqX != []:
            while True:
                if n2 in numeros or n2 == x or n2 > min(maiorqX):
                    n2 = randint(0, 100)
                else:
                    break
        elif menorqX != [] and maiorqX != []:
            while True:
                if n2 in numeros or n2 == x or n2 < max(menorqX) or n2 > min(maiorqX):
                    n2 = randint(0, 100)
                else:
                    break
        # Adiciona o valor para os números que já foram chutados pelo jogador
        numeros.append(n2)

        #Dá a dica:
        if x < n2:
            linha(20)
            print('DICA:')
            print(f'X é menor que {n2}!')
            linha(20)
            maiorqX.append(n2)
        else:
            linha(20)
            print('DICA')
            print(f'X é maior que {n2}')
            linha(20)
            menorqX.append(n2)



            



