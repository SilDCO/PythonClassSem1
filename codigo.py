#prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
#prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
#prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.

plantName = input("Enter with the plant name:")

if plantName == "Spathiphyllum":
        print("Yes - Spathiphyllum is the best plant ever!")
elif plantName == "spathiphyllum":
        print("No, I want a big Spathiphyllum!")
else:
        print ("No Spathiphyllum! Not " + plantName + "!")





