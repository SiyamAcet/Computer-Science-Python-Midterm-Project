baska_kutu = "e"
toplam_kutu = 0
bilyelerin_ayni_agirlikta_oldugu_kutu = 0
iade_edilen_kutu = 0
satin_alinan_kutu = 0
kabul_edilen_bilye_say = 0
iade_edilen_bilye_say = 0

bir_bilye_daha_agir_kutu = 0
bir_bilye_daha_hafif_kutu = 0

bir_bilye_daha_hafif_agirlik_farki = 0
bir_bilye_daha_agir_agirlik_farki = 0

bir_bilye_daha_hafif_agirlik_farki_yuzde = 0
bir_bilye_daha_agir_agirlik_farki_yuzde = 0

hatasiz_kutu_en_cok_bilye = 0
hatasiz_kutu_en_cok_bilye_agirlik = 0

hatasiz_kutu_en_agir_bilye_sayisi = 0
hatasiz_kutu_en_agir_bilye_agirlik = 0

agirlik_fark_en_buyuk = -1
agirlik_fark_en_buyuk_yuzde = 0

agirlik_fark_en_kucuk = -1
agirlik_fark_en_kucuk_yuzde = 0

agirlik_fark_en_kucuk_bilye_turu = ""
agirlik_fark_en_buyuk_bilye_turu = ""

