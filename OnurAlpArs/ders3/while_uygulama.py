# kullanıcı adı iste ve şifre admin ve 123456 isteyince kabıl et yanlış girdikçe yeniden iste


while True :
    kullanıcı_adı = input("kullanıcı adı giriniz:")
    sifre = input("Şifre giriniz:")
    if kullanıcı_adı=="admin" and sifre=="123456":
        print("Hoşgeldiniz")
        break
    else:
        print("hatalı kullanıcı adı veya şifre")
