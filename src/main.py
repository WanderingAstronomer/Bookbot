import sys
from stats import get_book_as_str, get_words, get_wordcount, get_char_count, sort_dict

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

FILE = sys.argv[1]
text = get_book_as_str(FILE)

if __name__ == "__main__":
    try:
        # Returns word_count via composable function calls.
        word_count = get_wordcount(get_words(text))
        # Returns character_count via composable function calls.
        char_count = get_char_count(text)
        # Returns list of dictionaries sorted by character frequency, descending, each on a new line.
        sorted_char_count = sort_dict(char_count)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {FILE}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for item in sorted_char_count:
            ch = item["char"]
            if ch.isalpha():
                print(f"{ch}: {item['num']}")
        print("============= END ===============")
    except FileNotFoundError:
        print("File not found!")
