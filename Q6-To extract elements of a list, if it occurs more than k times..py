def extract(l):
    word = "ADITYAAAAA"
    letter_counts = {letter: word.count(letter) for letter in word}
    print(letter_counts)

    if(letter_counts > l):
        print(letter)
def main():
    l = "A"
    x=extract(l)
    return (x)

if __name__=="__main__":
    main()