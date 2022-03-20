import random
while True:
    seviye = input("bir seviye giriniz (kolay/orta/zor):").lower()#yazıyı küçüğe çevirir/upper yazıyı büyüğe çevirir
    if seviye == "kolay":
        uret=random.randint(1,10)
        break
    elif seviye == "orta":
        uret=random.randint(1,50)
        break
    elif seviye == "zor":
        uret=random.randint(1,100)
        break
    else:
        print("lütfen geçerli zorluk girişi yapınız:")

while True:
    tahmin=int(input("Tahmininiz:"))
    if tahmin==uret:
        print("Tebrikler,sayıyı doğru tahmin ettiniz.")
        break
    elif tahmin<uret:
        print("Üzgünüm,tahmininizi büyütün.")

    else :
        print("Üzgünüm,tahmininizi küçültün.")


