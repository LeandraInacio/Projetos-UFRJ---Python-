print('---------------- ')
print('PESQUISA BINARIA ')
print('---------------- ')
import time
t1=time.time()
lista=range(100)
print(lista)
inicio=0
fim=len(lista)-1
print(fim)
while (inicio<=fim) :
    meio=((inicio+fim)//2)
    if(lista[meio]==89):
        print('a posicao da chave é:\n',meio)
        break
    else:
        if(lista[meio]<89):
            inicio=meio+1
        else:
            fim=meio-1
   
t2=time.time()
tempo=t2-t1
print(tempo)