while baska_kutu == "e" or baska_kutu == "E":

    bilye_sayisi = int(input("Kutudaki bilye sayıyını giriniz: "))

    while bilye_sayisi < 10:
        bilye_sayisi = int(input("Hatalı değer girdiniz, Kutudaki bilye sayısını giriniz: "))
    toplam_kutu += 1

    i = 0
    agirlik = 0
    onceki_agirlik1 = 0
    onceki_agirlik2 = 0
    onceki_agirlik3 = 0
    hatali_bilye_say = 0

    daha_hafif_bilye = 0
    daha_agir_bilye = 0

    daha_agir_bilye_fark = 0
    daha_hafif_bilye_fark = 0

    sondan_bir_onceki_agirlik = 0
    while i < bilye_sayisi and hatali_bilye_say < 2:
        agirlik = float(input("Sıradaki bilyenin mg cinsinden ağırlığını giriniz: "))

        while agirlik <= 0:
            agirlik = float(input("Yanlış ağırlık girdiniz, Sıradaki bilyenin mg cinsinden ağırlığını giriniz: "))
        if i == 0:  # ilk bilyenin ağırlığını değişkene atma
            onceki_agirlik1 = agirlik
        elif i == 1:  # 2. bilyenin ağırlığını değişkene atma
            onceki_agirlik2 = agirlik
            if onceki_agirlik2 != onceki_agirlik1:  # ilk bilye ikinci bilyeden farklı gelirse hatalı bilye say bir artar
                hatali_bilye_say += 1
        elif i == 2:  # 3. bilyenin ağırlığını bir değişkene atma
            onceki_agirlik3 = agirlik
            if onceki_agirlik3 != onceki_agirlik1 == onceki_agirlik2:  # 3. bilyenin ağırlığı diğer bilyelerden farklı gelirse hatalı bilye sayısı bir olur
                hatali_bilye_say = 1
            if onceki_agirlik1 != onceki_agirlik2 and onceki_agirlik1 != onceki_agirlik3 and onceki_agirlik2 != onceki_agirlik3:
                hatali_bilye_say = 3  # ilk gelen 3 ağırlık değeri de farklı gelirse hatalı bilye sayısı 3 olur

            if onceki_agirlik1 < onceki_agirlik2 == onceki_agirlik3:  # ilk bilye diğerlerinde daha hafif gelirse ilk bilyeyi daha hafif bilye yapar
                daha_hafif_bilye = onceki_agirlik1
            elif onceki_agirlik1 > onceki_agirlik2 == onceki_agirlik3:  # ilk bilye daha ağır gelirse ilk bilyeyi daha ağır yapar
                daha_agir_bilye = onceki_agirlik1
            if onceki_agirlik2 < onceki_agirlik1 == onceki_agirlik3:  # ikinci bilye daha hafif gelirse ikinci bilyeyi daha hafif bilye yapar
                daha_hafif_bilye = onceki_agirlik2
            elif onceki_agirlik2 > onceki_agirlik1 == onceki_agirlik3:  # ikinci bilye daha ağır gelirse ikinci bilyeyi daha ağır bilye yapar
                daha_agir_bilye = onceki_agirlik2
            if onceki_agirlik3 < onceki_agirlik1 == onceki_agirlik2:  # üçüncü bilye daha hafif gelirse üçüncü bilyeyi daha hafif bilye yapar
                daha_hafif_bilye = onceki_agirlik3
            elif onceki_agirlik3 > onceki_agirlik1 == onceki_agirlik2:  # üçüncü bilye daha ağır gelirse üçüncü bilyeyi daha ağır bilye yapar
                daha_agir_bilye = onceki_agirlik3

        elif i > 2:
            if agirlik == onceki_agirlik1 and agirlik != onceki_agirlik2 and agirlik != onceki_agirlik3:  # 4. gelen ağırlık değeri 1. bilyeye aşit ama diğerlerinde eşit değilse hatalı bilye sayısı 2 olur
                hatali_bilye_say = 2
            elif agirlik == onceki_agirlik2 and agirlik != onceki_agirlik1 and agirlik != onceki_agirlik3:  # 4. gelen ağırlık değeri 2. bilyeye aşit ama diğerlerinde eşit değilse hatalı bilye sayısı 2 olur
                hatali_bilye_say = 2
            elif agirlik == onceki_agirlik3 and agirlik != onceki_agirlik1 and agirlik != onceki_agirlik2:  # 4. gelen ağırlık değeri 3. bilyeye aşit ama diğerlerinde eşit değilse hatalı bilye sayısı 2 olur
                hatali_bilye_say = 2
            elif agirlik != onceki_agirlik1 == onceki_agirlik2 == onceki_agirlik3:  # sonradan gelen ağırlıklar 2 defa ilk üç ağırlığa eşit olmazsa hatalı bilye sayısı 2 olur
                hatali_bilye_say += 1
                if agirlik < onceki_agirlik1 and hatali_bilye_say != 2:  # sonradan gelen ağırlık değeri ilk ağırlıklardan farklı ise daha hafif ya da daha ağır bilye için atama yapılır
                    daha_hafif_bilye = agirlik
                elif agirlik > onceki_agirlik1:
                    daha_agir_bilye = agirlik
            elif agirlik != onceki_agirlik1 and agirlik != onceki_agirlik2 and agirlik != onceki_agirlik3:  # sonradan ağırlık hepsinden farklıysa hatalı bilye sayısı 2 olur
                hatali_bilye_say = 2
        if i == bilye_sayisi - 2 and hatali_bilye_say != 2:  # sondan bi onceki bir bilyeyi tutmaya yarayan kod bloğu
            sondan_bir_onceki_agirlik = agirlik

        if hatali_bilye_say >= 2:  # hatalı bilye sayısı 1 den büyük olursa iade edilen kutu sayısı 1 artar
            iade_edilen_kutu += 1
            iade_edilen_bilye_say += bilye_sayisi  # iade edilen kutu sayısına bilye sayısı eklenir
            print("Şuanki kutuda birden fazla hatalı bilye var.. Kutu iade ediliyor...")

        if i == bilye_sayisi - 1 and hatali_bilye_say != 2:  # kutu iade edilmezse girilicek kod bloğu
            kabul_edilen_bilye_say += bilye_sayisi  # satın alınan bilye sayısına ekler
            satin_alinan_kutu += 1  # satın alınan kutuyu bir arttırır
            if daha_hafif_bilye != 0:  # içince hafif bilye bulunan kutu sayısına bir ekler
                bir_bilye_daha_hafif_kutu += 1
            if daha_agir_bilye != 0:  # içinde ağır bilye bulunan kutu sayısına bir ekler
                bir_bilye_daha_agir_kutu += 1
            if daha_agir_bilye == 0 and daha_hafif_bilye == 0:  # hiç farklı bilye yoksa bilyelerin aynı olduğu kutu sayısını 1 arttırır
                bilyelerin_ayni_agirlikta_oldugu_kutu += 1
                print("Kutudaki tüm bilyeler eşit ağırlıkta...")
                if bilye_sayisi > hatasiz_kutu_en_cok_bilye:  # bilye sayısı aynı olan kutulardan en çok bilyeye sahip kutuyu günceller
                    hatasiz_kutu_en_cok_bilye = bilye_sayisi
                    hatasiz_kutu_en_cok_bilye_agirlik = agirlik
                if agirlik > hatasiz_kutu_en_agir_bilye_agirlik:  # ağırlığı en fazla olan aynı ağırlıktaki bilyelerin olduğu kutunun içindeki ağırlığı günceller
                    hatasiz_kutu_en_agir_bilye_agirlik = agirlik
                    hatasiz_kutu_en_agir_bilye_sayisi = bilye_sayisi

            if daha_hafif_bilye != 0 and daha_hafif_bilye != agirlik:  # daha hafif bilyenin diğer bilyeler ile arasındaki farkı alır
                daha_hafif_bilye_fark = agirlik - daha_hafif_bilye
                daha_hafif_bilye_fark_yuzde = daha_hafif_bilye_fark * 100 / agirlik
                bir_bilye_daha_hafif_agirlik_farki += daha_hafif_bilye_fark
                bir_bilye_daha_hafif_agirlik_farki_yuzde += daha_hafif_bilye_fark_yuzde
                print("Bir bilye diğerlerinden daha hafif...")
                print("Ağırlık farkının değeri: {:.2f}".format(daha_hafif_bilye_fark))
                print("Ağırlık farkının yüzdesi: %{:.2f}".format(daha_hafif_bilye_fark_yuzde))
            elif daha_hafif_bilye != 0 and daha_hafif_bilye == agirlik:
                daha_hafif_bilye_fark = sondan_bir_onceki_agirlik - daha_hafif_bilye
                daha_hafif_bilye_fark_yuzde = daha_hafif_bilye_fark * 100 / sondan_bir_onceki_agirlik
                bir_bilye_daha_hafif_agirlik_farki += daha_hafif_bilye_fark
                bir_bilye_daha_hafif_agirlik_farki_yuzde += daha_hafif_bilye_fark_yuzde
                print("Bir bilye diğerlerinden daha hafif...")
                print("Ağırlık farkının değeri: {:.2f}".format(daha_hafif_bilye_fark))
                print("Ağırlık farkının yüzdesi: %{:.2f}".format(daha_hafif_bilye_fark_yuzde))
            if daha_agir_bilye != 0 and daha_agir_bilye != agirlik:  # daha ağır bilyenin diğer bilyelerden farkını alır
                daha_agir_bilye_fark = daha_agir_bilye - agirlik
                daha_agir_bilye_fark_yuzde = daha_agir_bilye_fark * 100 / agirlik
                bir_bilye_daha_agir_agirlik_farki += daha_agir_bilye_fark
                bir_bilye_daha_agir_agirlik_farki_yuzde += daha_agir_bilye_fark_yuzde
                print("Bir bilye diğerlerinden daha ağır...")
                print("Ağırlık farkının değeri: {:.2f}".format(daha_agir_bilye_fark))
                print("Ağırlık farkının yüzdesi: %{:.2f}".format(daha_agir_bilye_fark_yuzde))
            elif daha_agir_bilye != 0 and daha_agir_bilye == agirlik:
                daha_agir_bilye_fark = daha_agir_bilye - sondan_bir_onceki_agirlik
                daha_agir_bilye_fark_yuzde = daha_agir_bilye_fark * 100 / sondan_bir_onceki_agirlik
                bir_bilye_daha_agir_agirlik_farki += daha_agir_bilye_fark
                bir_bilye_daha_agir_agirlik_farki_yuzde += daha_agir_bilye_fark_yuzde
                print("Bir bilye diğerlerinden daha ağır...")
                print("Ağırlık farkının değeri: {:.2f}".format(daha_agir_bilye_fark))
                print("Ağırlık farkının yüzdesi: %{:.2f}".format(daha_agir_bilye_fark_yuzde))

            if daha_hafif_bilye_fark > daha_agir_bilye_fark:  # agırlık fark değerinin en büyük olduğu bilyeyi bulma
                if daha_hafif_bilye_fark > agirlik_fark_en_buyuk:
                    agirlik_fark_en_buyuk = daha_hafif_bilye_fark
                    agirlik_fark_en_buyuk_yuzde = agirlik_fark_en_buyuk * 100 / agirlik
                    agirlik_fark_en_buyuk_bilye_turu = "Hafif"
            elif daha_agir_bilye_fark > daha_hafif_bilye_fark:
                if daha_agir_bilye_fark > agirlik_fark_en_buyuk:
                    agirlik_fark_en_buyuk = daha_agir_bilye_fark
                    agirlik_fark_en_buyuk_yuzde = agirlik_fark_en_buyuk * 100 / agirlik
                    agirlik_fark_en_buyuk_bilye_turu = "Ağır"

            if agirlik_fark_en_kucuk == -1:  # ağırlık fark değerinin en küçük olduğu bilyeyi bulma
                if daha_hafif_bilye_fark > daha_agir_bilye_fark:
                    agirlik_fark_en_kucuk = daha_hafif_bilye_fark
                    agirlik_fark_en_kucuk_yuzde = agirlik_fark_en_kucuk * 100 / agirlik
                    agirlik_fark_en_kucuk_bilye_turu = "Hafif"
                elif daha_agir_bilye_fark > daha_hafif_bilye_fark:
                    agirlik_fark_en_kucuk = daha_agir_bilye_fark
                    agirlik_fark_en_kucuk_yuzde = agirlik_fark_en_kucuk * 100 / agirlik
                    agirlik_fark_en_kucuk_bilye_turu = "Ağır"

            else:
                if daha_hafif_bilye_fark > daha_agir_bilye_fark:
                    if agirlik_fark_en_kucuk > daha_hafif_bilye_fark:
                        agirlik_fark_en_kucuk = daha_hafif_bilye_fark
                        agirlik_fark_en_kucuk_yuzde = agirlik_fark_en_kucuk * 100 / agirlik
                        agirlik_fark_en_kucuk_bilye_turu = "Hafif"

                elif daha_agir_bilye_fark > daha_hafif_bilye_fark:
                    if agirlik_fark_en_kucuk > daha_agir_bilye_fark:
                        agirlik_fark_en_kucuk = daha_agir_bilye_fark
                        agirlik_fark_en_kucuk_yuzde = agirlik_fark_en_kucuk * 100 / agirlik
                        agirlik_fark_en_kucuk_bilye_turu = "Ağır"

        i += 1

    baska_kutu = input("Baska kutu var mı ? (E, e, H, h)")

    # Verilen biçime uygun olmayan veri girişi sağlanırsa hata kontrolu
    while baska_kutu != "e" and baska_kutu != "E" and baska_kutu != "h" and baska_kutu != "H":
        baska_kutu = input("Hatalı veri girdiniz, baska kutu var mı? (E, e, H, h)")

    if baska_kutu == "h" or baska_kutu == "H":
        print("Programdan çıkılıyor...")
