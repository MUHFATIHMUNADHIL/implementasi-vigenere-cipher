def print_vigenere_table():
    print("="*58)
    print("                 TABEL VIGENERE (26x26)")
    print("="*58)
    
    # Cetak header kolom
    print("  | " + " ".join([chr(i) for i in range(65, 91)]))
    print("-" * 56)
    
    # Cetak baris demi baris
    for i in range(26):
        row = [chr(((i + j) % 26) + 65) for j in range(26)]
        print(f"{chr(65+i)} | " + " ".join(row))
    print("="*58 + "\n")

def vigenere_cipher(text, keyword, decrypt=False):

    text = text.upper().replace(" ", "")
    keyword = keyword.upper().replace(" ", "")
    result = ""
    kw_len = len(keyword)
    kw_idx = 0

    for char in text:
        if char.isalpha():
            t_val = ord(char) - 65
            k_val = ord(keyword[kw_idx % kw_len]) - 65
            
            # Logika perhitungan
            if decrypt:
                c_val = (t_val - k_val) % 26
            else:
                c_val = (t_val + k_val) % 26
                
            result += chr(c_val + 65)
            kw_idx += 1
        else:
            result += char 
            
    return result


print_vigenere_table()


plaintext = "orang baik" 
keyword = "hebat kamu"              


ciphertext = vigenere_cipher(plaintext, keyword, decrypt=False)


decrypted_text = vigenere_cipher(ciphertext, keyword, decrypt=True)


print("HASIL VIGENERE CIPHER")
print(f"Keyword      : {keyword}")
print(f"Plaintext    : {plaintext}")
print(f"Ciphertext   : {ciphertext}")
print(f"Decrypted    : {decrypted_text}")