import random
computer_choice = random.choice(["rock", "paper", "scissors"])

num = 0
while num <= 30:
    user_choice = input("What is your choice? ")
    if user_choice == computer_choice:
        print("Hey we got the same thing let's try again")
    elif user_choice == "rock" and computer_choice == "paper":
        print(f"Aww! You lost the game. I chose {computer_choice}")
    elif user_choice == "paper" and computer_choice == "scissors":
        print(f"Aww! You lost the game. I chose {computer_choice}")
    elif user_choice == "scissors" and computer_choice == "rock":
        print(f"Aww! You lost the game. I chose {computer_choice}")
    elif user_choice == "rock" and computer_choice == "scissors":
        print(f"Hey you won the game! I chose {computer_choice}")
        break
    elif user_choice == "paper" and computer_choice == "rock":
        print(f"Hey you won the game! I chose {computer_choice}")
        break
    elif user_choice == "scissors" and computer_choice == "paper":
        print(f"Hey you won the game! I chose {computer_choice}")
        break               
    else:
        print("Please enter a valid option!")    
        num = num + 1
        
    
















# random
# while
# input
# print and print-formatting
# comparison operators
# break and continue
