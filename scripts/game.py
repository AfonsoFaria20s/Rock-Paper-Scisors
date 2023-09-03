import utils as util
import sys,time,random

gameStarted = False
name = ""
rounds = 1
max_wins = 3

c_wins = 0
c_totalWins = 0

p_wins = 0
p_totalWins = 0

options = ["r", "p", "s"] # Rock, Paper, Scisors

def init():
    global name
    global gameStarted
    while(True):
        if(gameStarted==False):
            try:
                name = str(input("Choose a name: "))
                gameStarted = True
            except ValueError:
                print("Enter a valid name.")
            
            util.welcome(name)
        
        start()
        
def start():
    util.options()
    option = int(input("Option: "))
    
    match option:
        case 1:
            play()
        case 2:
            changeName()
        case 3:
            changeRoundsPerGame()
        case 4:
            print("Closing program.")
            time.sleep(0.5)
            sys.exit()

def play():
    global rounds
    global c_wins
    global p_wins
    
    while(True):
        player_turn = playerTurn()
        computer_turn = computerTurn()
        
        winner = checkWinner(player_turn, computer_turn)
               
        match winner:
            case 0:
                print("-"*20)
                computerWins()
                util.getCurrentScore(c_wins, p_wins, rounds,name, c_totalWins, p_totalWins)
                print("-"*20)
            case 1: 
                print("-"*20)
                playerWins()
                util.getCurrentScore(c_wins, p_wins, rounds,name, c_totalWins, p_totalWins)
                print("-"*20)
            case 2:
                print("-"*20)
                tie()
                util.getCurrentScore(c_wins, p_wins, rounds,name, c_totalWins, p_totalWins)
        rounds+=1
        
        
def checkWinner(player_turn, computer_turn):
    if((player_turn=="r" and computer_turn=="r") or (player_turn=="p" and computer_turn=="p") or (player_turn=="s" and computer_turn=="s")):return 2 #Tie
    elif((player_turn=="p" and computer_turn=="r") or (player_turn=="r" and computer_turn=="s") or (player_turn=="s" and computer_turn=="p")):return 1 #Player
    elif((player_turn=="r" and computer_turn=="p") or (player_turn=="s" and computer_turn=="r") or (player_turn=="p" and computer_turn=="s")):return 0 #Computer
        
def playerWins():
    global p_wins
    global p_totalWins
    
    if(p_wins==max_wins-1):
        p_totalWins+=1
        p_wins+=1
        print("Game is over.\n{} wins the game.".format(name))
        util.getCurrentScore(c_wins, p_wins, rounds,name, c_totalWins, p_totalWins)
        reset()
        init()
    p_wins+=1
    print("{} wins!!".format(name))
    
    
def computerWins():
    global c_wins
    global c_totalWins
    
    if(c_wins==max_wins-1):
        c_wins+=1
        c_totalWins+=1
        print("Game is over.\nComputer wins the game.")
        util.getCurrentScore(c_wins, p_wins, rounds,name, c_totalWins, p_totalWins)
        reset()
        init()
    c_wins+=1
    print("Computer wins!!")   

def tie():
    print("Tie, no points for both players.")

def playerTurn():
    option = str(input("Your turn: "))
    
    # while((option!="r") or (option!="p") or (option!="s")):
    #     print("Invalid value. Try again!")
    #     option = str(input("Your turn: "))

    return option

def computerTurn():
    option = random.choice(options)
    print("Computer Turn: {}".format(option))
    
    return option

def changeName():
    global name
    try:
        new_name = str(input("New name: "))
        name = new_name
    except ValueError:
        print("Not a valid name")
    except Exception as e:
        print("Unexpected error: \n",e)

def changeRoundsPerGame():
    global max_wins
    new_count = int(input("Number of rounds per game: "))
    max_wins = new_count    

def reset():
    global c_wins
    global p_wins
    global rounds
    
    c_wins = 0
    p_wins = 0
    rounds = 0