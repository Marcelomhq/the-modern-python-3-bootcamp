file = open("text.txt")
print(file.read())
file.seek(0)
print(file.readline())
print(file.read())