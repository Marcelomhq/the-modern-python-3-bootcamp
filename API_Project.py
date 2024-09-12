from pyfiglet import figlet_format
from termcolor import colored
import requests
from random import choice

print(colored(figlet_format('Dad Joke 3000'),'magenta'))

top_jokes = input('Let me tell you an amazing joke. Choose a topic first: ')

url = 'https://icanhazdadjoke.com/search'
res = requests.get(
    url,
    headers={'Accept' : 'application/json'},
    params={'term': top_jokes}
).json()

quant_jokes = res['total_jokes']

all_jokes = res['results']
# print (all_jokes)

if quant_jokes > 1:
    print(f"I've got {quant_jokes} jokes about '{top_jokes}'. Here's one: ")
    print(choice(all_jokes)['joke'])
elif quant_jokes == 1:
    print(f"I've got one joke about '{top_jokes}'. Here's one: ")
    print(all_jokes['joke'])
else:
    print("Sorry, I don't have a joke about that topic.")

          