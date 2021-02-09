def selection_sort(dizi):
    for i in range(len(dizi)):
        min_index = i
        for j in range(i+1, len(dizi)):
            if dizi[min_index] > dizi[j]:
                min_index = j
        if min_index != i:
            dizi[min_index], dizi[i] = dizi[i], dizi[min_index]

sirasiz_dizi = [3,10,-2,-1,15,400,17]
selection_sort(sirasiz_dizi)
print(sirasiz_dizi)
