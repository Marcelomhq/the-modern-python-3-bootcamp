from csv_funcs import rand_quote
from time import sleep
import os

def checking_author(guess,author):
    print(guess.title())
    if guess.title() == author:
        return True
    

def guessing_game(quote,author,bio_link):
    os.system('cls')
    print(f"Here is the quote:\n '{quote}'")
    sleep(1)
    guess = input("Who said the quote above? PS: you have to type all the spaces or special character in it's name.\n")
    
    if checking_author(guess,author):
        return f"YOU ARE CORRECT, the author is {guess.capitalize()}"
    
    sleep(1)
    print('Wrong answer, you can try 3 more times.')
    sleep(1)
    print('But now lets me give you a bit more info.')
    sleep(1)
    print(bio_link)
    print(author)
    guess = input("It's you turn again, who said that quote. \n")

    if checking_author(guess,author):
        return f"YOU ARE CORRECT, the author is {guess.capitalize()}"
    
    os.system('cls')
    print('Ok lets start over, you obviously suck at this.\n')
    sleep(1)
    print(f'Quote was: {quote}\nAnd the author info was: {bio_link}\n')
    sleep(1)
    print(f'And the first letter of its name is {author[0]}\n')
    sleep(1)
    guess = input("It's you turn again, who said that quote.\n")

    if checking_author(guess,author):
        return f"YOU ARE CORRECT, the author is {guess.capitalize()}"
    
    os.system('cls')
    print('Ok last try, you obviously suck at this.\n')
    sleep(1)
    print(f'Quote was: {quote}\nAnd the author info was: {bio_link}\n')
    sleep(1)
    print(f'And the first letter of its name is {author[0]}\n')
    sleep(1)
    print(f'And lastly his name has {len(author)} letters (including spaces)\n')
    sleep(1)
    guess = input("It's you turn again, who said that quote.\n")

    if checking_author(guess,author):
        os.system('cls')
        return f"YOU ARE CORRECT, the author is {guess.capitalize()}"
    
    return f"You suck at this, the author was {author}"
    
    

    
    

