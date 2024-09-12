#using For

# for x in range (9):
#     print ('\U0001f600' * x)

#Pyramid

space = 6
tiles = 1
print ('     *')
for tiles in range (7):
    print (' '*space+('*'*tiles)*2)
    space -= 1
