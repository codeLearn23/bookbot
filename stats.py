import sys


def get_book_text():  # this function retrieves and opens the source text file
    with open(sys.argv[1]) as f:
        return f.read()


def word_counter():  # this function counts the words in the source text file
    source = get_book_text()  # bring the source file into this function
    word_total = source.split()  # split source file into list
    return len(word_total)  # return list length (total words)


def character_counter():  # this function counts the characters in the source file
    source = get_book_text()  # bring the source file into this function
    lowered = source.lower()  # make source file all lowercase
    lowered_list = list(lowered)  # make source file into a countable list

    container = {}  # create dictionary

    for char in lowered_list:
        if char in container:  # if the character already is in the dictionary
            container[char] = container[char] + 1  # then {key: increment the value}
        else:  # if the character is NOT already in dictionary:
            container[char] = 1  # then {key: value is 1}
    return container


# this code presents a more readable character count


def report_maker():
    source_dict = character_counter()  # bring in source dictionary

    listed = []  # create empty list

    for i in source_dict:  # loop and ...
        listed.append((i, source_dict[i]))  # populate list with dict keys and values
        listed.sort()  # sort new list

    alphaset = "abcdefghijklmnopqrstuvwxyzæâêëô"  # ... isolating characters ...
    alphaset_list = list(alphaset)  # ... that are in the alphabet

    print(
        f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------\nFound {word_counter()} total words\n--------- Character Count -------"
    )
    for j in listed:
        if j[0] in alphaset_list:
            statement = f"{j[0]}: {j[1]}"
            print(statement)
    print("============= END ===============")
    return statement
