copy = input('Hey whats up? ')
while copy.upper() != 'STOP COPYING ME':
    print(copy)
    copy = input()
print ('okkk i will stop sajjjj')

#or a differente way

copy = input('Hey whats up? ')
while copy.upper() != 'STOP COPYING ME':
    copy = input(f'{copy} ')
print ('okkk i will stop sajjjj')