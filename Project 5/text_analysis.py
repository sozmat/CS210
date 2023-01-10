import doctest
def get_user_input() -> list:
    """Gets the user's input in the correct format, with multiple lines
    :return:The text in a list format with each line being a unit.
    """
    print('Enter/paste some text (Ctrl-D, Cmd-D or Ctrl-Z (Windows) to end):')
    text_lines = []
    while True:
        try:
            line = input()
        except EOFError:    # detects the Ctrl-D (or Ctrl-Z)
            break
        text_lines.append(line)
    return text_lines

def get_num_words(text_lines: list) -> int:
    """Gives the num of words of the text inputted
    :param text_lines: the inputted text: list
    :return: the number of words of the text: integer

    >>> get_num_words(['Hello my name is Sydney!', 'How about you?'])
    8

    >>> get_num_words([])
    0

    >>> get_num_words(['one two\\n', 'three\\n', 'four'])
    4
    """
    num_words = 0
    for i in range(0,len(text_lines)):
        num_words += len(text_lines[i].split())
    return num_words

def get_num_sentences(text_lines: list) -> int:
    """Calculates the number of sentences per inputted text.
    :param text_lines: list
    :return: number of sentences: int

    >>> get_num_sentences([])
    0

    >>> get_num_sentences(['I really hope this works!', 'Will it?', "Let's see."])
    3

    """
    # count() is the way to go!
    # needs to be applied to each line, not the list of lines, then increment the sentence count
    line = ''
    for el in text_lines:
        line += el
    period = line.count('.')
    exclamation = line.count('!')
    question = line.count('?')
    num_sentences = period + exclamation + question
    return num_sentences

def get_avg_words(num_words: int, num_sentences: int) -> float:
    """Calculates the average word per sentence in the text
    :param num_words: integer
    :param num_sentences: integer
    :return: the average number of words per sentence

    >>> get_avg_words(200, 15)
    13.3

    >>> get_avg_words(50, 4)
    12.5
    """
    avg_words = round((num_words / num_sentences), 1)
    return avg_words

def get_most_used_words(text_lines: list) -> str:
    """Calculates the mode, the most frequenctly occuring word in the text
    :param text_lines: list
    :return: string
    """
    words = []
    for i in range (0, len(text_lines)):
        words += text_lines[i].split()

    count_dict = {}
    for item in words:
        if item in count_dict:
            count_dict[item] = count_dict[item] + 1
        else:
            count_dict[item] = 1

    count_list = count_dict.values()
    max_count = max(count_list)

    mode_list = []
    for item in count_dict:
        if count_dict[item] == max_count:
            mode_list.append(count_dict[item])

    return mode_list

def print_stats(num_words: int, num_sentences: int, avg_words: float, most_freq_word: str):
    """Displays all of our return values from our functions in a table.
    :param num_words: integer
    :param num_sentences: integer
    :param avg_words: float
    :param most_freq_word: string
    :return: A table displaying text analysis data

    >>> print_stats(500, 22, 22.7, 'the')
           Sentence Statistics Table
    ----------------------------------------
    | Number of words        |           500|
    | Number of sentences    |            22|
    | Average words/sentence |          22.7|
    | Most frequent word     |           the|
    ----------------------------------------
    """

    title = "Sentence Statistics Table"
    print(title.center(40))
    first_line = '-'
    print(first_line * 40)
    second_line = '| Number of words        |{:>14}|'
    print(second_line.format(str(num_words)))
    third_line = '| Number of sentences    |{:>14}|'
    print(third_line.format(str(num_sentences)))
    fourth_line = '| Average words/sentence |{:>14}|'
    print(fourth_line.format(str(avg_words)))
    fifth_line = '| Most frequent word     |{:>14}|'
    print(fifth_line.format(str(most_freq_word)))
    sixth_line = '-'
    print(sixth_line * 40)
def main():
    """Driver function: calls other functions to perform all tasks."""
    text_lines = get_user_input()
    num_words = get_num_words(text_lines)
    num_sentences = get_num_sentences(text_lines)
    avg_words = get_avg_words(num_words, num_sentences)
    most_freq_word = get_most_used_words(text_lines)
    print_stats(num_words, num_sentences,avg_words,most_freq_word)

if __name__ == '__main__':
    main()

doctest.testmod()

