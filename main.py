from stats import count_word
from stats import count_char



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    text = "books/frankenstein.txt"
    word_count = count_word(get_book_text(text))
    dict_char_count = count_char(get_book_text(text))
    #print(get_book_text(text))
    #print(word_count)
    print(dict_char_count)



main()