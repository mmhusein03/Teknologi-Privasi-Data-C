import random

def generate_key():
    """
    Fungsi ini akan menghasilkan kunci acak untuk Substitusi Cipher.
    :return: kunci dalam bentuk kamus
    """
    chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(chars)
    key = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", chars))
    return key


def encrypt(plain_text, key):
    """
    Fungsi ini akan mengenkripsi pesan yang diberikan menggunakan metode Substitusi Cipher.
    """
    cipher_text = ""

    for char in plain_text.upper():
        if char.isalpha():
            # Jika karakter adalah huruf, maka enkripsi menggunakan Substitusi Cipher
            cipher_char = key[char]
        else:
            # Jika bukan huruf, abaikan dan tambahkan ke teks terenkripsi
            cipher_char = char

        cipher_text += cipher_char

    return cipher_text


def decrypt(cipher_text, key):
    """
    Fungsi ini akan mendekripsi teks yang diberikan menggunakan metode Substitusi Cipher.
    """
    plain_text = ""

    for char in cipher_text.upper():
        if char.isalpha():
            # Jika karakter adalah huruf, maka dekripsi menggunakan Substitusi Cipher
            for k, v in key.items():
                if v == char:
                    plain_char = k
                    break
        else:
            # Jika bukan huruf, abaikan dan tambahkan ke teks biasa
            plain_char = char

        plain_text += plain_char

    return plain_text


# Contoh penggunaan program
plain_text = "Husein"
key = generate_key()
cipher_text = encrypt(plain_text, key)
print("Teks terenkripsi:", cipher_text)
decrypted_text = decrypt(cipher_text, key)
print("Teks biasa:", decrypted_text)
