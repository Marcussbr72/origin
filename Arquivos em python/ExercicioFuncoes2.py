def main():

	lado1= int(input("digite o numero 1: "))
	lado2= int(input("digite o numero 2: "))
	lado3= int(input("digite o numero 3: "))
	lado4= int(input("digite o numero 4: "))
	print("A soma é",soma(lado1,lado2,lado3,lado4))
	print("A multiplicação é",mult(lado1,lado2,lado3,lado4))
	print("A divisão é",div(lado1,lado2,lado3,lado4))


def soma(lado1,lado2,lado3,lado4):
	s=lado1+lado2+lado3+lado4
	return s

def mult(lado1,lado2,lado3,lado4):
	m=lado1*lado2*lado3*lado4
	return m
	
def div(lado1,lado2,lado3,lado4):
	d=lado1/lado2/lado3/lado4
	return d

if __name__ == "__main__":
	main()
