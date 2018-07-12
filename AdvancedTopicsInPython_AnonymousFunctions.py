
my_list = range(16)
print my_list
print filter(lambda x: x % 3 == 0, my_list)



def by_three(x):
  return x % 3 == 0

print by_three(9)



languages = ["HTML", "JavaScript", "Python", "Ruby"]

print filter(lambda item: item == "Python", languages)


cubes = [x ** 3 for x in range(1, 11)]
filter(lambda x: x % 3 == 0, cubes)
print cubes
print filter(lambda x: x % 3 == 0, cubes)

squares = [x **2 for x in range(1, 11)]
print squares
print filter (lambda x: x >= 30 and x <= 70, squares)