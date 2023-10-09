print("enter the charecter to be searched")
def count(w):
    a=input()
    b=w.count(a)
    print(b)


def main():
    w="THIS IS A TEST LINE TO COUNT THE NUMBERS OF LETTERS"
    c=count(w)
    return(c)

if __name__=="__main__":
    main()