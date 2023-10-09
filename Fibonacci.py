def fib(n):
	a = 0
	b = 1

	for i in range(0, n):
		next = a + b
		print(next)

		a = b
		b = next

def main():
	n=10
	x = fib(n)

if __name__=="__main__":
	main()
