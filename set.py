def set():
    playerscores = {
        "Rohit": {53, 87, 96},
        "Virat": {123, 21, 78},
        "Shubham": {23, 44, 85}
    }
    for name, scores in playerscores.items():
        if scores & {21, 85}:  # scores intersection with 21 and scores intersection with 85
            print(name)

def main():
        x=set()
        return(x)

if __name__=="__main__":
    main()