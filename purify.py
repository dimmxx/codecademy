seq =[1, 3, 4, 2, 7, 1, 8]

def purify(sequence):
    seq1 = []
    for i in sequence:
        if i % 2 == 0:
            seq1.append(i)
    return seq1

print purify(seq)