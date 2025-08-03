import sys 
from stats import get_num_words, get_num_of_times, get_sorted_list

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        read_data = f.read()
    return read_data.strip()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book = get_book_text(filepath)
    num_words = get_num_words(book)
    num_of_times = get_num_of_times(book)
    sorted_dicts = get_sorted_list(num_of_times)

    print("============ BOOKBOT ============")
    print(f"Analizing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_dicts:
        char = char_dict["char"]
        if char.isalpha():
            count = char_dict["num"]
            print(f"{char}: {count}")


if __name__ == "__main__":
    main()
