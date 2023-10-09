def check(n):
	if ( n%2==0 ):
		out = "even"
	else:
		out = "Odd"

	return (out)

def main():
	n=505
	a = check(n)
	print (a)

if __name__=="__main__":
	main()
