import itertools


def generate_passwords(length):
    # Rakamların kombinasyonlarını oluştur
    combinations = itertools.product(range(10), repeat=length)

    # Oluşan kombinasyonları stringlere dönüştür
    passwords = [''.join(map(str, combination)) for combination in combinations]

    return passwords


def main():
    try:
        hanecount = int(input("Kaç haneli şifreler oluşturulsun? (En fazla 8 haneli): "))
        if hanecount < 1 or hanecount > 8:
            print("Hane sayısı 1 ile 8 arasında olmalıdır.")
            return
    except ValueError:
        print("Geçersiz giriş. Lütfen bir tam sayı girin.")
        return

    # Kullanıcıya dosyanın kaydedileceği yolu sormak
    file_path = input("Şifrelerin kaydedileceği dosya yolu ve adı nedir? (Örneğin: passwords.txt): ")

    passwords = generate_passwords(hanecount)

    # Kullanıcının belirttiği yere şifreleri yazmak
    with open(file_path, "w") as file:
        for password in passwords:
            file.write(password + "\n")

    print(f"{len(passwords)} adet şifre oluşturuldu ve {file_path} dosyasına kaydedildi.")


if __name__ == "__main__":
    main()
