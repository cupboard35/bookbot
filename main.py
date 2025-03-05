import sys
from stats import number_of_words, counting_character, sorter

def get_books_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book")
        sys.exit(1)
    
    path = sys.argv[1]
    main_string = get_books_text(path)
    dictionary = counting_character(main_string)
    num_words = number_of_words(main_string)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    for dict in sorter(dictionary):
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main()