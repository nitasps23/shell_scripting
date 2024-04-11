# rock, paper, scissors game

def play_rps():

    import random

    options = ("rock", "paper", "scissors")
    playing = True

    while playing:

        player = None
        computer = random.choice(options)

        while player not in options:
            player = input("Enter your options > rock, paper, or scissors: ").lower()

        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("It's a tie!")
        elif player == "rock" and computer == "scissors":
            print("You win!")
        elif player == "paper" and computer == "rock":
            print("You win!")
        elif player == "scissors" and computer == "paper":
            print("You win!")
        else:
            print("You lose!")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if not play_again == "y":
            playing = False

    print("Thanks for playing!")

play_rps()