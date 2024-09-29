from csv import writer, reader, DictReader
from random import choice

csv_file1 = "all_quotes.csv"
def dict_quotes(all_quotes):
    with open(csv_file1,"w", newline='', encoding='utf-8') as file:
        csv_writer = writer(file)
        csv_writer.writerow(["Quote", "Author", "Bio Link"])
        for quote in all_quotes:
            csv_writer.writerow([quote['quote'],quote['author'],quote['bio-link']])

def rand_quote():
    with open(csv_file1, encoding='utf-8') as file:
        csv_reader = DictReader(file)      
        csv_reader_list = list(csv_reader) 
        random_quote = choice(csv_reader_list) 
        # print(random_quote)
        # print(csv_reader_list.index(random_quote))
    return random_quote
        
