grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_average(grades_input):
    return float(grades_sum(grades_input))/len(grades_input)

def grades_sum(line):
    total = 0
    for i in line:
        total += i
    return total

print grades_sum(grades)
print grades_average(grades)
print grades_average([4,5,1,0])