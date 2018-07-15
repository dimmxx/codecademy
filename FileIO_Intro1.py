my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

# Add your code below!

for i in my_list:
  my_file.write(str(i) + "\n")

my_file.close()

my_file = open("output.txt", "r")

#print my_file.read()

print my_file.readline()
my_file.close()
