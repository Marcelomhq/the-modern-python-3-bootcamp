from pyfiglet import figlet_format
from termcolor import colored

text = input ("Which phrase do you want? ")
color = input ('Which color do you want? ')
# phase and coloor all set
#Next step transform text into pyfiglet and then add color if it match to something we can.

# colors = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
# if color in colors:
#     new_text = pyfiglet.figlet_format((termcolor.colored(text,color)))
# else:
#     new_text = pyfiglet.figlet_format((termcolor.colored(text,'magenta')))
# # text = pyfiglet.figlet_format(text, font="slant")
# new_text = pyfiglet.figlet_format(text)
def print_colors(text,color):
    colors = ('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')    
    if color not in colors:
        color = 'magenta'

    print(colored(figlet_format(text),color))

print_colors(text,color)
