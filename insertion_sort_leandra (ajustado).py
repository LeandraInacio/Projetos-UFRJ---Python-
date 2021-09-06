print('-------------- ')
print('INSERTION SORT ')
print('-------------- ')
#lista=('O','R','D','E','N','A')             #linha original: isso é uma tupla. Tuplas não podem ser alteradas, lembra?
lista=['O','R','D','E','N','A']              #nova linha: isso é uma lista. Listas podem ser alteradas.
print('A lista a ser ordenada é :\n',lista)
i=0
j=0
for i in range(1,len(lista)):
    posicao_menor=i
    valor_menor=lista[i]
    for j in range(0,i):
        if(lista[j]>valor_menor):
            #valor_menor=lista[j]
            #auxiliar=valor_menor
            #del(lista[j])
            #lista.insert(i,auxiliar)
            #break

            auxiliar = lista[i]
            del(lista[i])
            lista.insert(j,auxiliar)
            break   
        
print(lista)


    
