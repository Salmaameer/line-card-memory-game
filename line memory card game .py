#this is line memory card game
#created by  salma ameer
#the game is multipalyer game , each  player has to pick two numbers and if they match he
#will take point and if not the his score will be the same
# Note :to activate function  sleep go to run>>edit configuration >>emulate terminal in output console



import random           #to randomize the list of numbers
import os                #used for screen clear function
from time import sleep


list_char= ['B','D','A','C','D','H','F','I','F','G','A','B','E','J','I','C','E','G','J','H']

list_num= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# list to take the number from it  again if the player answer did not match
list2_num =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#this list for the end game statement
check_lst = ['*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*',]


random.shuffle(list_char)

player1_score=0
player2_score=0


def replacement():
    # this function for  the replacement process between the number chosen and the character

    global position1
    global position2
    global act1
    global act2

    position1 = list_char[act1 - 1]      #get the equivalent  index from the character list
    position2 = list_char[act2 - 1]

    list_num[act1 - 1] = position1       #replace the values from the two lists
    list_num[act2 - 1] = position2

    print("welcome,", list_num)






def player1_turn():  # function to each player to control the game

    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '20'] #this list for check if the number is in range or not

    global player1_score
    global act1
    global act2

    while list_num != check_lst: #the main condition if it false the game will end

        print()
        print(" player one, choose 2 numbers  :", list_num)
        print()
        act1, act2 = input("Enter here : ").split() #got the input from the first player

        # validation conditions

        if act1 not in nums or act2 not in nums :
            print("please enter in range 20")
            continue

        if act1 == act2:
            print("please enter two different numbers,")
            continue

        if list_num[int(act1) - 1] == '*' or list_num[int(act2) - 1] == '*':
            print("this number is taken ")
            continue


        act1 = int(act1)
        act2 = int(act2)
        replacement() #calling the function to make the process


# this condition for counting the score and replace the character with * or not
        if position1 == position2:
            player1_score += 1
            list_num[act1 - 1] = '*'
            list_num[act2 - 1] = '*'
            break
        else:
            player1_score = player1_score
            list_num[act1 - 1] = list2_num[act1 - 1]
            list_num[act2 - 1] = list2_num[act2 - 1]
            break


# sams as function player1_turn but for player 2
def player2_turn():
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '20']
    global player2_score
    global act1
    global act2

    while list_num != check_lst:
        print()
        print(" player two , choose 2 numbers  :", list_num)
        print()

        act1, act2 = input("Enter here : ").split()

        if act1 not in nums or act2 not in nums:
            print("please enter an integer,")
            continue



        if act1 == act2:
            print("please enter two different numbers,")
            continue

        if list_num[int(act1) - 1] == '*' or list_num[int(act2) - 1] == '*':
            print("this number is taken ")
            continue

        act1 = int(act1)
        act2 = int(act2)
        replacement()

        if position1 == position2:
            list_num[act1 - 1] = '*'
            list_num[act2 - 1] = '*'
            player2_score += 1
            break
        else:
            list_num[act1 - 1] = list2_num[act1 - 1]
            list_num[act2 - 1] = list2_num[act2 - 1]
            player2_score = player2_score
            break




def screen_clear(): # to clear the console
    if os.name == 'posix':
        _ = os.system('clear')


def who_won(): # the winner checker

    if list_num == check_lst:

        if player1_score > player2_score:
            print("    player one is the winner")
        if player2_score > player1_score:
            print("    player two is the winner")
        else:
            print("    DRAW, no one won!")




print("          ...welcome to line memory card game ...   \n          ...this game is multiplayer game... \n  ...each player has to pick two numbers from 1 to 20...      ")

#collecting all functions

while list_num != check_lst :


  player1_turn()

  sleep(5)    # sleep before the clear function
  screen_clear()
  player2_turn()
  print()
  print(" player one score :" , player1_score ,"\n player two score:",player2_score)
  sleep(5)
  screen_clear()

else:
    who_won()