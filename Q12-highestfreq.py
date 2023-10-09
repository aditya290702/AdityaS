#FACING PROBLEM IN THE SYNTAX!!!

def freq(w):
    b=len(w)
    j=0
    for i in range (0, len(w)):
       if(w[i]==w[j]):
           print(w[i])

def main():
    w="ADIYAAATTTTTTTTYA"
    c=freq(w)
    return(c)

if __name__=="__main__":
    main()