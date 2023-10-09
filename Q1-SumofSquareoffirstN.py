def sum(n):
    Sum, count = 0, 0

    while(count<=n):
        square = (count * count)
        Sum = Sum + square
        count+=1
    return (Sum)


def main():
    n = 5
    x = sum(n)
    print(x)

if __name__ == "__main__":
    main()
