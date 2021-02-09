"""-100 ile 100 arası tekrara etmeyen 10 sayıyı rastgele yazdırma"""
import random
dizi = []
for i in range(5):
    dizi.append(random.randrange(-100,100))
print(dizi)
