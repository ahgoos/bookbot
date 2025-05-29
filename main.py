import sys
from stats import count_words, count_characters, sort_characters

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    word_count = count_words(text)
    symbols_dict = count_characters(text)
    # print(f"Symbols found:\n{symbols_dict}")
    sorted_symbols = sort_characters(symbols_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for symbol in sorted_symbols:
        if symbol["char"].isalpha():
            print(f"{symbol['char']}: {symbol['num']}")
    print("============= END ===============")


main()
