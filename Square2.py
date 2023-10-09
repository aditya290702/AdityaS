def sq(n):
	sq , count , sum = 0, 0, 0

	if (n > 0):
		while (count<= n):
			sq = (count) * (count)
			sum = (sum) + (sq)
			count = (count) + 1
		return(sum)
	
	else:
		if (n < 0):
		        while (count>= n):
        		        sq = (count) * (count)
               			sum = (sum) + (sq)
               			count = (count) - 1
       			return(sum)


def main():
	n = -10
	x = sq(n)
	print (x)

if __name__=="__main__":
	main()
