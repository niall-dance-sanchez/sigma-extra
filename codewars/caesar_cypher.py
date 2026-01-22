def extract_words(message: str) -> list[str]:
    """
    Extracts words from a full message, ignoring 
    punctuation and sets them to lower case.
    """

    words = ""

    for char in message:
        if char.isalpha():
            words += char.lower()
        else:
            words += " "

    return words.split()

    # return "".join(char for char in message.lower() if char.isalpha() or char == " ").split()


def count_valid_words(words: list[str], valid_words: list[str]) -> int:
    """Counts the number of words in a list that appear in a given valid words list."""

    count = 0
    for w in words:
        if w in valid_words:
            count += 1

    return count


def shift_character(char: str, shift: int) -> str:

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    index = alphabet.index(char) + shift

    index = index % 26

    return alphabet[index]


def shift_message(words: k):
    pass


if __name__ == "__main__":
    print(shift_character("a", 5))
