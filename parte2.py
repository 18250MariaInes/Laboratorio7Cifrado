'''
Maria Jose Castro 181202
Diana de Leon 18607
Camila Gonzalez 18398
Maria Ines Vasquez 18250
'''
#codigo extraido de 
#https://pypi.org/project/elgamal/#description

from elgamal.elgamal import Elgamal

#Aqui se ingresa el texto
m = b'Laboratorio 7 Cifrado'
#lo imprimos
print('El texto plano enviado: ', m)
print()


#aqui se generan ambas llave, publicas y privadas
pb, pv = Elgamal.newkeys(128)

#se imprimen ambas llaves
print('El numero primo es: ', pb.p)
print()
print('El generador de la llave Publica: ',pb.g)
print()
print('La llave publica es: ', pb)
print()
print('La llave privada: ', pv)

#aqiuu se cifra el mensaje tomando como parametro
#el texto y la llave publica
ct = Elgamal.encrypt(m, pb)

#mostramos el texto Cifrado
print()

print('El texto encriptado: ' ,ct)

#desencriptar el texto con la llave privada
dd = Elgamal.decrypt(ct, pv)

#mostrar texto plano
print()
print('El texto recibido es:', dd)
print()
