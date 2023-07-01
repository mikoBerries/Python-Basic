# Map Function
def square (num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square,my_nums):
    print(item)

result = list(map(square,my_nums))
print(result)


# Filter function
def check_even(num):
    return num%2 ==0

check_this=[1,2,3,4,5,6,7,8]

filtered_list = list(filter(check_even,check_this))

print(filtered_list)

for n in filter(check_even,check_this):
    print(n)

# lambda exprexion or anonymous function like go 
# to fill simple small function in map/filter 

# this lambda function to sqoare number
# can be stored 
my_lambda = lambda number:number**2
print(list(map(my_lambda,my_nums)))
# same result
print(list(map(lambda n : n**2 ,my_nums)))