def main():

	lado1= (input("digite um lado do triangulo: "))
	lado2= (input("digite outro lado do triangulo: "))
	lado3= (input("digite o ultimo lado do triangulo: "))
	if (lado1+lado2>lado3) or (lado2+lado3>lado1) or (lado3+lado1>lado2):
		print ("É Triangulo")
		if lado1==lado2==lado3:
			print("É equilatero")
		elif lado1 != lado2 != lado3:
			print("É escaleno")
		else:
			print("É isoceles")
	else:
		print("Não é Triangulo")
		
	
	






if __name__ == "__main__":
	main()
