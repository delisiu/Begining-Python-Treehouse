def sillycase (word):
    word = word.lower()[:(int(len(word)/2))] + word.upper()[(int(len(word)/2)):]
    print (word)
    return word

sillycase("Treehouse")
