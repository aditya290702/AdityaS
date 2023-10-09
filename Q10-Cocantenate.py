def cocantenate(a):
    b = "this is the second line"
    a+= " " + b
    print (a)

def main():
    a=input()
    x=cocantenate(a)
    return(x)

if __name__== "__main__":
    main()