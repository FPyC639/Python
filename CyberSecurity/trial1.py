import monoalphabetic as masters

cipher = masters.alphabet_soup()
print(cipher)
encrypted = masters.encrypt_with_monoalpha('Hello all you hackers out there!', cipher)
decrypted = masters.decrypt_with_monoalpha(encrypted, cipher)

print(encrypted)
print(decrypted)

