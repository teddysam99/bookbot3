def count_char(text):
    char_dict = {}
    words = text.split()
    for word in words:
        lower_case = word.lower()
        for letter in lower_case:
            if letter not in char_dict:
                char_dict[letter] = 1
            else:
                char_dict[letter] += 1
    return char_dict
 

def count_word(text):
    return len(text.split())

def sort_on(items):
    return items["num"]

def dict_sorted_list(char_dict):
    char_list = []
    for char, num in char_dict.items():
        char_list.append({"char": char, "num": num})
    char_list.sort(reverse=True, key=sort_on)
    return char_list