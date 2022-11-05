print("Bienvenidos a la calculadora de medidas creada con un código de python :)")
print("¿Qué desea hacer?")
#print("1 = Medir una sucesión aritmetica \n 2 = Medir una sucesión Geometrica \n 3 = Medir la altura de algo \n 4 = medir el volumen de un cuerpo")
print("")
b = "1 = Medir una sucesión aritmetica"
c = "2 = Medir una sucesión Geometrica"
d = "3 = Medir la altura de algo"
e = "4 = Medir el volumen de un cuerpo"

print(b + "\n" + c + "\n" + d + "\n" + e + "\n")

a = int(input("Elección: "))
print("¿Estás seguro de que quieres " + str(a) + "?")
cel = int(input("Si = 1, No = 2: "))

if cel == 1:
	print("Ok bro")
else:
	print("Ni modo :)... hoy continue")

print("")

if a == 1:
	print("Requerimos sus datos :)")
	a1 = int(input("Digite el numero inicial: "))
	a2 = int(input("Digite la distancia o altura: "))
	a3 = int(input("Digite el numero de bloques: "))

	a7 = a1 + a2 * (a3 - 1)
	print("El resultado es el siguiente: ")
	print("Si el numero inicial es de: " + str(a1) + ", Su diferencia o altura es de: " + str(a2) + ", y el numero de veces por multiplicar es de: " + str(a3) + "\nSe tiene que su altura total es de: " + str(a7))

elif a ==2:
	print("Requerimos sus datos :)")
	b1 = int(input("Desea encontrar la diferencia de datos primero? Si = 1, No = 2"))
	if b1 == 1:
		b2 = int(input("Digite la medida de la primer cámara: "))
		b3 = int(input("Digite el numero de la segunda cámara: "))
		a2 = b3 / b2
		print("La diferencia o distancia de las cámaras es: " + str(a2))

		a1 = int(input("Digite el numero inicial: "))
		a2 = float(input("Digite la distancia o diferencia: "))
		a3 = int(input("Digite el numero de cámaras a encontrar: "))

		a7 = a1 * a2 ** (a3 - 1)

		print("El resultado es el siguiente: ")
		print("Si el numero inicial es de: " + str(a1) + ", Su diferencia o distancia es de: " + str(a2) + ", y el numero de cámaras por multiplicar es de: " + str(a3) + "\nSe tiene que su total es de: " + str(a7))

	else:
		print("Ok bro")
		print("Tons sigamos...")
		a1 = int(input("Digite el numero inicial: "))
		a2 = int(input("Digite la distancia o diferencia: "))
		a3 = int(input("Digite el numero de cámaras a encontrar: "))

		a7 = a1 * a2 ** (a3 - 1)

		print("El resultado es el siguiente: ")
		print("Si el numero inicial es de: " + str(a1) + ", Su diferencia o distancia es de: " + str(a2) + ", y el numero de cámaras por multiplicar es de: " + str(a3) + "\nSe tiene que su total es de: " + str(a7))

elif a == 3:
	a1 = int(input("Kiubo bro"))
	a2 = int(input(""))


else:
	print("Se ha equivocado vuelva a intentarlo...")

"""if a == 2:
	print("Requerimos sus datos :)")
	b1 = input("Desea encontrar la diferencia de datos primero? Si = s, No = n")
	if b1 == s:
		b2 = int(input("Digite la medida de la primer cámara: "))
		b3 = int(input("Digite el numero de la segunda cámara: "))
		a2 = b3 / b2
		print("La diferencia o distancia de las cámaras es: " + str(a2))

		a1 = int(input("Digite el numero inicial: "))
		a2 = int(input("Digite la distancia o diferencia: "))
		a3 = int(input("Digite el numero de cámaras a encontrar: "))

		a7 = a1 * a2 ** (a3 - 1)

		print("El resultado es el siguiente: ")
		print("Si el numero inicial es de: " + str(a1) + ", Su diferencia o distancia es de: " + str(a2) + ", y el numero de cámaras por multiplicar es de: " + str(a3) + "\nSe tiene que su total es de: " + str(a7))

	else:
		print("Ok bro")
		print("Tons sigamos...")
		a1 = int(input("Digite el numero inicial: "))
		a2 = int(input("Digite la distancia o diferencia: "))
		a3 = int(input("Digite el numero de cámaras a encontrar: "))

		a7 = a1 * a2 ** (a3 - 1)

		print("El resultado es el siguiente: ")
		print("Si el numero inicial es de: " + str(a1) + ", Su diferencia o distancia es de: " + str(a2) + ", y el numero de cámaras por multiplicar es de: " + str(a3) + "\nSe tiene que su total es de: " + str(a7))

else: 
	print("Se ha equivocado vuelva a intentarlo...")
"""