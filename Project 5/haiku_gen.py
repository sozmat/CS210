# Implement your solutions here. Remember to follow 210 Style and PEP8.
# Do not forget to click SUBMIT -- you can submit multiple times without penalty.
#
# Include docstrings for all functions. Feel free to delete these comments.
# NO DOCTESTS needed for this problem!



from random import randint
word_dict = {
    'l1-adjective': ["Enchanting", "Amazing", "Colourful",
                     "Delightful", "Delicate", "Scary"],
    'l1-noun': ["visions", "distance", "conscience", "process", "chaos"],
    'l2-adjective': ["superstitious", "contrasting", "graceful", "haunting", "inviting", "contradicting",
                     "overwhelming"],
    'l2-adjective2': ["true", "dark", "cold", "warm", "great", "grim"],
    'l2-noun': ["scenery", "season", "colours", "lights", "Spring", "Winter", "Summer", "Autumn"],
    'l3-adjective': ["undeniable", "beautiful", "irreplaceable", "unbelievable", "irrevocable"],
    'l3-noun': ["inspiration", "imagination", "wisdom", "thoughts"],
}

l1_adj_list = word_dict['l1-adjective']
print(l1_adj_list[randint(0, 5)])


