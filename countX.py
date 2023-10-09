def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count


def main():
    lst= [0,6,8,10,8,20,10,0,0]
    x=6
    print('{} has occ {} times'.format(x, countX(lst,x)))

if __name__=="__main__":
    main()

    # return lst.count(x)