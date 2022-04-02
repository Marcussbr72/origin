def main():
	pessoas = []
	
	for i in range(3):
		listaPessoas(pessoas)
		print(pessoas)
		

def listaPessoas(pessoas):
	dic={}
	cpf= input("Digite o CPF: ")
	dic['cpf']= cpf
	nome= input("Digite o nome:")
	dic['nome']= nome
	idade= input("Digite a idade:")
	dic['idade']= idade 
	fone= input("Digite o Telefone:")
	dic['fone']= fone
	pessoas.append(dic)
def deleteMenores(pessoas):
	
	del pessoas['idade']
	return pessoas		


if __name__ == "__main__":
	main()
