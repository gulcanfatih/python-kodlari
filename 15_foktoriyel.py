"""
faktöriyel hesabı
5!=5*4*3*2*1=120   n!=n*(n-1)*(n-2)*...1
"""
def faktor(s):
    f=1
    for i in range(1,s+1):
        f *= i
    return (f)
sonuc = faktor(5)
print(sonuc)



