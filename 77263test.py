numerbooks = int(input("Please enter the number of books: "))
pricebooks = float(input("Please enter the price of the books: "))

pricebooks = pricebooks * numerbooks

if numerbooks >=3:
    pricebooks = pricebooks * 0.15
    if pricebooks > 50:
        pricebooks = pricebooks - 5
        print ("The final price is: ", pricebooks)
        print ("You have earned: 15% bulk discount and 5% promotion discount")
    else:
        print ("The final price is: ", pricebooks)
        print ("You have earned: No discounts or promotions.")

        

      
