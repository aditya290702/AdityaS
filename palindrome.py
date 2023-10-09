def check(w):

	if (w[-1::-1] == w[:]):
		return "PALINDROME"
	else:		
		return "not"

def main():
	w = input()
	y = check(w)
	print (y)

if __name__=="__main__":
	main()
