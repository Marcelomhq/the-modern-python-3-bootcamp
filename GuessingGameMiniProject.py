import random



# handle user guesses
#     if they guess correct, tell them they won
#         otherwise tell them if they are too low or too high

# Bonus: let the player tell if they want to player again

while True:
    random_num = random.randint(1,10)
#Loops literally forever to check if user typed a valid input
    while True:
        guess = input('Guess the number motherfuker: ')
        if guess.isdigit():
            guess = int(guess)
            print(f'You guessed {guess}.')
            break #break as soon as a valid number has been types
        else:
         print('INVALID INPUT, R U STUPID?? ')

#Code to check it its higher or lower or correct
    while guess != random_num:
        if guess < random_num:
            guess = input ('Number is higher. Guess the number again mf: ')
            guess = int(guess)
        elif guess > random_num:
            guess = input ('Number is lower. Guess the number again mf: ')
            guess = int(guess)
    print(f'U guess correctly, the random number was {random_num}')
    play_again = input ('Do you want to play again? (y/n)')
    if play_again == 'n':
        break

