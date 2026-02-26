import time
import random

def main():
    is_running = True
    while is_running:
        print("**********************************************************************************************")
        print("WELCOME TO THE NUMBER GUESSING GAME !")
        print("**********************************************************************************************")
        print("I'm thinking of a number between 0 and 100\n(Including both)\n ")
        num = random.randint(0,100)
        chances = 0
        print("Choose Game Difficulty: ")
        print("1 - Easy (10 chances)")
        print("2 - Medium (5 chances)")
        print("3 - Hard (2 chances)")
        difficulty = input("(Enter 1,2 or 3 according to your preffered difficulty): ")
        if difficulty == "1":
            chances = 10
        elif difficulty == "2":
            chances = 5
        elif difficulty == "3":
            chances = 2
        else:
            print("Invalid input. Try Again.")
            print()
            continue
        
        print()
        #Main Game
        guess_count = chances
        b = 0
        print("Lets start the game:")
        start_time = time.perf_counter()
        while chances > 0:
            print()
            try:
                guess = int(input("Guess the number: "))
            except ValueError:
                print("Please enter numbers only.")
                continue
            except KeyboardInterrupt:
                print("\nOh no, no. I decide when we are done.")
                continue
            if guess<0 or guess>100:
                print("Enter number between 0 and 100.")
                continue
            elif guess == num:
                print("You guessed the number !! Good Game !")
                print(f"You took {guess_count - chances + 1} guesses.")
                b = guess
                break
            elif guess > num:
                print(f"Wrong guess ! {guess} is greater than the chosen number.")
                chances -= 1
                print(f"Chances remaining = {chances}")
                b = guess
            elif guess < num:
                print(f"Wrong guess ! {guess} is lesser than the chosen number.")
                chances -= 1
                print(f"Chances remaining = {chances}")
                b = guess
        end_time = time.perf_counter()
        if b != num:
            print("\nGAME OVER ! You Lost")
        print(f"Total time taken = {(end_time - start_time):.2f} seconds")
        play_again = input("\nDo you want to play again ? (Y/any key): ")
        if play_again == "Y":
            print()
            print()
            continue
        else:
            print()
            print("Thank You for playing the game ! Bye !")
            is_running = False


if __name__ == '__main__':
    main()

