import re

def whkontrol(pw):
    skor = 0

    if len(sifre) >= 8:
        skor += 1
    if re.search(r"[A-Z]", pw):
        skor += 1
    if re.search(r"[a-z]", pw):
        skor += 1
    if re.search(r"[0-9]", pw):
        skor += 1
    if re.search(r"[!@#$%^&*()_+]", pw):
        skor += 1

    return skor

if __name__ == "__main__":
    pw = input("Kontrol edilecek şifreyi girin: ")
    skor = whkontrol(pw)

    if skor <= 2:
        print("Zayıf şifre")
    elif skor <= 4:
        print("Orta şifre")
    else:
        print("Güçlü şifre")
