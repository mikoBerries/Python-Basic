# re - regular expresion

text = "The person's phone number is 408-555-1234. Call phone soon!"
print('phone' in text)

print()

import re
pattern ='phone'
print(re.search(pattern,text))
result = re.search(pattern,text)
# where index matched given pattern ?
print(result.span())
# starting index?
print(result.start())
# end index ?
print(result.end())

# re.search just returning 1 matches pattern and return

# re.findall() getting all pattenr given
print(re.findall(pattern,text))
matches = re.findall(pattern,text)
# mathces are list object of match
print(matches)
# checking how many mached word in text
print(len(matches))

# generator function
for m in re.finditer(pattern,text):
    print(m)
    m.group() #get matches given pattren

print()

# building regex expressions
# r'mypattern'

# Character	Description	Example Pattern Code	Exammple Match
# \d	    A digit	            file_\d\d	    file_25
# \w	    Alphanumeric	    \w-\w\w\w	    A-b_1
# \s	    White space	        a\sb\sc	        a b c
# \D	    A non digit	        \D\D\D	        ABC
# \W	    Non-alphanumeric	\W\W\W\W\W	    *-+=)
# \S	    Non-whitespace	    \S\S\S\S	    Yoyo

target_text = "My telephone number is 408-555-1234"

# sample usage #1
print('using manual regex:')
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',target_text)
print(phone.group())

# Quantifiers we can use them along with quantifiers to define how many we expect.
# Character	Description	                Example Pattern Code	Exammple Match
# +	        Occurs one or more times	Version \w-\w+          Version A-b1_1
# {3}	    Occurs exactly 3 times	    \D{3}	                 abc
# {2,4}	    Occurs 2 to 4 times	        \d{2,4}	                123
# {3,}	    Occurs 3 or more	        \w{3,}	                anycharacters
# \*	    Occurs zero or more times	A\*B\*C*	            AAACC
# ?	        Once or none	            plurals?	            plural

# re write sample usage #1 with Quantifiers
print('Quantifiers:')
phone = re.search(r'\d{3}-\d{3}-\d{4}',target_text)
print(phone.group())

# using pattern compiler
# result can be easyly indexed match by group

# (\d{3}) -> as group by ()
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,target_text)
# grab everything
print(results.group())
# grab by grouping from matcher start with 1 not 0
print(results.group(1))
print(results.group(2))
print(results.group(3))


# searching man/woman 
print(re.search(r"man|woman","This man was here."))

# wild card operator grabping something before at one char
print(re.findall(r".at","The bat went splat")) # ['bat', 'lat']
# grabping 2 char before at finded
print(re.findall(r"..at","The bat went splat")) # ['e bat', 'splat']

# One or more non-whitespace that ends with 'at'
print(re.findall(r'\S+at',"The bat went splat")) # ['bat', 'splat']

# Starts with and Ends With
# We can use the ^ to signal starts with, and the $ to signal ends with:

# Ends with a number
print(re.findall(r'\d$','This ends with a number 2'))  # ['2']

# Starts with a number
print(re.findall(r'^\d','1 is the loneliest number.')) # ['1']

# Exclusion¶
# To exclude characters, we can use the ^ symbol in conjunction with a set of brackets [].
#  Anything inside the brackets is excluded. For example:

phrase = "there are 3 numbers 34 inside 5 this sentence."
print(re.findall(r'[^\d]',phrase))


test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
# removing ! . ? and white space
print(re.findall('[^!.? ]+',test_phrase))

# finding with 2 groups
text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
print(re.findall(r'[\w]+-[\w]+',text))


# Find words that start with cat and end with one of these options: 'fish','nap', or 'claw'
text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"
# eaither cat + (fish/nap/claw)
print(re.search(r'cat(fish|nap|claw)',text))
print(re.search(r'cat(fish|nap|claw)',texttwo))
print(re.search(r'cat(fish|nap|claw)',textthree))