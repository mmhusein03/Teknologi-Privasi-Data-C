def encrypt(plain_text, shift):
    """
    Fungsi ini akan mengenkripsi pesan yang diberikan menggunakan metode Shift Cipher.
    """
    ciper=""
    for char in plain_text:
        if char ==" ":
            ciper = ciper + char
        elif char.isupper():
            ciper=ciper+chr((ord(char)+shift-65)%26+65)
        else:
            ciper=ciper+chr((ord(char)+shift-97)%26+97)
    return ciper

def decrypt(plain_text, shift):
    """
    Fungsi ini akan mendekripsi teks yang diberikan menggunakan metode Shift Cipher.
    """
    ciper=""
    for char in plain_text:
        if char ==" ":
            ciper = ciper + char
        elif char.isupper():
            ciper=ciper+chr((ord(char)-shift-65)%26+65)
        else:
            ciper=ciper+chr((ord(char)-shift-97)%26+97)
    return ciper

# Contoh penggunaan program
plain_text = "Ini adalah pesan rahasia"
shift = 66
cipher_text = encrypt(plain_text, shift)
print("Teks terenkripsi:", cipher_text)
decrypted_text = decrypt(cipher_text, shift)
print("Teks biasa:", decrypted_text)
