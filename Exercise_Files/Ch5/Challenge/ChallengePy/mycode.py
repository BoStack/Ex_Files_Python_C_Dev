
def myfunc(sentence):
    vowels = "AEIOUaeiou"
    plwords = []
    curwords = sentence.split(' ')

    for word in curwords:
        # if the word starts with a vowel just append "way" to the word
        if vowels.find(word[0:1]) != -1:
            plwords.append(word + "way")
        else:
            # find the position of the first vowel
            for i, c in enumerate(word):
                indx = vowels.find(c)
                if indx != -1:
                    prefix = word[0:i]
                    suffix = word[i:]
                    newword = suffix + prefix + "ay"
                    plwords.append(newword)
                    break

    # return all of the words joined into a sentence
    return " ".join(plwords)


promt = input("Enter a string to convert to PigLatin:\n")
name = promt
piglatinstr = myfunc(name)
print("The result is:")
print(piglatinstr)