def prime(n):
    a=n*n

    if(a%2!=0):
        out = "prime"
    else:
       out = "not prime"

    return(out)

def main():
    n=55
    c=prime(n)
    print (c)

if __name__=="__main__":
    main()

