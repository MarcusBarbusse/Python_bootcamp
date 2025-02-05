def text_analyser(*args):
    """
        This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.
    """
    if len(args) == 0:
        print("What is the text to analyse?")
        str = input("-->")
    elif x != 0:
        str = args[0]
    x = len(str)
    y = 0
    upper = 0
    lower = 0
    punc = 0
    digit = 0
    space = 0
    while y < x:
        if str[y].isupper() is True:
            upper += 1
        elif str[y].islower() is True:
            lower += 1
        elif str[y].isspace() is True:
            space += 1
        elif str[y].isdigit() is True:
            digit += 1
        y += 1
    print("The text contains", x, "characters:\n")
    print("_", upper, "upper letters\n")
    print("_", lower, "lower letters\n")
    print("_", (x - upper - lower - digit - space), "punctuation marks\n")
    print("_", space, "spaces")