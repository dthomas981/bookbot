import sys

from stats import get_num_words
from stats import get_num_letters
from stats import get_sorted_num_letters

def get_book_text(path_to_file):

    with open(path_to_file) as f:
        # do something with f (the file) here
        # f is a file object
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    sorted_char_count = get_sorted_num_letters(get_num_letters(text))
    for i in sorted_char_count:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")


main()