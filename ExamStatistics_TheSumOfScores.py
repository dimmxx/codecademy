grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(line):
    total = 0
    for i in line:
        print i
        total += i
    return total

print grades_sum(grades)