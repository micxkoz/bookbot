def get_number_of_words(book_text):
    words = book_text.split()
    return len(words)

def get_letters_list(book_text):
    book_text = book_text.lower()
    characters_dict = {}
    for character in book_text:
        if character in characters_dict:
            characters_dict[character] += 1
        else:
            characters_dict[character] = 1
    
    letters_list = []
    for character in characters_dict:
        if character.isalpha():
            letters_list.append({"char": character, "num": characters_dict[character]})
    letters_list.sort(reverse=True, key=lambda dict: dict["num"])
    return letters_list
