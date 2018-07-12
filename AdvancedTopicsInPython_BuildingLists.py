
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

doubles = [x * 2 for x in range(1, 6)]
print doubles

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
print doubles_by_3

even_squares = [i ** 2 for i in range(2, 11) if (i ** 2) % 2 == 0]
print even_squares

c = ['C' for x in range(5) if x < 3]
print c