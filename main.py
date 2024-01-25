def main():
    visible = get_text()  # call the text reading fxn
    print(visible)  # print the source text file to the console

    word_up = word_counter()  # call the word counting fxn
    print("\n")
    print(f"There are {word_up} words in the document.")
    print("\n")

    """ # ... code for counting the characters in the source document
    print("\n")
    letter_up = character_counter()
    print(f"This is the count of each character in the document:" "\n")
    print(letter_up)
    print("\n")
    """

    report_maker()  # call the report function
    print("\n")
    print("-- End of report --")


def get_text():  # this function retrieves and opens the source text file
    with open("books/frankenstein.txt") as f:
        return f.read()


def word_counter():  # this function counts the words in the source text file
    source = get_text()  # bring the source file into this function
    word_total = source.split()  # split source file into list
    return len(word_total)  # return list length (total words)


def character_counter():  # this function counts the characters in the source file
    source = get_text()  # bring the source file into this function
    lowered = source.lower()  # make source file all lowercase
    lowered_list = list(lowered)  # make source file into a countable list

    container = {}  # create dictionary

    for char in lowered_list:
        if char in container:  # if the character already is in the dictionary
            container[char] = container[char] + 1  # then {key: increment the value}
        else:  # if the character is NOT already in dictionary:
            container[char] = 1  # then {key: value is 1}
    return container


def report_maker():
    source_dict = character_counter()  # bring in source dictionary

    listed = []  # create empty list

    for i in source_dict:  # loop and ...
        listed.append((i, source_dict[i]))  # populate list with dict keys and values
        listed.sort()  # sort new list

    alphaset = "abcdefghijklmnopqrstuvwxyz"  # ... isolating characters ...
    alphaset_list = list(alphaset)  # ... that are in the alphabet

    for j in listed:
        if j[0] in alphaset_list:
            statement = f"The character '{j[0]}' occurs {j[1]} times"
            print(statement)
    return statement


main()
