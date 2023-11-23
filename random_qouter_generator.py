import random

# you can add more qoute list
quotes = ["The only way to do great work is to love what you do.", 
          "Success is not final, failure is not fatal: It is the courage to continue that counts.",
          "Believe you can and you're halfway there.",
          "The future belongs to those who believe in the beauty of their dreams.",
          "In the middle of every difficulty lies opportunity.",
          "The only limit to our realization of tomorrow will be our doubts of today."] 

while True:
    rand_quote = random.choice(quotes)
    print("\n\n\n****************Welcome to Quote Generator App****************")

    user = input('''Press (G) to generate a quote 
Press (Q) to exit 
                  ''').capitalize()

    if user == "G":
        print(rand_quote)
    elif user == "Q":
        print("Thanks for using our code\n")
        break
    else:
        print("Please choose only the given options.")
