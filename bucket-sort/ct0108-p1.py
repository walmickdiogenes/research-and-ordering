#Walmick Diógenes Nogueira de Queirós

#Gerar series de 10000 a 50000 números e plotar gráficos com o melhor, médio e pior caso.

from random import randint
import matplotlib as mpl
import timeit

tamlista = [10000, 20000, 30000, 40000, 50000]
def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def insertionSort(alist):
   for i in range(1,len(alist)):
       current = alist[i]
       while i>0 and alist[i-1]>current:
            alist[i] = alist[i-1]
            i = i-1
            alist[i] = current

def bucketSort(alist):
    largest = max(alist)
    length = len(alist)
    size = largest / length

    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i] / size)
        if j != length:
            buckets[j].append(alist[i])
        else:
            buckets[length - 1].append(alist[i])

    for i in range(length):
        insertionSort(buckets[i])

    result = []
    for i in range(length):
        result = result + buckets[i]

    return result

mpl.use('Agg')
import matplotlib.pyplot as plt
def desenhaGrafico(x,y,ym,yp,xl = "Tamanho", yl = "Tempo"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo")
    ax.plot(x,ym, label = "Medio Tempo")
    ax.plot(x,yp, label = "Pior Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('bucket.png')

melhorTempo = []
piorTempo = []
medioTempo = []

for i in tamlista:
  medio = geraLista(i)
  melhor = sorted(medio)
  pior = sorted(medio, reverse=True)

  melhorTempo.append(timeit.timeit("bucketSort({})".format(melhor),setup="from __main__ import bucketSort",number=1))
  piorTempo.append(timeit.timeit("bucketSort({})".format(pior),setup="from __main__ import bucketSort",number=1))
  medioTempo.append(timeit.timeit("bucketSort({})".format(medio),setup="from __main__ import bucketSort",number=1))

desenhaGrafico(tamlista,melhorTempo, piorTempo, medioTempo)