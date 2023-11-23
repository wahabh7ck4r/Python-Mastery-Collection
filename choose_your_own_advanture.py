def start():
    print("\n********** CHOOSE YOUR OWN ADVENTURE **********\n")

    print("Welcome to the Amazon forest")
    print("You are standing behind the river")
    print("You have two paths to cross the river")
    print("1- Cross by boat (boat): ")
    print("2- Cross by bridge (bridge): ")

    while True:
        choice = input("> ").lower()
        if choice == "boat":
            boat()
            break
        elif choice == "bridge":
            bridge()
            break
        else:
            print("You must choose 'boat' or 'bridge'.")


def boat():
    print("You start crossing the river halfway when suddenly a crocodile appears.")
    print("You have two ways to deal with it.")
    print("1- Kill it with a Gun (Gun): ")
    print("2- Fight it with a Sword (Sword): ")

    while True:
        choice = input("> ").lower()

        if choice == "gun":
            print("You waste all the bullets in the gun.")
            print("The crocodile eats you.")
            game_over()
            break

        elif choice == "sword":
            print("You successfully kill the crocodile and ")
            print("successfully cross the river.")
            night()
            break

        else:
            print("Please choose one of the given options.")


def bridge():
    print("You successfully cross the river.")
    night()


def night():
    print("The sun sets...")
    print("Do you want to stay or go? (Stay/Go)")

    while True:
        choice = input("> ").lower()
        if choice == "stay":
            day()
            break
        elif choice == "go":
            print("You ventured into the dark. Lost and disoriented, ")
            print("you were eventually eaten by a lion.")
            game_over()
            break
        else:
            print("Please choose 'Stay' or 'Go'.")


def day():
    print("The Sun rises....")
    print("Now you have two ways")
    print("Go into the dark forest where dangerous animals lurk (forest):  ")
    print("Follow the river where sharks or crocodiles might be waiting (river): ")

    while True:
        choice = input("> ").lower()

        if choice == "forest":
            print("You face numerous challenges but eventually reach your destination.")
            win()
            break
        elif choice == "river":
            print("You fall into the river and get eaten by a Shark.")
            game_over()
            break
        else:
            print("Please choose one of the given options.")


def game_over():
    print("Game Over")
    print("Thanks for playing this game")

    while True:
        play_again = input("Do you want to play again? (Yes/No): ").lower()
        if play_again == "yes":
            start()
        elif play_again == "no":
            print("Okay! Have a nice day ahead")
            exit()
        else:
            print("Please answer 'Yes' or 'No'.")


def win():
    print("\n********** CONGRATULATIONS! YOU WON THE GAME **********\n")
    print("Thanks for playing this game")

    while True:
        play_again = input("Do you want to play again? (Yes/No): ").lower()
        if play_again == "yes":
            start()
        elif play_again == "no":
            print("Okay! Have a nice day ahead")
            exit()
        else:
            print("Please answer 'Yes' or 'No'.")


if __name__ == "__main__":
    start()
