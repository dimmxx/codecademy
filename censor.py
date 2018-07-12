def censor(text, word):
    str_i =  text.find(word)
    str_i2 = text[0 : str_i] + "*" * len(word) + text[str_i + len(word) : len(text)]
    return str_i2

print censor("Hello world world the life is beautiful", "world")