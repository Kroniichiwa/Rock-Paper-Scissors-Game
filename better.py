import random

possibility = ["R","S","P"]
botChoice = random.choice(possibility)

def main() :
    while True :
        winning_choices = {"R": "S", "S": "P", "P": "R"}

        playerInput = input("Please type your choice : Rock = R , Paper = P , Scissors = S : ").upper()

        if playerInput not in winning_choices:
            print("Please only type R , P and S ")
        else:
            if botChoice == playerInput:
                print("It's a draw this time!")
            elif botChoice == winning_choices[playerInput]:
                print("Congratulation you win!")
            else:
                print(": ( unlucky, you just lose!)")
        play_again = input("Do you want to play again? (Y/N)").upper()
        if play_again == "N":
            break

if __name__ == '__main__':
    main()