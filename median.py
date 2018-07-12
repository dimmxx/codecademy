seq = [7, 3, 1, 4]
print seq

def srt (lst):
    return sorted(lst)

def median (lst):
    lst_m = srt(lst)
    if len(lst) % 2 != 0:
        return lst_m[int((len(lst))/2)]
    elif len(lst) % 2 == 0:
        return float((lst_m[int((len(lst))/2)] + lst_m[int((len(lst))/2) - 1])) / 2

print srt(seq)
print median(seq)