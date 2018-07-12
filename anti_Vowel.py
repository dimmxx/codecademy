vowel_list = ['e', 'u', 'o', 'i', 'a', 'y']

def anti_vowel (text):
    avowel = ""
    for letter in text:
        for i in vowel_list:
            if letter == i or letter == i.upper():
                letter = ""
                break

        avowel += letter


    return avowel

print anti_vowel("Envy")