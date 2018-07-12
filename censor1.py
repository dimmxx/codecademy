def censor(text, word):
    str_i =  text.split(" ")

    for i in range (0, len(str_i)):
        if str_i[i] == word:
            str_i[i] = "*" * len(word)

    return " ".join(str_i)

print censor("Hello world world the the the life is beautiful money go to home", "money")