def main():
    x= input("Input:")
    print(shorten(x))


def shorten(word):
    for letter in word:
        if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            y+= word.replace(letter, "")
    return y



if __name__ == "__main__":
    main()