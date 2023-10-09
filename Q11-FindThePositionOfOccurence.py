#CODE IS WORKING BUT NOT ABLE TO DO THE SAME THING WITH USER INPUT
def freq(n):
    a="ADITYA"
    b=len(a)
    for i in range (0, len(a)):
       if(n==a[i]):
           print(i)

def main():
    n=input()
    c=freq(n)
    return(c)

if __name__=="__main__":
    main()