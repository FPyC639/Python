import random as rand
from string import ascii_letters
lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 
   67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 
   157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 
   251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,317, 331, 337, 347, 349, 
   353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 
   457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 
   571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 
   673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 
   797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 
   911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
def ifLowPrime(size=1024):
    x = rand.randint(1,size)
    if x in lowPrimes:
        return x
    else:
        return ifLowPrime()
def alphabet_soup(size=1024):
    seed = ifLowPrime(size)
    rand.seed(seed)
    abcssoup = list(ascii_letters+ascii_letters.upper())
    switch = list(ascii_letters+ascii_letters.upper())
    for i in range(0,seed,20):
        rand.shuffle(switch)
    return dict(zip(abcssoup, switch))
def inverse_monoalpha_cipher(monoalpha_cipher):
   inverse_monoalpha = {}
   for key, value in monoalpha_cipher.items():
      inverse_monoalpha[value] = key
   return inverse_monoalpha

def encrypt_with_monoalpha(message, monoalpha_cipher):
   encrypted_message = []
   for letter in message:
      encrypted_message.append(monoalpha_cipher.get(letter, letter))
   return ''.join(encrypted_message)

def decrypt_with_monoalpha(encrypted_message, monoalpha_cipher):
   return encrypt_with_monoalpha(
      encrypted_message,
      inverse_monoalpha_cipher(monoalpha_cipher)
   )
