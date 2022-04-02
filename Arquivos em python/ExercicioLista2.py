def main():
	a=[]
	for _ in range (10):
		b= input("digite a letra: ")
		a.append(b)
	teste(a)
	
def teste(a):
	consoantes = 0
	
	for x in a:
		if x not in ['a', 'e', 'i' , 'o' , 'u']:
			print(x)
			consoantes = consoantes + 1
		
	print(consoantes)
		





if __name__ == "__main__":
	main()
