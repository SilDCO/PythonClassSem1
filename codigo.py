#prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
#prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
#prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.

"""plantName = input("Enter with the plant name:")

if plantName == "Spathiphyllum":
        print("Yes - Spathiphyllum is the best plant ever!")
elif plantName == "spathiphyllum":
        print("No, I want a big Spathiphyllum!")
else:
        print ("No Spathiphyllum! Not " + plantName + "!")"""


#if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was the so-called tax relief)
#if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.

income = float(input("Enter the annual income: "))

if income <= 85_528:
    tax = income*.18 - 556.02
else: 
    tax = (income-85_528)*.32+14_439.02
if tax < 0:
    tax= 0.0
tax = round(tax,0)
print("The tax is:", tax, "thalers")

