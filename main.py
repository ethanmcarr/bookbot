def get_book_text(book_file_path):
    with open(book_file_path) as book_file:
        book_contents = book_file.read()
    return book_contents

def get_number_of_words(book_text):
    array_of_words = book_text.split()
    return len(array_of_words)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    number_of_words = get_number_of_words(book_text)
    print(f"{ number_of_words } words found in the document")

main()