print()

# hesaplamalar

uretim_hatasi_kutu_yuzde = iade_edilen_kutu * 100 / toplam_kutu
tum_bilyeler_esit_agirlik_yuzde = bilyelerin_ayni_agirlikta_oldugu_kutu * 100 / satin_alinan_kutu
bir_bilye_daha_agir_kutu_yuzde = bir_bilye_daha_agir_kutu * 100 / satin_alinan_kutu
bir_bilye_daha_hafif_kutu_yuzde = bir_bilye_daha_hafif_kutu * 100 / satin_alinan_kutu

bir_bilye_daha_agir_agirlik_farki_ort = bir_bilye_daha_agir_agirlik_farki / bir_bilye_daha_agir_kutu
bir_bilye_daha_agir_agirlik_farki_yuzde_ort = bir_bilye_daha_agir_agirlik_farki_yuzde / bir_bilye_daha_agir_kutu

bir_bilye_daha_hafif_agirlik_farki_ort = bir_bilye_daha_hafif_agirlik_farki / bir_bilye_daha_hafif_kutu
bir_bilye_daha_hafif_kutu_yuzde_ort = bir_bilye_daha_hafif_agirlik_farki_yuzde / bir_bilye_daha_hafif_kutu

print("Üretim hatası olan kutu sayısı: ", iade_edilen_kutu)
print("Üretim hatası olan kutuların tüm kutular içindeki yüzdesi: {:.2f}".format(uretim_hatasi_kutu_yuzde))
print("İade edilen bilye sayısı: ", iade_edilen_bilye_say)
print("Kabul edilen bilye sayısı: ", kabul_edilen_bilye_say)
print()
print("Tüm bilyelerin eşit ağırlıkta olduğu kutu sayısı: ", bilyelerin_ayni_agirlikta_oldugu_kutu)
print("Bir bilyenin diğerinden daha ağır olduğu kutu sayısı: ", bir_bilye_daha_agir_kutu)
print("Bir bilyenin diğerinden daha hafif olduğu kutu sayısı: ", bir_bilye_daha_hafif_kutu)
print()
print("Tüm bilyelerin eşit ağırlıkta olduğu kutu sayısının satın alınan kutular içindeki yüzdesi: %{:.2f}".format(
    tum_bilyeler_esit_agirlik_yuzde))
