from random import randint

theBoard = { '1': '1' , '2': '2' , '3': '3' ,
             '4': '4' , '5': '5' , '6': '6' ,
             '7': '7' , '8': '8' , '9': '9' ,}
            
boardKeys = []

for key in theBoard:
    boardKeys.append(key)

    def print_board_def(board):
        print(" Tabuleiro:\n")
        print('', board['1'] , '|' , board['2'] , '|' , board['3'])
        print("---|---|---")
        print('', board['4'] , '|' , board['5'] , '|' , board['6'])
        print("---|---|---")       
        print('', board['7'] , '|' , board['8'] , '|' , board['9'])

    def game_board_def():  
        turn = 'X'
        count = 0

        firstPlayer = randint(1, 2)
        if firstPlayer == 1:
            turn = 'X'
        elif firstPlayer == 2:
            turn = 'O'   

        for i in range(10):
            print_board_def(theBoard)
            print("É sua vez, " + turn + ". Aonde deseja jogar?")

            move = input()
        
            if theBoard[move] == move:
                theBoard[move] = turn
                count += 1
            else:
                print("Este campo já esta preenchido!.\nAonde deseja jogar?")
                continue

            if count >= 5:
                if theBoard['1'] == theBoard['2'] == theBoard['3'] != move:
                    print_board_def(theBoard)
                    print("\nGAME OVER!!.\n")                
                    print("O jogador " +turn + " venceu.")                
                    break
                elif theBoard['4'] == theBoard['5'] == theBoard['6'] != move: 
                    print_board_def(theBoard)
                    print("\nGAME OVER!!.\n")           
                    print("O jogador " +turn + " venceu.")
                    break
                elif theBoard['7'] == theBoard['8'] == theBoard['9'] != move:  
                    print_board_def(theBoard)
                    print("\nGAME OVER!!.\n")                
                    print("O jogador " +turn + " venceu.")
                    break
                elif theBoard['1'] == theBoard['5'] == theBoard['9'] != move:  
                    print_board_def(theBoard)
                    print("\nGAME OVER!!.\n")              
                    print("O jogador " +turn + " venceu.")
                    break
                elif theBoard['3'] == theBoard['5'] == theBoard['7'] != move: 
                    print_board_def(theBoard)
                    print("\nGAME OVER!!.\n")               
                    print("O jogador " +turn + " venceu.")
                    break
                elif theBoard['1'] == theBoard['4'] == theBoard['7'] != move: 
                    print_board_def(theBoard)
                    print("\nGAME OVER!!.\n")               
                    print("O jogador " +turn + " venceu.")
                    break 
                elif theBoard['2'] == theBoard['5'] == theBoard['8'] != move: 
                    print_board_def(theBoard)
                    print("\nGAME OVER!!.\n")                
                    print("O jogador " +turn + " venceu.")
                    break
                elif theBoard['3'] == theBoard['6'] == theBoard['9'] != move: 
                    print_board_def(theBoard)
                    print("\nGAME OVER!!.\n")              
                    print("O jogador " +turn + " venceu.")
                    break 
                    
            if count == 9:
                print("\nPartida FINALIZADA!!.\n")                
                print("O jogo EMPATOU!")
                break
                    
            if turn =='X':
                turn = 'O'
            else:
                turn = 'X'   
            
game_board_def()