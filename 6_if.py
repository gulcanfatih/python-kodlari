print("---MENÜ---")
print("1-Dairenin Alanı")
print("2-Dikdörtgenin Alanı")
print("---------------")

secim = int(input("Seçiminizi Giriniz :"))

if secim == 1:
    print("dairenin alanı")
    r = float(input("Yarı çapı giriniz :"))
    print("Dairenin alanı {}".format(3.14 * pow(r, 2)))
elif secim == 2:
    print("dikdörtgenin alanı")
    a = float(input("birinci kenarı giriniz :"))
    b = float(input("ikinci kenarı giriniz :"))
    alan = a * b
    print(f"Dikdörtgenin Alanı :{alan}")
    print("Dikdörtgenin Alanı : {}".format(alan))
else:
    print("yanlış seçim")
