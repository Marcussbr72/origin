def main():
	a=[]
	for _ in range (4):
		b= float(input("digite a nota: "))
		a.append(b)
	media(a)
	
def media(a):
	soma= 0
	
	for x in a:
		print(x)
		soma= soma + x	
	print("Media",soma/4)
		





if __name__ == "__main__":
	main()
