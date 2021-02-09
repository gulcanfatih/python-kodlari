"""1-100 arası 10 adet sayıyı rastgele atadıktan sonra döngü
 kullanarak sıralayan fonksiyonu yazınız.
-buble sort
 """
import random


def buble_sort(dizi):
    for d in range(len(dizi) - 1, 0, -1):
        for e in range(d):
            if dizi[e] > dizi[e + 1]:
                dizi[e], dizi[e + 1] = dizi[e + 1], dizi[e]
    return dizi


sayilar = []
for i in range(11):
    sayilar.append(random.randrange(1, 101))

print("sıralanmadan önce")
print(sayilar)
print("sıralanınca")
print(buble_sort(sayilar))
