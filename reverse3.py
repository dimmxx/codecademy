def reverse(word):
    rword = ""
    for i in range(len(word) - 1, -1, -1):
       rword += word[i]
    return rword

print reverse("Python!")


