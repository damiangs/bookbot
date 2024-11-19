def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters_dictionary = get_characters(text)
    report = get_report(characters_dictionary)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    for item in report:
        print(f"The '{item["character"]}' was found {item["count"]} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_characters(text):
    lowered_text = text.lower()
    characters = {}

    for letter in lowered_text:
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1

    return characters

def get_report(dict):

    character_lists = []

    for character, count in dict.items():
        character_lists.append({"character": character, "count":count})

    def sort_on(dict):
        return dict["count"]

    character_lists.sort(reverse=True, key=sort_on)

    return character_lists



main()
