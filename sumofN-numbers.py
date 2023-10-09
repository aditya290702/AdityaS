def sum(n):
	Sum, count = 0, 0
	
	while (count <= n):
		Sum = Sum + count
		count = count + 1
	
	return (Sum)

def main():
	n=input()
	x = sum(n)
	print (x)

if __name__=="__main__":
	main()
