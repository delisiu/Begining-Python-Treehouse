def disemvowel(word):
    newword=list(word)
    vowels = ('a', 'e', 'i', 'o', 'u')
    for i in word:
        if i.lower() in vowels:
            newword.remove(i)
    word=("".join(newword))
    print(word)
    return word

disemvowel("LMpAXiNjg")
