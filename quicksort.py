def QuickSort(X,Inivet, Fimvet):
    i=Inivet
    j=Fimvet
    pivo= X[(Inivet + Fimvet)//2]
    while (i<j):
        while(X[i]<pivo):
            i=i+1
        while(X[j]>pivo):
            j=j-1
        if(i<=j):
            aux=X[i]
            X[i]=X[j]
            X[j]=aux
            i=i+1
            j=j-1
    if(j>Inivet):
        QuickSort(X,Inivet,j)
    if(i<Fimvet):
        QuickSort(X,i,Fimvet)
tamanho=10
Lista=range(10,0)
QuickSort(Lista,10,0)
print(Lista)
