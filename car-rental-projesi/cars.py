import rental
import main

class Tasit:
    def __init__(self,ID):
        self.ID=ID
        self.marka=None
        self.model=None
        self.yil=None
        self.renk=None
        self.fiyat=None

    def __str__(self):
        return f"{self.ID}"

class Otomobil(Tasit):
    def __init__(self, ID):
        super().__init__(ID)
        self.arac_tipi = "Otomobil"

    def otomobilEkle(self):
        self.marka=input("Aracın markasını giriniz. :")
        self.model=(input("Aracın modelini giriniz.:"))
        self.yil=int(input("Aracın model yılını giriniz. :"))
        self.renk=input("Aracın rengini giriniz. :")
        self.fiyat=int(input("Aracın fiyatını giriniz. :"))
        otomobil = (self.ID, self.marka, self.model, self.yil, self.renk, self.fiyat,self.arac_tipi)
        return self

    def __str__(self):
        return f"{self.arac_tipi}"

class Minibus(Tasit):
    def __init__(self, ID):
        super().__init__(ID)
        self.arac_tipi = "Minibüs"

    def minibusEkle(self):
        self.marka=input("Minibüsün markasını giriniz. :")
        self.model=(input("Minibüsün modelini giriniz. :"))
        self.yil=int(input("Minibüsün model yılını giriniz. :"))
        self.renk=input("Minibüsün rengini giriniz. :")
        self.fiyat=int(input("Minibüsün fiyatını giriniz. :"))
        minibus = (self.ID, self.marka, self.model, self.yil, self.renk, self.fiyat,self.arac_tipi)
        return self

    def __str__(self):
        return f"{self.arac_tipi}"