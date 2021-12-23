import cars
import main

class Rental:
    def __init__(self):
        self.adi_soyadi = None
        self.tc_no = None
        self.gun_sayisi = None
        
    def aracKirala(self,ID, kasa, araclar):
        self.adi_soyadi = input("Alıcının adı ve soyadını giriniz")
        self.tc_no = input("Alıcının TC Kimlik numarasını giriniz")
        self.gun_sayisi = int(input("Alıcının aracı kiralayacağı gün sayısını giriniz"))
        self.arac = None

        
        for index, arac in enumerate(araclar):
            if arac.ID == ID:
                kasa += arac.fiyat
                del araclar[index]

        
    def aracFiyatGuncelle(ID,araclar):
        alt_menu = int(input("Otomobil için 1 e, Minibüs için 2 ye basınız\n"))
        match alt_menu:
            case 1:
                if len(araclar) > 0:
                    for index,arac in enumerate(araclar):
                        if arac.arac_tipi == "Otomobil":
                            print(f"{arac.ID}, {arac.marka}, {arac.model}, {arac.yil}, {arac.renk}, {arac.fiyat}, {arac.arac_tipi}")
                        else:
                            print("Hiçbir veri bulunamadı")
                    
                    secim = input("Fiyatını güncellemek istediğiniz aracın numarasını giriniz")
                    oto = cars.Otomobil(secim)
                    araclar.insert(oto.otomobilEkle,int(secim)-1)

                else:
                    print("Hiçbir girdi bulunamadı.\n")

            case 2:
                if len(araclar) > 0:
                    for index,arac in enumerate(araclar):
                        if arac.arac_tipi == "Minibüs":
                            print(f"{arac.ID}, {arac.marka}, {arac.model}, {arac.yil}, {arac.renk}, {arac.fiyat}, {arac.arac_tipi}")
                        else:
                            print("Hiçbir veri bulunamadı")
                    
                    secim = input("Fiyatını güncellemek istediğiniz aracın numarasını giriniz")
                    oto = cars.Minibus(secim)
                    araclar.insert(oto.minibusEkle,int(secim)-1)
                else:
                    print("Hiçbir girdi bulunamadı.\n")
                
            case _:
                print("Hatalı giriş")    