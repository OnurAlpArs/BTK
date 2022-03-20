try:
    sayi=int(input("bir sayı giriniz"))
    sayi2=int(input("bir sayı giriniz"))
    print("sayilarımızın bölümü:",sayi/sayi2)
except ValueError:
    print("Lütfen sayı giriniz")
except ZeroDivisionError:
    print("olmaz")