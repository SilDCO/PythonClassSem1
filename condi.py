#number1 = int(input("Enter the first number: "))
#number2 = int(input("Enter the second number: "))

# Choose the larger number
#if number1 > number2:
    larger_number = number1
#else:
#    larger_number = number2

# Print the result
#print("The larger number is:", larger_number)

largest_number = -999999999
number = int(input("Choose a number: "))

if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
# Go to line 02
