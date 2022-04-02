def main():

	segundos= int(input("digite o total de segundos: "))
	print ("O valor em horas é: ",converte(segundos))
		
		

def converte(segundos): 
	segundos = segundos % (24 * 3600) 
	hora = segundos // 3600
	segundos %= 3600
	minutos = segundos // 60
	segundos %= 60
	      
	return "%d:%02d:%02d" % (hora, minutos, segundos) 
	      
	
	
	

if __name__ == "__main__":
	main()
