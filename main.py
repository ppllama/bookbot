import wordcounter

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)
        num_of_word = wordcounter.words(file_contents)
        print(num_of_word)

if __name__ == "__main__":
    main()