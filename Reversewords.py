def rev(s):

    words=s.split()
    x = words[::-1]
def main():
    s = "who will win the world cup"
    b=rev(s)
    print(b)

if __name__=="__main__":
	main()