print("Bir bilyenin diğerinden daha ağır olduğu kutu sayısının satın alınan kutular içindeki yüzdesi: %{:.2f}".format(
    bir_bilye_daha_agir_kutu_yuzde))
print("Bir bilyenin diğerinden daha hafif olduğu kutu sayısının satın alınan kutular içindeki yüzdesi: %{:.2f}".format(
    bir_bilye_daha_hafif_kutu_yuzde))
print()
print(
    "Bir bilyenin diğerlerinden daha ağır olduğu kutulardaki ağır olan bilyelerin ağırlık farkı değerlerinin ortalaması: {:.2f}".format(
        bir_bilye_daha_agir_agirlik_farki_ort))
print(
    "Bir bilyenin diğerlerinden daha ağır olduğu kutulardaki ağır olan bilyelerin ağırlık farkı yüzdelerinin ortalaması: %{:.2f}".format(
        bir_bilye_daha_agir_agirlik_farki_yuzde_ort))
print(
    "Bir bilyenin diğerlerinden daha hafif olduğu kutulardaki hafif olan bilyelerin ağırlık farkı değerlerinin ortalaması: {:.2f}".format(
        bir_bilye_daha_hafif_agirlik_farki_ort))
print(
    "Bir bilyenin diğerlerinden daha hafif olduğu kutulardaki hafif olan bilyelerin ağırlık farkı yüzdelerinin ortalaması: %{:.2f}".format(
        bir_bilye_daha_hafif_kutu_yuzde_ort))
