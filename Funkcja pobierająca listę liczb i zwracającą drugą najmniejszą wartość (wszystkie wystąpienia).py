lista=[1, 67, 2, 4, 5, 5, 77, 2, 3, 6, 8, 3]
def znajdowanie():
    lista.sort()
    listano=list(set(lista))
    listano.sort()
    l=0
    for i in range(0,len(lista)):
        if listano[1]==lista[i]:
            l+=1
    for x in range(1,l+1):
        print(listano[1])
znajdowanie()