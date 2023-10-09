def PRINTALT(w):
    c=len(w)
    print(w[0:c:2])
def main():
    w=input()
    x=PRINTALT(w)
    return (x)

if __name__=="__main__":
    main()