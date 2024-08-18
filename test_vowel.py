def main():
    x= input("Input:")
    print(shorten(x))


def shorten(word):
    w=[]
    for letter in word:
        if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            w.append(letter)
    result= "".join(w)
    return result



if __name__ == "__main__":
    main()

