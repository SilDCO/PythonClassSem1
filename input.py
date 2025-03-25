numerbooks = 3

while numerbooks >= 3:
        numerbooks = int(input("Please enter the number of books: "))
        pricebooks = float(input("Please enter the price of the books: "))
        if numerbooks >=3:
            pricebooks = pricebooks * 0.15
            if pricebooks > 50:
            pricebooks = pricebooks - 5
        print ("The final price is: ", pricebooks)
        print ("You have earned: 15% bulk discount and 5% promotion discount")
        else:
            print ("The final price is: ", pricebooks)
            print("You have earned: No discounts or promotions.")
        break




#while moneyInMywallet >= 0:
        #drinkname = input("I will buy a drink, what do you want? ")
        #drinkprice = float(input("How much is it: "))
        #if drinkprice <= moneyInMywallet:
            #moneyInMywallet -= 7.5
            #print ("Here is your ", drinkname, "Enjoy")
        #else:
            #print ("Sorry, I can't afford anymore, let's go.")
           # break