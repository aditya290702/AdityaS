def stringhalf(w):
    a=len(w)//2
    halfstring = a
    b = w[0:a]
    print(b)

def main():
    w=input()
    x=stringhalf(w)
    return(x)

if __name__=="__main__":
    main()