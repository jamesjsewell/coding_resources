print("============================")
print("======Factorial Wizard======")
print("============================")

# prompts the user for input, the variable is assigned what the user entered
# expects an integer 
user_number = int(input("Please Input Integer: "))

# =========================================== #
# = BUILDS AN ARRAY OF VALUES STARTING AT 1 = # 
# =   AND ENDING AT USER INPUT NUMBER       = #
# =========================================== #

# this will be assigned the "iteration" number we are on in the for loop
the_index = 0

# defines the array that will be populated with the integer values 1 - user input
numbers_array = []

# iterates through every value from 1 to user input
for the_index in range(1, user_number + 1):
    
    # pushes the current "iteration" of the loop as an integer to 
    # the numbers_array array
    numbers_array.append(the_index)
# =========================================== #
  
# at this point numbers array should be populated like
# [ 1, 2, 3, 4, 5] if the user entered 5 for example

# ------------------------------------------- #  
# the below while loop will iterate from the variable i, which starts out as the user input number
# because it will be assigned the user number once it is defined,
# and will subtract 1 from the variable i every iteration in the loop until the variable i is equal
# to 0, so instead of iterating from 0 up to some number, we are iterating
# backwards from some number down to 1 ( to one because in this case the loop condition is 
# while i is greater than 0 )
# for example if the user entered 5, the loop would go 5, 4, 3, 2, 1

# this is where the results of multiplications will be stored and iterated on
product = 0

# sets i, ( i is short for iteration ) to the value that the user entered
i = user_number

# iterates down from the user input and ends once the variable i is equal to 1
while i > 0:

    # this checks if we are on the first iteration of the loop
    if i == user_number:
        
        # assigns the variable called product the value of the user input,
        # times its preceding number
        # since if it makes it inside of this conditional statement we know that the loop
        # is on the first iteration only
        product = user_number * (i - 1)

    # after the loop has iterated once, this else statement will execute 
    # every iteration until the loop is done
    else:

        # makes sure that the variable is atleast 2 before performing
        # the operation
        if i > 1:

            # this takes the value stored in the variable called product,
            # and multiplies the previous value of product by 
            # the preceding value of the current iteration number. It then stores
            # the newly updated value back into the variable product
            # so that it can be iterated on in the next step of the loop
            # remember that the variable product is defined outside of the loop, 
            # therefore it persists until the program is finished and can be changed
            # to something new at anytime
            product = product * (i - 1)

    # this subtracts 1 from the variable i after everything in the loop is done 
    # on each iteration
    # this is what makes the loop iterate down to 1
    i -= 1
# ------------------------------------------- # 
  
print(product, "product")