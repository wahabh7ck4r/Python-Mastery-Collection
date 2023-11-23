import random
import word
print("\n************WELCOM TO THE HANGMAN GAME***********\n")

name = input("Plese Enter your name: ")
print(f"\nWelcome, {name}!! Try to guess the word correctly.")

word_list = word.word_list
rand_word = random.choice(word_list).upper()

def Hangman(wrong):
    if wrong == 0:
        print("     ------- ")
        print("           | ")
        print("           | ")
        print("           | ")
        print("     -------- ")
    elif wrong == 1:
        print("     ------- ")
        print("      O    | ")
        print("           | ")
        print("           | ")
        print("       ==== ")
    elif wrong == 2:
        print("     ------- ")
        print("      O    | ")
        print("      |    | ")
        print("           | ")
        print("     -------- ")
    elif wrong == 3:
        print("     ------- ")
        print("      O    | ")
        print("     /|\   | ")
        print("           | ")
        print("     -------- ")
    elif wrong == 4:
        print("     ------- ")
        print("      O    | ")
        print("     /|\   | ")
        print("      |    | ")
        print("     -------- ")
    elif wrong == 5:
        print("     ------- ")
        print("      O    | ")
        print("     /|\   | ")
        print("     / \   | ")
        print("     -------- ")
    elif wrong == 6:
        print("     ---|---- ")
        print("      O_|  | ")
        print("     /|\   | ")
        print("     / \   | ")
        print("     -------- ")


def play_game(word):
    wrong = 0
    total_chances = 7
    gusses_word = "-"*len(word)

    print(gusses_word)

    
    while total_chances!=0:
        print(gusses_word)
        latter = input("gussess a latter: ").upper()
        if latter in word:
            for index in range(len(word)):
                if(word[index]== latter):
                    gusses_word = gusses_word[:index]+latter+gusses_word[index+1:]
                    # print(gusses_word)
                    
            if gusses_word == word:
                print("Congratulation!! you won the game")
                break
                
        else:
            total_chances = total_chances-1
           
            Hangman(wrong)
            wrong += 1
            print("you Gusses it wornd the remaining chance are {}\n".format(total_chances))
            

        if total_chances == 0:          
            print("game over")
            print(f"The correct word is {rand_word}")




play_game(rand_word)

      



