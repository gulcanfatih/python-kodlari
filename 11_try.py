sayi1 = 50
sayi2 = 10

try:
    sonuc= sayi1 / sayi2
    print(sonuc)
except ZeroDivisionError:
    print("Sıfıra bölünemez :(")
except:
    print("olmuyor")
finally:
    print("herşeye rağmen calışır")