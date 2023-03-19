def encrypt(plain_text, key):
    """
    Fungsi ini akan mengenkripsi pesan yang diberikan menggunakan metode Vigenere Cipher.
    """
    cipher_text = ""
    key_len = len(key)
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            # Jika karakter adalah huruf, maka enkripsi menggunakan Vigenere Cipher
            key_char = key[key_index].upper()
            shift = ord(key_char) - 65

            if char.isupper():
                cipher_char = chr((ord(char) + shift - 65) % 26 + 65)
            else:
                cipher_char = chr((ord(char) + shift - 97) % 26 + 97)

            key_index = (key_index + 1) % key_len
        else:
            # Jika bukan huruf, abaikan dan tambahkan ke teks terenkripsi
            cipher_char = char

        cipher_text += cipher_char

    return cipher_text


def decrypt(cipher_text, key):
    """
    Fungsi ini akan mendekripsi teks yang diberikan menggunakan metode Vigenere Cipher.
    """
    plain_text = ""
    key_len = len(key)
    key_index = 0

    for char in cipher_text:
        if char.isalpha():
            # Jika karakter adalah huruf, maka dekripsi menggunakan Vigenere Cipher
            key_char = key[key_index].upper()
            shift = ord(key_char) - 65

            if char.isupper():
                plain_char = chr((ord(char) - shift - 65) % 26 + 65)
            else:
                plain_char = chr((ord(char) - shift - 97) % 26 + 97)

            key_index = (key_index + 1) % key_len
        else:
            # Jika bukan huruf, abaikan dan tambahkan ke teks biasa
            plain_char = char

        plain_text += plain_char

    return plain_text

# Contoh penggunaan program
plain_text = "Ini adalah pesan rahasia"
key = "266"
cipher_text = encrypt(plain_text, key)
print("Teks terenkripsi:", cipher_text)
decrypted_text = decrypt(cipher_text, key)
print("Teks biasa:", decrypted_text)
