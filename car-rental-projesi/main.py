import rental
import cars

araclar = []
kasa = 0
id = 1

def save():
    global araclar
    with open("arackiralama.txt", "w", encoding="utf-8")as f:
        for arac in araclar:
            temp = f"{arac.ID}, {arac.marka}, {arac.model}, {arac.yil}, {arac.renk}, {arac.fiyat}, {arac.arac_tipi}\n"
            f.write(temp)
            print(temp)

def load():
    global araclar
    global id
    with open("arackiralama.txt", "r") as f:
        fContent = f.read().split('\n')[:-1]

        for line in fContent:
            line = line.split(", ")
            temp = None
            if line[6] == "Otomobil":
                temp=cars.Otomobil(line[0])
            elif line[6] == "Minibüs":
                temp = cars.Minibus(line[0])
            else:
                print("Hatalı giriş.")
            temp.marka=line[1]
            temp.model=line[2]
            temp.yil=line[3]
            temp.renk=line[4]
            temp.fiyat=line[5]
            temp.arac_tipi=line[6]
            araclar.append(temp)
    
    if len(araclar)>0:
        id = int(araclar[-1].ID)

def listele():
    if len(araclar) > 0:
        for arac in araclar:
            print(f"{arac.ID}, {arac.marka}, {arac.model}, {arac.yil}, {arac.renk}, {arac.fiyat}, {arac.arac_tipi}")
    else:
        print("Hiçbir girdi bulunamadı.\n")

while True:
    print("AKN Rent a Car Hoşgeldiniz")
    girdi = int(input("""
    Menüden seçenek belirtiniz:
    Programdan çıkmak için 0'a basınız.
    Otomobil ekle 1,
    Minibüs ekle 2,
    Araçları Listele 3,
    Araç fiyatını güncelle 4,
    Aracı kiraya ver 5,
    Verileri yükle 6,
    Yapılanları kaydet 7,
    Kasayı gör 8
    """))
    match girdi:
        case 0:
            print("Prgramdan çıkış başarılı.")
            break
        case 1:
            id += 1
            araba = cars.Otomobil(id)
            araclar.append(araba.otomobilEkle())
            
        case 2:
            id += 1
            minibus = cars.Minibus(id)
            araclar.append(minibus.minibusEkle())

        case 3:
            listele()
            
        case 4:
            guncelle = rental.Rental()
            guncelle.aracFiyatGuncelle(araclar)

        case 5:
            listele()
            secim = input("Listeden bir araç seçiniz\n")
            kirala = rental.Rental()
            kirala.aracKirala(secim,kasa,araclar)
        case 6:
            load()

        case 7:
            if input("Eminseniz 'e' ye basınız. :").lower() == "e":
                save()
                print("Değişiklikler başarıyla kaydedilmiştir.")
            else:
                print("KAYDEDİLMEDİ!!!")
            
        case 8:
            print(f"Kasa :{kasa}")
        case _:
            print("Hatalı Giriş")

