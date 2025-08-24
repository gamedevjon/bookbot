import sys
from stats import get_num_words
from stats import get_number_of_characters
from stats import print_data
from stats import sort_dictionary

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    #check for CLI args
    if (len(sys.argv)) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    text = get_book_text(sys.argv[1])

    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    number_of_characters = get_number_of_characters(text)
    sorted_dictionary = sort_dictionary(number_of_characters)
    print_data(sorted_dictionary)
    print("============= END ===============")

main()