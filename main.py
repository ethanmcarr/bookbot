from stats import get_number_of_words
from stats import get_character_dictionary
from stats import get_sorted_list_of_dictionaries
import sys

def get_book_text(book_file_path):
    with open(book_file_path) as book_file:
        book_contents = book_file.read()
    return book_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_file_path = sys.argv[1]
    book_text = get_book_text(book_file_path)
    number_of_words = get_number_of_words(book_text)
    dictionary_of_words = get_character_dictionary(book_text)
    character_dictionary_list = list(get_sorted_list_of_dictionaries(dictionary_of_words))
    print(f"{ number_of_words } words found in the document")
    print()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at { book_file_path }...")
    print("----------- Word Count ----------")
    print(f"Found { number_of_words } total words")
    print("--------- Character Count -------")
    for i in character_dictionary_list:
        print(f"{ i["character"] }: { i["count"] }")
    print("============= END ===============")

main()
