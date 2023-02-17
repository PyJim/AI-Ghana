# problem 1
def flatten_lists(list_of_lists):
    """summary

    Args:
        list_of_lists (_list_): a list containing sublists

    Returns:
        list: a sorted list of all sublists flattend
    """
    return sorted([value for sublist in list_of_lists for value in sublist])

# problem 2
def longest_word(line_of_text):
    """_summary_

    Args:
        line_of_text (str): a line of texts

    Returns:
        str: the longest word in the line of texts
    """
    longest_word_length = 0
    for text in line_of_text.split(" "):
        if len(text)>longest_word_length:
            longest_word = text
    return longest_word

# problem 3
def dictionarize(list_of_items):
    """summary

    Args:
        list_of_items (list): list of items
    
    Returns: dictionary with list items as keys and the number of items as values
    """
    dictionary = {}
    for item in list_of_items:
        dictionary[item] = list_of_items.count(item)
    return dictionary
