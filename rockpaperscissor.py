import random

a = input("enter a choice : (rock, paper, scissor)")
b = ["rock", "paper", "scissor"]
c = random.choice(b)
if a == c:
    print("tie")
elif a == "rock" and c == "paper":
    print("computer wins")
elif a == "rock" and c == "scissor":
    print("you win")
elif a == "paper" and c == "rock":
    print("you win")
elif a == "'paper" and c == "scissor":
    print("computer wins")
elif a == "scissor" and c == "rock":
    print("computer wins")
elif a == "scissor" and c == "paper":
    print("you winrock")