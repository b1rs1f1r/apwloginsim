for x in range(3):
    parola=input("Bir parola belirleyin: ")
    if x==2:
        print("Parolayı 3 kez yanlış girdiniz.",
        "Lütfen daha sonra tekrar deneyin...")

    elif not parola:
        print("Parola boş bırakılamaz")

    elif len(parola) in range(4,8):
        print("Yeni parolanız: ",parola)
        break

    else:
        print("Parola 8 karakterden kısa, 3 karakterden uzun olmalı")
