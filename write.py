# def copy(text1,text2):
#     with open(text1, 'r+') as file:  
#         file.write('agora eh isso e foda-se ')
#         file.seek(0)
#         new_text = file.read()
#         # print(file.read())
#     with open(text2, 'r+') as file2:
#         file2.write(new_text)
    
#         file2.seek(0)
#         print(file2.read())
        
# copy('text.txt', 'text2.txt')

# def copy_and_reverse(text1, text2):
#     with open(text1, 'r') as file:
#         new_text = file.read()
    
#     with open(text2, 'w') as file2:
#         file2.write(new_text[::-1])
    
# copy_and_reverse("text.txt", "text2.txt")

'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''

# def statistics(text):
#     with open(text, "r") as file:
#         lines = file.readlines()

#         return{"lines": len(lines),
#                "words": sum(len(line.split(" ")) for line in lines),
#                "Characters": sum(len(lines) for line in lines)
#                }

# print(statistics("text.txt"))

'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''

def find_and_replace(text, word1, word2):
    #Find Marcelo and replace it for Belo
    with open(text, 'r+') as file:
        text = file.read()
        new_text = text.replace(word1, word2)
        file.seek(0)
        file.write(new_text)
        file.truncate(1235)
        

find_and_replace("text.txt", 'Xdd', 'Belo')

def truncate_example():
    with open('text2.txt', 'r+') as file: 
        content = file.read()  # Read the file content
        print(f"Original content:\n{content}")
        
        file.seek(5)  # Move the file pointer to position 5
        file.truncate()  # Truncate the file from position 5 onward

        # Now, the file only contains the first 5 characters
        file.seek(0)  # Go back to the start of the file
        truncated_content = file.read()  # Read the truncated content
        print(f"Truncated content:\n{truncated_content}")

truncate_example()
    



