board = {'1' : '','2' : '','3' : '','4' : '','5' : '','6' : '','7' : '','8' : '','9' : ''}
import random, os, check, time
p1= input("enter your name player 1 (symbol X):\n")
p2 = input("enter your name player 2 (symbol O):\n")
score1, score2, score_tie = [], [], []
total_moves =0
player = random.randint(1, 2)
time.sleep(2, 6)
os.system("cls")
if player == 1:
    print(f" {p1} won the toss.")
else:
    print("let us begin")
time.sleep(2)
def toggaleplayer(player):
    if player == 1:
        player = 2
    elif player == 2:
        player = 1
def playagain():
    inp = input("do you want to okay again??(Y/N)\n")
    if inp.upper() == "Y":
        a = toggaleplayer(player)
        restart(a)
    elif inp.upper() == "N":
        os.system("cls")
        print("thanks of playing")
        prin(f"Number of times {p1} won : {len(score1)}.")
        prin(f"Number of times {p2} won : {len(score2)}.")
        prin(f"Number of ties : {len(score_tie)}.")
        abc = input()
        quit()
    else:
        print("invalid input")
        quit()
def restart(a):
    total_moves, board =0 , {'1' : '','2' : '','3' : '','4' : '','5' : '','6' : '','7' : '','8' : '','9' : ''}
    while True:
        os.system("cls")
        print(board['1'] + '|' + board['2'] + '|'  + board['3'] )
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|'  + board['6'] )
        print('-+-+-')
        print(board['7'] + '|' + board['8'] + '|'  + board['9'] )
        print('-+-+-')
        check.check(total_moves,score1, score2, score_tie, playagain, board, p1, p2)
        while True:
            if a == 1:
                p1_input = input(f"its {p1}'s chance..\n where do you want to place your move:")
                if p1_input.upper()  in board and board[p1_input.upper()] == "" + board[p1_input.upper()] = 'X'
                a = 2
                break
            else:
                print("invaild inpt \n enter again. ")
                continue
        else:
            p2_input = input(f"its {p2}'s chance..\n where do you want to place your move:")
            if p2_input.upper()  in board and board[p2_input.upper()] == "": + board[p2_input.upper()] = 'O'
            a = 1
            break
    else:
            print("invaild input")
            continue
    total_moves += 1
    while True:
        os.system(cls)
        print(board['1'] + '|' + board['2'] + '|'  + board['3'] )
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|'  + board['6'] )
        print('-+-+-')
        print(board['71'] + '|' + board['8'] + '|'  + board['9'] )
        print('-+-+-')
        check.check(total_moves,score1, score2, score_tie, playagain, board, p1, p2)
        while True:
            if a == 1:
                p1_input = input(f"its {p1}'s chance..\n where do you want to place your move:")
                if p1_input.upper()  in board and board[p1_input.upper()] == "": + board[p1_input.upper()] = 'X'
                a = 2
                break
            else:
                print("invaild inpt \n enter again. ")
                continue
        else:
            p2_input = input(f"its {p2}'s chance..\n where do you want to place your move:")
            if p2_input.upper()  in board and board[p2_input.upper()] == "": + board[p2_input.upper()] = 'O'
            a = 1
            break
    else:
            print("invaild input")
            continue
    total_moves += 1