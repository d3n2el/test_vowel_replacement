def main():
    x= input("Input:")
    print(shorten(x))


def shorten(word):
    for letter in word:
        if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            word = word.replace(letter, "")
    return word



if __name__ == "__main__":
    main()
