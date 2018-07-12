
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l
print l[2:9:2]

to_five = ['A', 'B', 'C', 'D', 'E']

print to_five[3:]
# prints ['D', 'E']

print to_five[:2]
# prints ['A', 'B']

print to_five[::2]
# print ['A', 'C', 'E']

my_list = range(1, 11)
print my_list[::2]

backwards = my_list
print backwards[::-1]

to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens


to_21 = range(1, 22)
print to_21

odds = to_21[::2]
print odds

middle_third = to_21[7:14]
print middle_third

