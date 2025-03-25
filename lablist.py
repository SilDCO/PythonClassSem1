numbers = [1,2,3,4,5]
numbers[2] = int(input("Choose a number: "))

del numbers[4]

print ("How many numbers do you have? ", len(numbers))
print ("List of numbers:", numbers)