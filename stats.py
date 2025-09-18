def character_sort_on(character):
    return character["count"]

def get_number_of_words(book_text):
    array_of_words = book_text.split()
    return len(array_of_words)

def get_character_dictionary(book_text):
    lowercase_book_text = book_text.lower()
    character_set = set(lowercase_book_text)
    character_dictionary = {}
    for character in character_set:
        character_dictionary[character] = lowercase_book_text.count(character)
    return character_dictionary

def get_sorted_list_of_dictionaries(character_dictionary):
    list_of_dictionaries = list()
    for character in character_dictionary:
        if character.isalpha():
            list_of_dictionaries.append(
                {
                    "character": character,
                    "count": character_dictionary[character]
                }
            )
    list_of_dictionaries.sort(reverse=True, key=character_sort_on)
    return list_of_dictionaries
