# for numb in range(1,21):
#     if numb == 4 or numb == 13:
#         print (f'{numb} is UNLUCKY! ')
#     else:
#         if numb % 2 == 0:
#             print(f'{numb} is odd! ')
#         else:
#             print(f'{numb} is odd! ')

#Making it better
for numb in range(1,21):
    if numb == 4 or numb == 13:
        state = 'Unlucky'
    else:
        if numb % 2 == 0:
            state = 'Even'
        else:
            state = 'Odd'
    print (f'{numb} is {state}! ')