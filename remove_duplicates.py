seq = [1, 1, 2]
seq_m = []

def remove_duplicates(sequence):
     if sequence == []:
         return []

     seq_m.append(sequence[0])
     for i in range (1, len(sequence), 1):
         compare_add(sequence[i])
     return seq_m

def compare_add(a):
    for i1 in seq_m:
        if a == i1:
            return
        else:
            continue
    seq_m.append(a)
    return

print remove_duplicates(seq)