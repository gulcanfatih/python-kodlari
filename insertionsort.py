def inserion_sort(dizi):
    for i in range(1, len(dizi)):
        key = dizi[i]
        j =i-1

        while j >= 0 and key<dizi[j]:
            dizi[j+1] = dizi[j]
            j =j-1

        dizi[j+1] = key

sirasiz_dizi = [3,10,-2,-1,15,400,17]
inserion_sort(sirasiz_dizi)
print(sirasiz_dizi)