import random

choices = ["rock" , "paper" , "scissors"]
computer = random.choice(choices)

player = None

while player not in choices:
    player = input("rock , paper or scissors : ").lower()


print("computer : ",computer)
print("Player : " , player)

if computer == player:
    print("Its a tie")
elif player == "rock" :
    if computer == "scissors" :
        print("Rock smashes scissors . You win!")
    else :
        print("paper covers rock, You lose :(")
elif player== "paper":
    if computer == "rock":
        print("Paper covers rock.You win!")
    else :
        print("Scissors cut paper.You lose :(")
elif player == "scissors" :
    if computer == "rock":
        print("Rock smashes scissors.You lose :(")
    else :
        print("Scissors cuts paper.You win!")


