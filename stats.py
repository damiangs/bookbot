def get_num_words(text):
    num_words = text.split()
    return len(num_words)

def get_num_of_times(text):
    text = text.lower()
    characters_dict = {}

    for character in text:
        if character in characters_dict:
            characters_dict[character] += 1
        else:
            characters_dict[character] = 1
        
    return characters_dict

def sort_on(items):
    return items["num"]

def get_sorted_list(char_dict):
    sorted_list = []

    for key, value in char_dict.items():
        new_char_dict = {"char": key, "num": value}
        sorted_list.append(new_char_dict)

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
