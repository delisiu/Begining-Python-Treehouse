def word_count(tense):
    count = dict()
    tense=tense.split()
    for word in tense:
        word1=word.lower()
        if word1 in count:
            count[word1] += 1
        else:
            count[word1] = 1
    for x, y in count.items():
        print(x, y)
    return count
word_count("I do not like it Sam I Am")
