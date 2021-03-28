import random
computer_score = 0
user_score = 0
items1 = ("Rock", "Paper", "Scissor")
items2 = ("Rock", "Paper", "Scissor", "Exit")

while True:
    computer_choice = random.choice(items1)

    print("0-Rock")
    print("1-Paper")
    print("2-Scissor")
    print("3-Exit")

    user_choice_index = int(input())
    user_choice = items2[user_choice_index]

    print(computer_choice)

    if computer_choice == "Rock" and user_choice == "Scissor":
        print("Computer wins")
        computer_score += 1
    elif computer_choice == "Rock" and user_choice == "Paper":
        print("User wins")
        user_score += 1
    elif computer_choice == "Rock" and user_choice == "Rock":
        print("Tie!")

    elif computer_choice == "Scissor" and user_choice == "Paper":
        print("Computer wins")
        computer_score += 1
    elif computer_choice == "Scissor" and user_choice == "Rock":
        print("User wins")
        user_score += 1
    elif computer_choice == "Scissor" and user_choice == "Scissor":
        print("Tie!")

    elif computer_choice == "Paper" and user_choice == "Rock":
        print("Computer wins")
        computer_score += 1
    elif computer_choice == "Paper" and user_choice == "Scissor":
        print("User wins")
        user_score += 1
    elif computer_choice == "Paper" and user_choice == "Paper":
        print("Tie!")
    else:
        print("user_score:", user_score)
        print("computer_score:", computer_score)
        break
