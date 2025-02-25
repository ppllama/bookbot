import stats
import sys
#from stats import *

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
    if len(sys.argv) <2:
        print("Usage:python3 main.py <path_to_book>")
        sys.exit(1)
    bookpath = sys.argv[1]
    file_contents = stats.get_book_path(bookpath)
    num_of_word = stats.words(file_contents)
    report = stats.reports(file_contents)
    
    print(f"--- Begin report of {sys.argv[1]} ---")
    print()  # This adds one blank line
    #print(f"{num_of_word} words found in the document")
    print(f"Found {num_of_word} total words")
    print()  # This adds one blank line
    print(report)
    print("--- End report ---")

if __name__ == "__main__":
    main()