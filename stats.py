def count_char(text):
    dict_of_letters = {}
    lower_case = text.lower()
    words = lower_case.split
    for word in lower_case:
        if word not in dict_of_letters:
            dict_of_letters[word] = 1
        elif word in dict_of_letters:
            dict_of_letters[word] += 1
    return dict_of_letters

def count_word(text):
    print(f"total {len(text.split())} number of words")