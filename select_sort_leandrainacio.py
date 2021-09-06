print('_______________')
print('SELECTION SORT ')
print('_______________\n')
lista=["O","R","D","E","N","A"]
print("A lista a ser ordenada é: \n", lista)
i=0
j=0
posição_inicial=0
tam_lista=len(lista)
for j in range(tam_lista):
    posicao_menor=j
    menor=lista[j]
    for i in range (j,tam_lista):
        if(menor>=lista[i]):
            menor=lista[i]
            posicao_menor=i
    if(lista[j]>=menor):
        aux=lista[j]
        lista[j]=menor
        lista[posicao_menor]=aux
    print('elemento analizado = ',lista[j],'\n','Com a iteração ',j+1,'ten-se a lista: ',lista)
