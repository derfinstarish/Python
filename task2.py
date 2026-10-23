# Rock paper scissors game by using if statements

Player_1 = input("Enter your choice (rock, paper, scissors): ")
Player_2 = input("Enter your choice (rock, paper, scissors): ")

if Player_1 == Player_2:
    print("It's a tie!")

elif Player_1 == "rock":
    if Player_2 == "scissors":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
        
elif Player_1 == "paper":
    if Player_2 == "rock":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
        
elif Player_1 == "scissors":
    if Player_2 == "paper":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")