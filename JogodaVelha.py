''' Jogo da Velha'''

'''Preenchimento do tabuleiro, montado em forma de dicionário'''
tabuleiroI = {'1': ' 1 ', '2': ' 2 ', '3': ' 3 ',
              '4': ' 4 ', '5': ' 5 ', '6': ' 6 ',
              '7': ' 7 ', '8': ' 8 ', '9': ' 9 '}

'''Separadores do tabuleiro'''
formatoCol = '|'
formatoLinha = '--+---+--'

'''Função para imprimir o tabuleiro no terminal do jogador'''


def imprimirTabuleiro(tabuleiroI):
    print(tabuleiroI['1']+formatoCol +
          tabuleiroI['2']+formatoCol+tabuleiroI['3'])
    print(formatoLinha)
    print(tabuleiroI['4']+formatoCol +
          tabuleiroI['5']+formatoCol+tabuleiroI['6'])
    print(formatoLinha)
    print(tabuleiroI['7']+formatoCol +
          tabuleiroI['8']+formatoCol+tabuleiroI['9'])


def jogo():
    global tabuleiroI

    peca = ' X '
    numJogadas = 0

    for i in range(10):
        imprimirTabuleiro(tabuleiroI)
        jogada = input('Jogador'+peca +
                       ', informe a posição que deseja marcar '+peca+': ')

        if tabuleiroI[jogada] != ' X ' and tabuleiroI[jogada] != ' O ':
            tabuleiroI[jogada] = peca
          #  jogador = '2'
            numJogadas += 1

        else:
            print('Jogada inválida, tente novamente.')
            continue

        if numJogadas >= 5:
            ''' X X X
                - - -
                - - -'''
            if tabuleiroI['1'] == tabuleiroI['2'] == tabuleiroI['3']:
                imprimirTabuleiro(tabuleiroI)
                print("\n>>> FIM DE JOGO <<<\n")
                print("\n * Jogador" + peca + " venceu! *\n")
                break

                """
                - - -
                X X X
                - - -
                """

            elif tabuleiroI['4'] == tabuleiroI['5'] == tabuleiroI['6']:
                imprimirTabuleiro(tabuleiroI)
                print("\n>>> FIM DE JOGO <<<\n")
                print("\n * Jogador" + peca + " venceu! *\n")
                break

                ''' - - -
                    - - -
                    X X X'''

            elif tabuleiroI['7'] == tabuleiroI['8'] == tabuleiroI['9']:
                imprimirTabuleiro(tabuleiroI)
                print("\n>>> FIM DE JOGO <<<\n")
                print("\n * Jogador" + peca + " venceu! *\n")
                break

                ''' X - -
                    X - -
                    X - - '''

            elif tabuleiroI['1'] == tabuleiroI['4'] == tabuleiroI['7']:
                imprimirTabuleiro(tabuleiroI)
                print("\n>>> FIM DE JOGO <<<\n")
                print("\n * Jogador" + peca + " venceu! *\n")
                break

                ''' - X -
                    - X -
                    - X - '''

            elif tabuleiroI['2'] == tabuleiroI['5'] == tabuleiroI['8']:
                imprimirTabuleiro(tabuleiroI)
                print("\n>>> FIM DE JOGO <<<\n")
                print("\n * Jogador" + peca + " venceu! *\n")
                break

                ''' - - X
                    - - X
                    - - X '''

            elif tabuleiroI['3'] == tabuleiroI['6'] == tabuleiroI['9']:
                imprimirTabuleiro(tabuleiroI)
                print("\n>>> FIM DE JOGO <<<\n")
                print("\n * Jogador" + peca + " venceu! *\n")
                break

                ''' X - -
                    - X -
                    - - X '''

            elif tabuleiroI['1'] == tabuleiroI['5'] == tabuleiroI['9']:
                imprimirTabuleiro(tabuleiroI)
                print("\n>>> FIM DE JOGO <<<\n")
                print("\n * Jogador" + peca + " venceu! *\n")
                break

            elif tabuleiroI['3'] == tabuleiroI['5'] == tabuleiroI['7']:
                imprimirTabuleiro(tabuleiroI)
                print("\n>>> FIM DE JOGO <<<\n")
                print("\n * Jogador" + peca + " venceu! *\n")
                break

        if numJogadas == 9:
            print("\n>>> FIM DE JOGO <<<\n")
            print("\nJogador1 e jogaor2 empataram!\n")

        if peca == ' X ':
            peca = ' O '
           # jogador = '2'
        else:
            peca = ' X '
            #jogador = '1'

    # Now we will ask if player wants to restart the game or not.
    reiniciar = input("Gostaria de jogar novamente?(s/n)")
    if reiniciar == "s" or reiniciar == "S":
        tabuleiroI = {'1': ' 1 ', '2': ' 2 ', '3': ' 3 ',
                      '4': ' 4 ', '5': ' 5 ', '6': ' 6 ',
                      '7': ' 7 ', '8': ' 8 ', '9': ' 9 '}
        jogo()


#if _name_ == "_main_":
jogo()