import turtle

def count_smaller(lst: list, item: int) -> int:
    """
    Counts the number of items in a list that are smaller than some value.
    You can assume the list is sorted in ascending order.
    Args:
        lst: list to be searched
        item: item to be searched for
    Returns:
        number of items smaller than item
    
    >>> count_smaller([1, 2, 3, 4, 5, 6, 7], 3)
    2

    >>> count_smaller([8, 9, 10, 11, 12, 13, 14, 15.5], 12)
    4
    """
    num_count = 0
    if lst[num_count] > item - 1:
        return 0
    else:
        num_count + 1
        return 1 + count_smaller(lst[1:], item)

def is_palindrome(s: str) -> bool:
    """
    Recursively checks if a string is a palindrome.
    Args:
        s: string to be checked
    Returns:
        True if string is a palindrome, False otherwise
    
    >>> is_palindrome('12022021')
    True

    >>> is_palindrome('backpack')
    False
    """
    if s[0] != s[-1]:
        return False
    else:
        is_palindrome(s[0:-1])    # slice off both first and last letter
        return True


def avg_word_length(lst: list, length: int = 0, count: int = 0) -> float:
    """
    Recursively finds the average word length in a list of words.
    Args:
        lst: list of words
        length: cumulative length of words (all characters in all words), initially 0
        count: number of words, initially 0
    Returns:
        average word length
    
    >>> avg_word_length(['dog', 'cat', 'top'])
    3.0

    >>> avg_word_length(['fish', 'banana', 'cow', 'exponential'])
    6.0
    """
    if lst == []: 
        return length / count
    else:
        return round(avg_word_length(lst[1:], length + len(lst[0]), count + 1), 2)

def draw_tree(the_turtle: turtle.Turtle, length: int) -> None:
    """
    Draws a tree using recursion and the turtle module.
    Args:
        turtle: turtle object
        length: length of the branch/trunk
    Returns:
        None
    """
    if length < 5:
        return
    else:
        the_turtle.forward(length)
        the_turtle.right(30)
        tree(the_turtle, length - 15)
        the_turtle.left(60)
        tree(the_turtle, length - 15)
        the_turtle.right(30)
        the_turtle.backward(length)


# Generate points Sierpinski triangle using recursion
def sierpinski(the_turtle: turtle.Turtle, points: tuple, degree: int) -> list:
    """
    Generates the points for a Sierpinski triangle using recursion, returning a list of points.
    Args:
        the_turtle: turtle object
        points: tuple of 2-d points (tuples) of initial triangle
        degree: degree of the Sierpinski triangle
    Returns:
        list of all points for the Sierpinski triangle
    """
    # TODO: write your code here
    pass


# ---- You shouldn't have to change anything below this line 
# ---- unless you implemented the optional problems 10.4 and 10.5

def save_png(the_turtle: turtle.Turtle, filename: str) -> None:
    """
    Saves the current image of the turtle as a PNG file.
    Args:
        the_turtle: turtle object
        filename: name of the file to be saved
    Returns:
        None
    """
    from PIL import Image
    import io
    if the_turtle.screen.getcanvas() is not None:
        ps = the_turtle.getscreen().getcanvas().postscript(colormode='color')
        img = Image.open(io.BytesIO(ps.encode('utf-8')))
        try:
            img.save(filename, 'png')
            print(f"Saved image to {filename}")
        except Exception as e:
            print(f"Error: Could not save image in {filename} file: {e}")
    return


def main():
    # Part 10.1
    print('Part 10.1')
    print('Counting smaller items in a list')
    print('5 in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] is', count_smaller([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))

    # Part 10.2
    print('\nPart 10.2')
    print('Recursively check if a string is a palindrome')
    print('racecar is a palindrome:', is_palindrome('racecar'))
    print('racecars is a palindrome:', is_palindrome('racecars'))

    # Part 10.3
    print('\nPart 10.3')
    print('Average word length in a list of words')
    wordlist = ['not', 'a', 'very', 'long', 'word', 'list']
    print(f'avg word length of {wordlist} is', avg_word_length(wordlist))

    
    # Part 10.4
    if True:   # change to True if you implement the optional part 10.4
        print('\nOPTIONAL Part 10.4')
        print('Drawing a tree using recursion and the turtle module')
        yurtle = turtle.Turtle()
        yurtle.penup()
        yurtle.setpos(0,-250)   # move closer to bottom of canvas
        yurtle.pendown()
        yurtle.speed(0)
        yurtle.left(90)         # Tree will grow upwards
        draw_tree(yurtle, 120)
        save_png(yurtle, 'tree.png')   


    # Part 10.5
    if False:    # Change to True if you implement the optional 10.5
        print('\nOPTIONAL Part 10.5')
        print('Generating points for a Sierpinski triangle using recursion')
        yurtle = turtle.Turtle()
        yurtle.speed(0)
        sierpinski(yurtle, points=((-100,-50),(0,100),(100,-50)), degree=3)
        save_png(yurtle, 'sierpinski.png')

if __name__ == '__main__':
    main()

