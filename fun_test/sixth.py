from fun_test.func.geoclass import PersegiPanjang, Segitiga

print('Menggunakan OOP')
p1 = PersegiPanjang(10,3)
s1 = Segitiga(10,3)

print(p1.info())
print(p1.luas())

print(s1.info())
print(s1.luas())

#Polymorphism
list_bangun_ruang = []
list_bangun_ruang.append(p1)
list_bangun_ruang.append(s1)

print('\nPolymorhism')
for bangun_ruang in list_bangun_ruang:
    print(bangun_ruang.info())
    print(bangun_ruang.luas())