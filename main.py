import sys
from stats import count_words, get_sorted_character_counts


def get_text(book):
    file_contents = None
    # https://docs.python.org/3/reference/compound_stmts.html#with
    with open(book) as f:
        # https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_text(sys.argv[1])
    word_count = count_words(text)
    sorted_character_count = get_sorted_character_counts(text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print(sorted_character_count)
    print("============= END ===============")


main()
