import random

def roll_dice(num_dice, num_sides):
    """Simulates rolling dice with given parameters."""
    print(f"Rolling {num_dice} dice with {num_sides} sides:")
    for i in range(num_dice):
        result = random.randint(1, num_sides)
        print(f"Die {i + 1}: {result}")
    print("All dice have been rolled.")

def main():
    print("Welcome to the Dice Roll Simulator!")

    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll: "))
            num_sides = int(input("Enter the number of sides for each die: "))

            if num_dice <= 0 or num_sides <= 0:
                print("Please enter positive values for the number of dice and sides.")
                continue

            roll_dice(num_dice, num_sides)

            choice = input("Do you want to roll again? (yes/no): ").lower()
            if choice != 'yes':
                print("Thank you for using the Dice Roll Simulator. Goodbye!")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
