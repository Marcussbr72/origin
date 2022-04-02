def main():
	nome= input("Digite uma string: ").lower()
	
	print(mais_frequentes(nome))
	
def mais_frequentes(nome):
	dic={}
	for letra in nome:
		if letra not in dic:
			dic[letra] = 1
		else:	
			dic[letra] += 1
	return dic

	
		





if __name__ == "__main__":
	main()
