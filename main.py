import wordcounter

# def main():
#     bookpath = "books/frankenstein.txt"
#     print("--- Begin report of books/frankenstein.txt---\n")
#     file_contents = wordcounter.get_book_path(bookpath)
#     num_of_word = wordcounter.words(file_contents)
#     print(f"{num_of_word} words found in the document\n")
#     report = wordcounter.reports(file_contents)
#     print(report)
#     print("--- End report ---")
    

# if __name__ == "__main__":
#     main()

def main():
    bookpath = "books/frankenstein.txt"
    file_contents = wordcounter.get_book_path(bookpath)
    num_of_word = wordcounter.words(file_contents)
    report = wordcounter.reports(file_contents)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print()  # This adds one blank line
    print(f"{num_of_word} words found in the document")
    print()  # This adds one blank line
    print(report)
    print("--- End report ---")

if __name__ == "__main__":
    main()