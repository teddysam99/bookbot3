import sys
from stats import count_word
from stats import count_char
from stats import dict_sorted_list



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    word_count = count_word(get_book_text(path))
    dict_char_count = dict_sorted_list(count_char(get_book_text(path)))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in dict_char_count:
        ch = item["char"]
        print(f"{ch}: {item['num']}")
    print("============= END ===============")


main()
