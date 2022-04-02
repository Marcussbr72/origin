def main():
	a=['']*5
	print("Responda com s para sim e n para não: ")
	a[0]= input("Telefonou para vitima?")
	a[1]= input("Esteve no local do crime?")
	a[2]= input("Mora perto da vitima?")
	a[3]= input("Devia para a vitima?")
	a[4]= input("Ja trabalhou com a vitima?")
	sim = 0
	for x in a:
		if x == 's':
			sim +=1	

	print(teste(sim))
		
	
	
def teste(sim):
	if sim == 2:
		print("Você é suspeito...")
	elif (sim == 3) or (sim == 4):
		print("Você é cumplice...")
	elif sim == 5:
		print("Você é o assasino..")
	else:
		print("Você é inocente...")
		
if __name__ == "__main__":
	main()
