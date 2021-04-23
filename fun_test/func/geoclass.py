class BangunRuang():
    def info():
        pass



class PersegiPanjang(BangunRuang):
    def __init__(self, p, l):
        self.p = p
        self.l = l

    def info(self):
        return f'ini Object dari Persegi Panjang dengan panjang = {self.p} dan lebar = {self.l}'

    def luas(self):
        return self.p * self.l



class Segitiga(BangunRuang):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def info(self):
        return f'ini Object dari Segitiga dengan alas = {self.alas} dan tinggi = {self.tinggi}'

    def luas(self):
        return self.alas * self.tinggi / 2