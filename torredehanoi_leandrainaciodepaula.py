# -*- coding: cp1252 -*-
import os
print ("----------------")
print (" TORRE DE HANÓI ")
print ("----------------")
a=[]
b=[]
c=[]
blocos = int(input ("PRIMEIRAMENTE NOS DIGA, COM QUANOS BLOCOS VOCÊ QUER JOGAR? "))
for val in range(1,blocos+1):
    a.append(val)
b=[0]*blocos
c=[0]*blocos
a.sort(reverse=True)
print ('A ordenação dos bocos são ' , a, ' considerando que a base começa à esquerda e você so poderá movimentar o topo de cada lista.')
x=1#x recebe 1 para poder entrar no while
contador=0
while x!=0:
    x=int(input("Digite a opção que deseja executar:\n 1) modificar a pilha a;\n 2) modificar a pilha b;\n 3) modificar a pilha c;\n 4) digite zero para sair;\n>"))
    if (x==1):#MODIFICAR PILHA A -----------------------------
        destino=(input("Para qual pilha o bloco será enviado?\n b) para a pilha B;\n c) para a pilha C;\n>"))
        if (destino=='b'):
            posicaoa=0
            posicaob=0
            i=0
            for item in a:
                if(a[i]==0):
                    posicaoa=i-1
                    break
                if(i==(blocos-1)):
                    posicaoa=i
                i+=1
            i=0
            for item in b:
                if(b[i]==0):
                    posicaob=i
                    break
                i+=1
            if(posicaob==0):
                b[posicaob]=a[posicaoa]
                a[posicaoa]=0
            else:
                if(b[posicaob-1] < a[posicaoa]):
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print(" não é possivel fazer essa jogada ")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                else:
                    b[posicaob]=a[posicaoa]
                    a[posicaoa]=0
        else:
            posicaoa=0
            posicaoc=0
            i=0
            for item in a:
                if(a[i]==0):
                    posicaoa=i-1
                    break
                if(i==(blocos-1)):
                    posicaoa=i
                i+=1
            i=0
            for item in c:
                if(c[i]==0):
                    posicaoc=i
                    break
                i+=1
            if(posicaoc==0):
                c[posicaoc]=a[posicaoa]
                a[posicaoa]=0
            else:
                if(c[posicaoc-1] < a[posicaoa]):
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print(" não é possivel fazer essa jogada ")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                else:
                    c[posicaoc]=a[posicaoa]
                    a[posicaoa]=0
    elif (x==2):#MODIFICAR PILHA B -----------------------------
        destino=(input("Para qual pilha o bloco será enviado?\n a) para a pilha A;\n c) para a pilha C;\n>"))
        if (destino=='a'):
            posicaoa=0
            posicaoc=0
            i=0
            for item in b:
                if(b[i]==0):
                    posicaob=i-1
                    break
                if(i==(blocos-1)):
                    posicaob=i
                i+=1
            i=0
            for item in a: #ver la em cima depois
                if(a[i]==0):
                    posicaoa=i
                    break
                i+=1
            if(posicaoa==0):
                a[posicaoa]=b[posicaob]
                b[posicaob]=0
            else:
                if(a[posicaoa-1] < b[posicaob]):
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print(" não é possivel fazer essa jogada ")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                else:
                    a[posicaoa]=b[posicaob]
                    b[posicaob]=0
        else:
            posicaob=0
            posicaoc=0
            i=0
            for item in b:
                if(b[i]==0):
                    posicaob=i-1
                    break
                if(i==(blocos-1)):
                    posicaob=i
                i+=1
            i=0
            for item in c:
                if(c[i]==0):
                    posicaoc=i
                    break
                i+=1
            if(posicaoc==0):
                c[posicaoc]=b[posicaob]
                b[posicaob]=0
            else:
                if(c[posicaoc-1] < b[posicaob]):
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print(" não é possivel fazer essa jogada ")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                else:
                    c[posicaoc]=b[posicaob]
                    b[posicaob]=0
    elif (x==3):#MODIFICAR PILHA C -----------------------------
        destino=(input("Para qual pilha o bloco será enviado?\n a) para a pilha A;\n b) para a pilha B;\n>"))
        if (destino=='b'):
            posicaoc=0
            posicaob=0
            i=0
            for item in c:
                if(c[i]==0):
                    posicaoc=i-1
                    break
                if(i==(blocos-1)):
                    posicaoc=i
                i+=1
            i=0
            for item in b:
                if(b[i]==0):
                    posicaob=i
                    break
                i+=1
            if(posicaob==0):
                b[posicaob]=c[posicaoc]
                c[posicaoc]=0
            else:
                if(b[posicaob-1] < c[posicaoc]):
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print(" não é possivel fazer essa jogada ")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                else:
                    b[posicaob]=c[posicaoc]
                    c[posicaoc]=0
        else:
            posicaoa=0
            posicaoc=0
            i=0
            for item in c:
                if(c[i]==0):
                    posicaoc=i-1
                    break
                if(i==(blocos-1)):
                    posicaoc=i
                i+=1
            i=0
            for item in a:
                if(a[i]==0):
                    posicaoa=i
                    break
                i+=1
            if(posicaoa==0):
                a[posicaoa]=c[posicaoc]
                c[posicaoc]=0
            else:
                if(a[posicaoa-1] < c[posicaoc]):
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print(" não é possivel fazer essa jogada ")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                else:
                    a[posicaoa]=c[posicaoc]
                    c[posicaoc]=0
    contador+=1
    os.system('cls')
    print("\n-----------------------------")
    print("Você já fez ", contador," movimentos.")
    print("-----------------------------\n")
    print(a)
    print(b)
    print(c)
    print("\n")
minimo=(2**blocos)-1
print("você fez ",contador, "movimentos. O numero minimo de movimentos é ",minimo,)
