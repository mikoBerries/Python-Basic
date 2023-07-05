# other method in python string

# Formatting
# The center() method allows you to place your string 'centered' between a provided string with a certain length.
# Personally, I've never actually used this in code as it seems pretty esoteric...

s = 'hello world'

print(s.center(20,'z')) # -> 'zzzzhello worldzzzzz'

# is check methods
# These various methods below check if the string is some case.
# Let's explore them:

s = 'hello'

# isalnum() will return True if all characters in s are alphanumeric
# isalpha() will return True if all characters in s are alphabetic
# Another method is endswith() which is essentially the same as a boolean check on s[-1]

print(s.isalnum())      # True
print(s.isalpha())      # True
print(s.endswith('o'))  # True


# Built-in Reg. Expressions
# Strings have some built-in methods that can resemble regular expression operations.
# We can use split() to split the string at a certain element and return a list of the results.
# We can /use partition() to return a tuple that includes the first occurrence 
# of the separator sandwiched between the first half and the end half.

print(s.split('e'))        # -> ['h', 'llo']
print(s.partition('l'))    # -> ('he', 'l', 'lo')