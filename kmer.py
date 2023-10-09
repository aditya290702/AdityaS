def kmer(w):

	for i in range(0,len(w)):
		n=3
		a=w[i:i+n]
		print(a)
	
def main():
	w = input()
	return kmer(w)

if __name__=="__main__":
        main()




