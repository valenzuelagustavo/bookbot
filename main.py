from stats import get_num_words, get_each_char, sort_on
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        file_content = f.read()
    return file_content    

def main():
    if len(sys.argv) == 2:    
        book_path = sys.argv[1]
        file_content = get_book_text(book_path)

        num_words = file_content.split()
        counter = get_num_words(num_words)

        num_char = get_each_char(file_content)

        letters_sort = sort_on(num_char)



        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {counter} total words")
        print("--------- Character Count -------")
        for letter in letters_sort:
            print(f"{letter['char']}: {letter['count']}")
        print("============= END ===============")

    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()


