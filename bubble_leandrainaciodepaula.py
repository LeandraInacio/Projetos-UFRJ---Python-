a=[]
tamanho=int(input('Qual o tamanho da lista que deseja testar? '))
a=[0]*tamanho
#print(a)
i=0
for tamanho in a:
    x=int(input('Digite um numero para adicionar à lista.'))
    a[i]=x
    i+=1
print('A lista a ser analizada é:\n',a)
p=0
contador=0
cp=0
for l in range(0,len(a)):
    for p in range(0,len(a)-1-l):#aqui quando se diminui l é pq temos a comparação, cada vez que roda, de menos um numero 
        anterior=a[p]
        posterior=a[p+1]
        if(anterior>posterior):
            aux=a[p]
            a[p]=a[p+1]
            a[p+1]=aux
            contador+=1
        cp+=1
    if(contador==0):
        print('_________________________________')
        print('A lista indicada já está ordenada')
        print('_________________________________')
        break
if(contador!= 0):
    print('A lista ordenada é: \n ',a)
    print('\nO número de trocas efetuadas é: \n ',contador)
print('quantidade de teste é:',cp)
