from stats import word_counter
from stats import get_book_text

from stats import character_counter

from stats import report_maker


def main():
    visible = get_book_text()  # call the text reading fxn
    # print(visible)  # print the source text file to the console

    word_up = word_counter()  # call the word counting fxn
    print("\n")
    # print(f"{word_up} words found in the document")
    print("\n")

    """ # ... code for counting the characters in the source document
    print("\n")
    letter_up = character_counter()
    print(f"This is the count of each character in the document:" "\n")
    print(letter_up)
    print("\n")
    """

    char_count = character_counter()
    report_maker()  # call the report function
    # print(char_count)
    print("\n")
    # print(report)


main()
