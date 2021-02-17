import random

player = input('Enter a choice(Rock,Paper,Scissors,Lizard,Spock):')
t = ['Rock','Paper','Scissors','Lizard','Spock']
computer = random.choice(t)
#player = False #no move by player
#while player==False :
    #player = input("Rock, Paper, Scissors?")
if player == computer:
    print("Tie!")

elif player == "Rock":
    if computer == "Paper":
        print("You lose!", computer, "covers", player)
    elif computer =="Spock":
        print("You lose!",computer,"vaporise",player)
    elif computer == "Lizard":
        print("You win!", player, "smashes", computer)
    else :
        print("You win!",player,"crushes",computer)

elif player == "Paper":
    if computer == "Scissors":
        print("You lose!", computer, "cut", player)
    elif computer == "Lizard":
        print("You lose!", computer,"eats",player)
    elif computer == "Rock":
        print("You win!", player, "covers", computer)
    else :
        print("You win!",player,"disproves",computer)

elif player == "Scissors":
    if computer == "Rock":
        print("You lose...", computer, "smashes", player)
    elif computer == "Spock":
        print("You lose",computer,"smashes",player)
    elif computer == "Paper":
        print("You win!", player, "cut", computer)
    else :
        print("You win!",player,"decapitate",computer)

elif player == "Lizard":
    if computer == "Scissors":
        print("You lose!", computer,"decapitate",player)
    elif computer == "Rock":
        print("You lose!",computer,"crushes",player)
    elif computer == "Paper":
        print("You win!",player,"eats",computer)
    else :
        print("You win!",player,"poisons",computer)

elif player == "Spock":
    if computer == "Lizard":
        print("You lose!",computer,"poisons",player)
    elif computer == "Paper":
        print("You lose!",computer,"disproves",player)
    elif computer == "Scissors":
        print("You win!",player,"smashes",computer)
    else :
        print("You win!",player,"vaporise",computer)
else:
    print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    #player = False
    #computer = t[randint(0,2)]
