grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_average(grades_input):
    return float(grades_sum(grades_input))/len(grades_input)

def grades_sum(line):
    total = 0
    for i in line:
        total += i
    return total

def grades_variance(score):
    variance = 0
    for i in score:
       variance += (grades_average(score) - i) ** 2
    return variance/len(score)

def grades_std_deviation(variance):
    return variance ** 0.5

print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(grades_variance(grades))