print()
print("Tüm bilyelerin eşit ağırlıkta olduğu kutular arasında, içinde en çok sayıda bilye olan kutudaki bilye sayısı: ",
      hatasiz_kutu_en_cok_bilye)
print(
    "Tüm bilyelerin eşit ağırlıkta olduğu kutular arasında, içinde en çok sayıda bilye olan kutudaki bir bilyenin ağırlığı: {:.2f}".format(
        hatasiz_kutu_en_cok_bilye_agirlik))
print("Tüm bilyelerin eşit ağırlıkta olduğu kutular arasında, içinde en ağır bilyeler olan kutudaki bilye sayısı: ",
      hatasiz_kutu_en_agir_bilye_sayisi)
print(
    "Tüm bilyelerin eşit ağırlıkta olduğu kutular arasında, içinde en ağır bilyeler olan kutudaki bir bilyenin ağırlığı: ",
    hatasiz_kutu_en_agir_bilye_agirlik)
print()
print(
    "Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın değerinin en büyük olduğu ağırlık farkının değeri: {:.2f}".format(
        agirlik_fark_en_buyuk))
print(
    "Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın değerinin en büyük olduğu ağırlık farkının yüzdesi: %{:.2f}".format(
        agirlik_fark_en_buyuk_yuzde))
print(
    "Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın değerinin en büyük olduğu ağırlık farkının işareti: ",
    agirlik_fark_en_buyuk_bilye_turu)
print(
    "Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın yüzdesinin en küçük olduğu ağırlık farkının değeri: {:.2f}".format(
        agirlik_fark_en_kucuk))
print(
    "Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın yüzdesinin en küçük olduğu ağırlık farkının yüzdesi: %{:.2f}".format(
        agirlik_fark_en_kucuk_yuzde))
print(
    "Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın yüzdesinin en küçük olduğu ağırlık farkının işareti: ",
    agirlik_fark_en_kucuk_bilye_turu)