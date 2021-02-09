"""
dairenin alanını bulan programı yapıyoruz
"""
r=float(input("dairenin yarıçapını giriniz:"))
alan = 3.14 * r * r
print("alan = ", alan)
print("yarı çapı", r, "olan dairenin alanı", alan, "cm karedir.")
print("yarı çapı {} olan dairenin alanı {} cm karedir.".format(r,alan))
print(f"yarı çapı {r} olan dairenin alanı {alan} cm karedir.")