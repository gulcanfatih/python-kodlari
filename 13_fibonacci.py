"""
fibonacci dizisini bulan program
1,1,2,3,5,8,13,21....
"""

s1 = 1
s2 = 1
for i in range(50):
    temp = s1 + s2
    s1 = s2
    s2= temp
    print(s2, end=" ")