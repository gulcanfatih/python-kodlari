# if kullanarak hesap makinesi yapma işlemi
print("---MENÜ---")
print("1-toplama")
print("2-çıkarma")
print("3-bölme")
print("4-çarpma")
print(10 * "-")

secim = int(input("seçiminizi giriniz :"))

if secim == 1:
    print("toplama")
    sayi1 = int(input("1.sayıyı giriniz :"))
    sayi2 = int(input("2.sayıyı giriniz :"))
    sonuc = sayi1 + sayi2
    print(f"{sayi1} + {sayi2} = {sonuc}")
elif secim == 2:
    print("çıkartma")
    sayi1 = int(input("1.sayıyı giriniz :"))
    sayi2 = int(input("2.sayıyı giriniz :"))
    sonuc = sayi1 - sayi2
    print(f"{sayi1} - {sayi2} = {sonuc}")
elif secim == 3:
    print("bölme")
    sayi1 = int(input("1.sayıyı giriniz :"))
    sayi2 = int(input("2.sayıyı giriniz :"))
    if sayi2 == 0:
        print("tanımsız")
        exit()
    sonuc = sayi1 // sayi2
    kalan = sayi1 % sayi2
    print(f"{sayi1} / {sayi2} = {sonuc}")
    print(f"kalan = {kalan}")

elif secim == 4:
    print("çarpma")
    sayi1 = int(input("1.sayıyı giriniz :"))
    sayi2 = int(input("2.sayıyı giriniz :"))
    sonuc = sayi1 * sayi2
    print(f"{sayi1} * {sayi2} = {sonuc}")
else:
    print("hatalı seçim yaptınız.")
