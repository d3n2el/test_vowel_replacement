def main():
    x= input("Input:")
    print(shorten(x))


def shorten(word):
    w = []
    for letter in word:
        if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
             w.append(letter)
        if w[-1] == " ":
                w[-1].replace(" ", "")
        print(f"Processing '{letter}': {w}")
    result = "".join(w)
    return result



if __name__ == "__main__":
    main()
