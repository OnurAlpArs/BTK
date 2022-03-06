"""> BÜYÜKTÜR
< : KÜÇÜKTÜR
<= KÜÇÜK EŞİTTİR
>= BÜYÜK EŞİTTİR
== EŞİTTİR
!=EŞİT DEĞİLDİR
"""
cinsiyet=input("Bir harf giriniz:")

if cinsiyet=="e" or cinsiyet=="E":# or: iki şarttan biri doğru olduğunda çalışır.
    print("Cinsiyet olarak erkek girdiniz.")
    print("if içerisinden selamlar ")
elif cinsiyet=="k":#else if = elif
    print("cinsiyet olarak kadın girdiniz")
    print("şuanda elif bloğu içerisinden selam veriyorum ")
else: #şartların dışında bir şey olduğu zaman kullanılır.
    print("Ben sana e ya da ka gir demedim mi?")

