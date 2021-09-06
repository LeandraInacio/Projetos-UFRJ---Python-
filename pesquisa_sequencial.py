print("-------------------- ")
print(" PESQUISA SEQUENCIAL ")
print("-------------------- ")
import time
t1=time.time()
lista=range(10000000)
#print(lista)
for i in lista :
    if(i==9888000):
        posicao=i+1
print(" a posicao da chave procurada e: ",posicao)
t2=time.time()
tempo=t2-t1
print(tempo)
