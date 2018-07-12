
seq = [1, 2, 4, 3, 6, 4, 2, 4, 2, 4]
seq1 = ["apple", "apricot", "peach", "apple"]

def count (sequence, item):
    quan = 0
    for i in sequence:
        if i == item:
            quan += 1



    return quan



print count (seq1, "apple")