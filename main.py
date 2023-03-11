import random

possibility = ["R","S","P"]
botChoice = random.choice(possibility)

def main() :
    print("Welcome to the Rock-Paper-Scissors Game")

    #S > P , P > R , R > S

    playerInput = input("Please type your choice : Rock = R , Paper = P , Scissors = S : ")

    try:
        playerInput = playerInput.upper()
        #print("Bot choosed : " + botChoice)
        #check rock
        if playerInput == "R" :
            if botChoice == "S" :
                print("Congratulation you win!")
            elif botChoice == "P" :
                print(":( unlucky, you just lose!)")
            else :
                print("It a draw this time!")
        #check paper
        elif playerInput == "P" :
            if botChoice == "R" :
                print("Congratulation you win!")
            elif botChoice == "S" :
                print(":( unlucky, you just lose!)")
            else :
                print("It a draw this time!")
        #check scissors
        elif playerInput == "S" :
            if botChoice == "P" :
                print("Congratulation you win!")
            elif botChoice == "R" :
                print(":( unlucky, you just lose!)")
            else :
                print("It a draw this time!")
        else :
            print("Please only type R , P and S ")

    except:
        print("Please try again!")

 
if __name__ == '__main__':
    main()