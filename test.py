#Exercises for list compehension

#EX 1

# list1 = ["Elie", "Tim", "Matt"]
# answer = [first[0] for first in list1]
# print (answer)

# original_list = [1, 2, 3, 4, 5, 6]
# answer2 = [num + 0 for num in original_list if num % 2 == 0]
# # answer2 = [num*2 if num % 2 == 0 else num / 2 for num in original_list]
# print (answer2)

#EX 2

# list1 = [1,2,3,4]
# list2 = [3,4,5,6]
# answer = []
# for x in range(len(list1)):
#     print(x)
#     if (list1[x] in list2):
#         answer.append(list1[x])
    
# print(answer)

#    BETTER WAY FOR EX 2
# list1 = [1,2,3,4]
# list2 = [3,4,5,6]
# answer = [ x for x in list1 if x in list2]

# # for x in list1:
 
# #     if x in list2:
# #         answer.append(x)
       

# print (answer)

#EX 4

# answer = [[i for i in range(10)] for x in range (10)]

# for o in answer:
#     print (o)
#     print('-' * 20)  # Line after each row

# def display(first,second):
#     print(f'{first} and {second}')

# names = {'first' : 'colt', 'second' : 'steele'}
# display(**names)

'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''

# def calculate(make_float,operation,first,second,message=''):
#     result = 0
#     if operation == 'add':
#         if make_float == True:
#             result = float(first+second)
#         else:
#             result = int(first+second)
#     elif operation == 'subtract':
#         if make_float == True:
#             result = float(first-second)
#         else:
#             result = int(first-second)
#     elif operation == 'multiply':
#         if make_float == True:
#             result = float(first*second)
#         else:
#             result = int(first*second)
#     elif operation == 'divide':
#         if make_float == True:
#             result = first/second
#         else:
#             result = first//second
#     if message:
#         return f'{message} {result}'
#     return f'The result is {result}'

# print(calculate(True,'add',4,4, 'te fode'))

# def lowercaps(name):
#     # new_name = list(map(lambda x: x.lower(), name))
#     # full_name = ''
#     # for i in new_name:
#     #     full_name += str(i)
#     # return full_name
#     return ''.join([str(i) for i in name]).lower()


# print (lowercaps('TEFODE'))
# nums = [2,60,26,17]

# print(all([num % 2 == 0 for num in nums]))

# def sum_even_values(*nums):
#     return sum(num for num in nums if isinstance(num, (int, float)) and num % 2 == 0)

# def main():
#     user_input = input("Enter values separated by spaces: ")
#     # Split the input string into a list of strings
#     input_list = user_input.split()
    
#     # Convert the list of strings into a list of values
#     nums = []
#     for item in input_list:
#         try:
#             # Try to convert each item to a float first
#             num = float(item)
#             # If it is an integer, convert it to an int
#             if num.is_integer():
#                 num = int(num)
#             nums.append(num)
#         except ValueError:
#             # Ignore items that cannot be converted to float
#             pass
    
#     result = sum_even_values(*nums)
#     print(f"The sum of even values is: {result}")

# if __name__ == "__main__":
#     main()

# midterms = [80,91,78]
# finals = [98,89,53]
# students = ['dan', 'ang', 'kate']

# nova = list(zip(midterms,finals))
# print(nova)

# name 
# def extract_full_name(lst):
    
#     # newlst = []
#     # for i in lst:
#     #     newlst.append(lst(i).key('first') + ' '  + lst(i).value(i))
#     # return newlst
#     return [f"{l.get('first', '')} {l.get('last', '')}" for l in lst]    
# print (extract_full_name([{'first' : 'pedro'}]))

# def divide(num1,num2):
#     try:
#         return num1/num2
#     except ZeroDivisionError:
#         return ('Please do not divide by zero')
#     except TypeError:
#         return ('Please provide two integers or floats')
    
# print (divide(1,'1'))

cucumber = 100
num_people = 6
whole_cucumber_per_person = int(cucumber/num_people)
print(whole_cucumber_per_person)
float_cucumber_per_person = cucumber/num_people
print(f'{float_cucumber_per_person:.2f}')
print(cucumber/num_people)