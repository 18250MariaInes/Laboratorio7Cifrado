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
from math import pow, gcd
from Crypto.Util.number import getPrime
import os
  
a = random.randint(2, 10) 

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
    # q es p
    # h es K
    # g es g
    #Cifrado
    print("-----CIFRADO-----")
    en_msg = [] 
    
    # k es b
    k = gen_key(q)# la llave privada
    print("La llave privada (k) de Bob es: ", k) 
    # s es y2
    s = powerMod(h, k, q) #Se realiza la exponenciacion modular con h
    # p es y1
    p = powerMod(g, k, q) #Se realiza la exponenciacion modular con g
      
    for i in range(0, len(msg)): 
        en_msg.append(msg[i]) #se guarda msg caracter por caracter
  
    print("g**k usado : ", p) 
    print("g**ak usado : ", s) 
    for i in range(0, len(en_msg)): 
        en_msg[i] = s * ord(en_msg[i]) 
  
    return en_msg, p 

# Desencripcion del mensaje con p, la llave y q 
def decrypt(en_msg, p, key, q): 
    
    print("-----DESCIFRADO-----")
    dr_msg = [] 
    h = powerMod(p, key, q) #Se realiza la exponenciacion modular
    for i in range(0, len(en_msg)): 
        dr_msg.append(chr(int(en_msg[i]/h)))  #Se desencripta cada caracter el msg
          
    return dr_msg 
  
# Se utilizan los metodos
def main(): 
  
    msg = 'esto es facil de cifrar'
    print("Mensaje original :", msg) 
    # q es p
    q = getPrime(100) # se genera q con numeros random grandes
    print("p numero primo usado : ", q)
    g = random.randint(2, q) # se genera g en base a q
    # key es a 
    key = gen_key(q)# se crea la llave privada
    # K 
    h = powerMod(g, key, q) #Se realiza la exponenciacion modular 
    
    print("g usado : ", g)
    print("La llave privada (key) de Alice es: ", key) 
    print("g**a usado : ", h) 
  
    en_msg, p = encrypt(msg, q, h, g) # se encripta el mensaje con q, h, g
    print("Mensaje Cifrado :", en_msg)
    dr_msg = decrypt(en_msg, p, key, q) # se desencripta el mensaje con p, la llave y q
    dmsg = ''.join(dr_msg)  # se concatena el mensaje y se imprime
    print("Mensaje Descifrado :", dmsg)
  
  
if __name__ == '__main__': 
    main() 


