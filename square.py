#def sq(n):
#	x = 0

#	for i in range (0, n):
#		x = n*n
#		n = n+1
	
#def main():
#	n=5
#	y=sq(n)
#	print (y)

#if __name__=="__main__":                                                                                        Fibonacci.py                                                                                                 
def sq(n):
        
	b = 1
	for i in range(0, n):
		sq = b * b
		b = b + 1
                print(sq)

def main():
       	n=10
       	x = sq(n)

if __name__=="__main__":
        main()


