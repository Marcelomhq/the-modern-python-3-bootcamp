from scraper_funcs import scraper_func, bio_link_scraper
from csv_funcs import rand_quote
from game_funcs import guessing_game
from time import sleep
import os


if __name__ == '__main__':
    print("Welcome to my amazing game, lets start it (this is definetely not useless xdd)!!!!")
    while True:    
        menu1 = int(input("You options are: \n1 - Start the quote guessing game\n2 - Do you want to scrap the website?\n"))
        sleep(1)
        match menu1:
            case 2:
                scraper_func()
                print("Scrapping done succesfully, select option 1 next time to play.")
            case 1:
                print(
                    "Quote Guessing game. \nRules: We will provide you with a quote and you will have a total of 4 guesses to find out who said.\nWith each incorrect answer we'll provide with with a little bit more info about this person. GOOD LUCK!!!\n"
                )
                input()
                random_quote = rand_quote()     
                quote = random_quote['Quote']        
                author = random_quote['Author']
                bio_link = bio_link_scraper(random_quote['Bio Link'])
                print(guessing_game(quote,author,bio_link))
                print("Thank you for playing")
                menu2 = int(input('Do you want to play again? (1 for yes/ 2 for no)\n'))
                match menu2:
                    case 2: 
                        os.system('cls')
                        print("Bye bye, ty for playing")
                        break
            case _:
                print("Bro wtf did u type, its incorrect, try again using one of the 2 option provided to you LMAO.")
        
        


    

    




