#moneyInMywallet = 100.
#while moneyInMywallet >= 0:
        #drinkname = input("I will buy a drink, what do you want? ")
        #drinkprice = float(input("How much is it: "))
        #if drinkprice <= moneyInMywallet:
            #moneyInMywallet -= 7.5
            #print ("Here is your ", drinkname, "Enjoy")
        #else:
            #print ("Sorry, I can't afford anymore, let's go.")
           # break

#print ("I left the pub, the money left is: ", moneyInMywallet)

#largest_number = -999999999
#number = int(input("Enter a number or type -1 to stop: "))
#while number != -1:
    #if number > largest_number:
        #largest_number = number
    #number = int(input("Enter a number os type -1 to stop: "))

#print ("The largest number is: ", largest_number)

#secret_number = 777
#print(
#"""
#+================================+
#| Welcome to my game, muggle!    |
#| Enter an integer number        |
#| and guess what number I've     |
#| picked for you.                |
#| So, what is the secret number? |
#+================================+
#""")
#numberguess = int(input("Guess the secret number: "))

#while numberguess != secret_number:
    #print ("Ha ha! You're stuck in my loop!")
    #numberguess = int(input("Try again, guess the number: "))
#else: 
    #print ("Well done, muggle! You are free now.")

#power = 1
#for expo in range(16):
    #print("2 to the power of", expo, "is", power)
    #power *= 2



# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)

# Write a print function with the final message.

import time
i = 3

for i in range(1 , 6):
    print (i , "mississippi")
    time.sleep(3)
print ("Here I come!")
