# Extraído de https://www.geeksforgeeks.org/elgamal-encryption-algorithm/
  
"""
Laboratorio 7
Cifrado de información
#Maria Jose Castro 181202
#Diana de Leon 18607
#Camila Gonzalez 18398
#Maria Ines Vasquez 18250
"""
import random  
from math import pow
import generate_prime as Prime
  
a = random.randint(2, 10) 

def gcd(a, b): 
    if a < b: 
        return gcd(b, a) 
    elif a % b == 0: 
        return b; 
    else: 
        return gcd(b, a % b) 


# Se generan numeros grandes random
def gen_key(q): 
  
    key = random.randint(10**20, q) 
    while gcd(q, key) != 1: 
        key = random.randint(10**20, q) 
  
    return key 


# Exponenciacion modular con 3 numeros 
def powerMod(a, b, c): 
    x = 1
    y = a 
  
    while b > 0: 
        if b % 2 == 0: 
            x = (x * y) % c; 
        y = (y * y) % c 
        b = int(b / 2) 
  
    return x % c 
  
# Encriptacion simetrica del mensaje con q, h y g 
def encrypt(msg, q, h, g): 
  
    en_msg = [] 
  
    k = gen_key(q)# la llave privada 
    s = powerMod(h, k, q) #Se realiza la exponenciacion modular con h
    p = powerMod(g, k, q) #Se realiza la exponenciacion modular con g
      
    for i in range(0, len(msg)): 
        en_msg.append(msg[i]) #se guarda msg caracter por caracter
  
    print("g**k usado : ", p) 
    print("g**ak usadp : ", s) 
    for i in range(0, len(en_msg)): 
        en_msg[i] = s * ord(en_msg[i]) 
  
    return en_msg, p 

# Desencripcion del mensaje con p, la llave y q 
def decrypt(en_msg, p, key, q): 
  
    dr_msg = [] 
    h = powerMod(p, key, q) #Se realiza la exponenciacion modular
    for i in range(0, len(en_msg)): 
        dr_msg.append(chr(int(en_msg[i]/h)))  #Se desencripta cada caracter el msg
          
    return dr_msg 
  
# Se utilizan los metodos
def main(): 
  
    msg = 'esto es facil de encriptar'
    print("Mensaje original :", msg) 
  
    q = random.randint(pow(10, 20), pow(10, 50)) # se genera q con numeros random grandes
    g = random.randint(2, q) # se genera g en base a q
  
    key = gen_key(q)# se crea la llave privada
    h = powerMod(g, key, q) #Se realiza la exponenciacion modular 
    print("g usado : ", g) 
    print("g**a usado : ", h) 
  
    en_msg, p = encrypt(msg, q, h, g) # se encripta el mensaje con q, h, g
    dr_msg = decrypt(en_msg, p, key, q) # se desencripta el mensaje con p, la llave y q
    dmsg = ''.join(dr_msg)  # se concatena el mensaje y se imprime
    print("Mensaje Descifrado :", dmsg); 
  
  
if __name__ == '__main__': 
    main() 

"""from __future__ import division
from random import SystemRandom

cryptogen = SystemRandom()

# find a prime
p = 809

# random g
g = 256

# private key d from {1..,p-2}
d = 68

# public key part
k = (g ** d) % p


## k_rpiv d
## k_pub: p, g, k


# message
m = 100
# r is any real number
r = 89
# encryption
e = (g ** r) % p
# cipher
c = (k ** r * m) % p

# decryption
s = (e ** d) % p
dec = (1/s * c) % p
#dec = ((e ** d) ** (p - 2) * c) % p
print(m, e, c, dec)"""

