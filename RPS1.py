import random
print ('Rock \nPaper \nScissors')

#setting r p and s variable to make it easier to compare
r = 'ROCK' 
p = 'PAPER'
s = 'SCISSORS'

# get player 1 choice betweens RPS
p1 = input ('Player 1 select your choice: ')

#check if p1 typed something
if not p1:
    
    #check if p1 typed something incorrect

    while not p1:
        print ('yo, wait a minute you didnt type anything, try again: ')
        p1 = input ('Player 1 select your choice: ')
        p1 = p1.upper()
        print(p1)

    
else:
    p1 = p1.upper()
    while p1 != r and p1 != p and p1 != s or p1 == float:
        print ('yo, wait a minute you didnt type Rock, Paper or Scissors, try again: ')
        p1 = input ('Player 1 select your choice: ')
        p1 = p1.upper()
        print(p1)



#If p2 = a computer
comp_rand = random.randint(0,2)
# print(f'Computer plays {comp_rand}')
p2 = 0
print (comp_rand)

#0 = rock, 1 = paper, 2 = scissors
if comp_rand == 0:
    p2 = r
elif comp_rand == 1:
    p2 = p
else:
    p2 = s

print(f'Computer plays {p2}')

# get player 2 choice between RPS
# p2 = input ('Now its your turn Player 2, make your choice: ')
# if p2:
#     while p2 != r and p2 != p and p2 != s or p2 == float:
#         print ('yo, wait a minute you didnt type Rock, Paper or Scissors, try again: ')
#         p2 = input ('Player 2 select your choice: ')
# else:
#     print ('yo, wait a minute you didnt type anything, try again: ')
#     p2 = input ('Player 2 select your choice: ')

#ACTUAL GAME

#Checking if they are the same, regardless of the choice
if p1 == p2:
    print (f'Draw, {p1} doesnt do shit against {p2}')    

#if they arent the same the game begins
else:
    if p1 == r:
        if p2 == p:
            print ('Player 2 wins, Paper beats Rock')
        else:
            print ('Player 1 wins, Rock beats Scissors')
    elif p1 == p:
        if p2 == r:
            print ('Player 1 wins, Paper beats Rock')
        else:
            print('Player 2 wins, Scissors beats paper')
    #HERE P1 WILL ALWAYS BE SCISSORS
    else:
        if p2 == r:
            print ('Player 2 wins, Rock beats scissors')
        #Here Player 2 will always be paper, cuz p1 is scissor and if they were the same it would've been a draw before
        else:
            print ('Player 1 wins, Scissors beats paper')

    



