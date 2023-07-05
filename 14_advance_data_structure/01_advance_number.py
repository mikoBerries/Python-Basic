# other method in python numbers
# Hexadecimal
# Using the function hex() you can convert numbers into a hexadecimal format:

print(hex(246)) # -> '0xf6'
print(hex(512)) # -> '0x200'

# Binary
# Using the function bin() you can convert numbers into their binary format.
bin(1234)   # '0b10011010010'
bin(128)    # '0b10000000'
bin(512)    # '0b1000000000'


# Exponentials
# The function pow() takes two arguments, equivalent to x^y.
# With three arguments it is equivalent to (x^y)%z, but may be more efficient for long integers.

pow(3,4)    # 81
pow(3,4,5)  # 1

# Absolute Value
# The function abs() returns the absolute value of a number.
# The argument may be an integer or a floating point number. If the argument is a complex number, its magnitude is returned.

abs(-3.14)  # 3.14
abs(3)      # 3

# Round
# The function round() will round a number to a given precision in decimal digits (default 0 digits).
#  It does not convert integers to floats.

round(3,2)              #3
round(395,-2)           #400
round(3.1415926535,2)   #3.14