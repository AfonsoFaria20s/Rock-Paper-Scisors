from tabulate import tabulate

def welcome(name):
    print("-+"*20)
    print("Welcome {} to Rock Paper Scisors.".format(name))
    print("This is you vs computer, whoever reaches 3 wins first, wins the round")
    print("\nYou have some options to choose from before\nany game starts including:")
    options()
    print("=#"*25)
    
def options():
    print("-+"*20)
    print("1 - Play")
    print("2 - Change name")
    print("3 - Change the number of rounds per game")
    print("4 - Close")
    print("-+"*20)
    
def getCurrentScore(computer, player, rounds, name, c_total, p_total):
    
    print("")
    print(tabulate([[name,"{} / {}".format(player, p_total)],["Computer","{} / {}".format(computer, c_total)]],headers=["Rounds: {}".format(rounds),"Score / Total"], tablefmt='orgtbl'))
    print("")