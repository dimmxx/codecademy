def reverse(word):
    rword = []
    for i in range(len(word) - 1, -1, -1):
       rword.append(word[i])
    return rword

def print_str(list):
    word =""
    for i in list:
         word = word + i
    return word

print print_str(reverse("one"))


