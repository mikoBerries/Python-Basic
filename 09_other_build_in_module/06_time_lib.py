# time module for timing our code 
import time

def func_one(n):
    '''
    Given a number n, returns a list of string integers
    ['0','1','2',...'n]
    '''
    return [str(num) for num in range(n)]

def func_two(n):
    '''
    Given a number n, returns a list of string integers
    ['0','1','2',...'n]
    '''
    return list(map(str,range(n)))


# STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result = func_one(1000000)
# Step 3: Calculate total time elapsed
end_time = time.time() - start_time

# efective for large block code
print(f"start: {start_time}")
print(f"start: {end_time}")

# timeit module to testing 
# for given function IN string (more detailed)
import timeit

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
stmt = 'func_one(100)'

result =timeit.timeit(stmt,setup,number=100000) # running 100000 times to test it to ge avg times of it 

print(f"result :{result}")

# setup are given function in string 
setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''
# what stmt to call setup?
stmt2 = 'func_two(100)'

result2 = timeit.timeit(stmt2,setup2,number=100000)

print(f"result :{result2}")
