import sys
from stats import (
    get_total_chars_by_book,
    get_alphabetical_order_list_of_chars,
    get_total_of_words,
)


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    frankestein_book = get_book_text(book_path)
    total_words = get_total_of_words(frankestein_book)
    total_of_words_by_book = get_total_chars_by_book(frankestein_book)
    order_list = get_alphabetical_order_list_of_chars(total_of_words_by_book)

    msg = """============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------"""
    msg += f"\nFound {total_words} total words\n"
    msg += "--------- Character Count -------\n"

    for item in order_list:
        msg += f"{item["name"]}: {item['num']}\n"

    msg += "============= END ==============="

    print(msg)


main()
