def get_longest_word(list_of_words: list) -> str:
    """
    Get the longest word out of a list of words

    Example
    >>> input_list = ["Hello", "Python", "rat"]
    >>> get_longest_word(input_list)  # This returns Python

    :param list_of_words: List of words
    :return: Longest word
    """
    pass


def sum_of_evens(list_of_integers: list) -> int:
    """
    Compute the sum of the even numbers on the given list

    Example
    >>> input_list = [1, 2, 3, 4]
    >>> sum_of_evens(input_list) # This returns 6

    :param list_of_integers: List of numbers
    :return: Sum of the even numbers
    """
    pass


def truncate_words(list_of_words: list, max_len: int) -> list:
    """
    Truncate the words longer than the max_len parameter, such that only the first max_len characters are kept
    Also keep words shorter than the max_len parameter

    Example
    >>> input_list = ["Hello", "Python", "rat"]
    >>> truncate_words(list_of_words, 3)  # This returns ["Hel", "Pyt", "rat"]

    :param list_of_words: List of words
    :param max_len: Maximum length of the word
    :return: Truncated list of words
    """
    pass


if __name__ == "__main__":
    assert get_longest_word(["Hello", "Python", "rat"]) == "Python"
    assert sum_of_evens([1, 2, 3, 4]) == 6
    assert truncate_words(["Hello", "Python", "rat"]) == ["Hel", "Pyt", "rat"]
