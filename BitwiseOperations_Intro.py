print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT00



print bin(1)
for i in range(2, 6):
  print bin(i)


print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print int("11001001", 2)



shift_right = 0b1100
shift_left = 0b1

print shift_right
print shift_left

shift_right = shift_right >> 2
shift_left = shift_left << 2
print shift_right
print shift_left

print bin(shift_right)
print bin(shift_left)


print bin (0b1110 & 0b101)
print bin (0b1110 | 0b101)
print bin (0b1110 ^ 0b101)
print ~1
print ~2
print ~3
print ~42
print ~123



def check_bit4(input):
    if input & 0b1000 > 0:
       return True
    else:
        return False
print check_bit4(0b0011000)




a = 0b10111011
mask = 0b100
desired = a | mask
print bin(desired)


a = 0b11101110
mask = 0b11111111
desired = a ^ mask
print bin(desired)


def flip_bit(number, n):
  mask = (0b1 << (n-1))
  result = number ^ mask
  return bin(result)


print flip_bit(0b100, 2)

