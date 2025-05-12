import sys
from stats import *

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    book_text = get_book_text(path_to_book)
    num_of_words = get_number_of_words(book_text)
    list_of_letters = get_letters_list(book_text)

    print_raport(path_to_book, num_of_words, list_of_letters)

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        return f.read()

def print_raport(path_to_book, num_of_words, list_of_letters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for letter_dictionary in list_of_letters:
        print(f"{letter_dictionary["char"]}: {letter_dictionary["num"]}")
    print("============= END ===============")

main()