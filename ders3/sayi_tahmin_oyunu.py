tuttugumsayi=3
sayi=int(input("Sayıyı tahmin et"))
while True:


    if sayi == tuttugumsayi:
        print("sayiyiyi buldun")
        break
    elif sayi < tuttugumsayi:
        print("bulamadın, sayıyı büyüt ve tekrar dene")
        sayi = int(input("Sayıyı tahmin et"))


    else:
        print("bulamadın,sayıyı küçült ve tekrar dene")
        sayi = int(input("Sayıyı tahmin et"))
