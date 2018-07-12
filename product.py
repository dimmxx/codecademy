seq = [2, 4, 2]

def product(sequence):
    pro = 1
    for i in sequence:
        pro *= i

    return pro

print product(seq)