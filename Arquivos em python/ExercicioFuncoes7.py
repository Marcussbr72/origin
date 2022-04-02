def main():

	a= (input("digite a: "))
	b= (input("digite b: "))
	c= (input("digite c: "))
	
	print ("Resposta: ",resp(a,b,c))

def resp(a,b,c):	
	if a==b==c:
		return 2
	elif a != b != c:
		return 0
	else:
		return 1
		
	
		





if __name__ == "__main__":
	main()
