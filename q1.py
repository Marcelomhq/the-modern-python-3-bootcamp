
# var = input('escreva aqui')
VET = []
for i in range (10):
    x = input("digite um numero")
    VET.append(x)

posicoes =[]
#VET = [1,2,3,5,5,6,6,7,8]
for i in VET:
    #i = 8
    count = 0    
    for n in range (10):
        #n(0,1,2,3,4,5,6,7,8,9)
        if i == VET[n]:
            count += 1
            #count = 2
        if count >= 2:
            existe = True
            posicoes.append(n)            
            
print(posicoes)
print(existe)




    
