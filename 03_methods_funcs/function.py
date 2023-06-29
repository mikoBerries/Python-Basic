# function declaration using def some_func():

# define seme function with given param and -> returning somthings
# number name is omitempty with default value
def compute_sompethings(num1 ,num2 ,numbername="something")->None:
    print(f"{numbername} : {num1+num2}")

def check_even_list(num_list):
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we return True
        if number % 2 == 0:
            return True
        # Don't do anything if its not even
        else:
            pass
    # Notice the indentation! This ensures we run through the entire for loop    
    return False

def employee_check(work_hours):
    
    # Set some max value to intially beat, like zero hours
    current_max = 0
    # Set some empty value before the loop
    employee_of_month = ''
    
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    
    # returning a tupels
    return (employee_of_month,current_max)

compute_sompethings(100,2000,numbername="this is new")

print(check_even_list([1,3,4,1,6,1]))

work_hours = [('Abby',100),('Billy',400),('Cassie',800)]
name,hours = employee_check(work_hours)
