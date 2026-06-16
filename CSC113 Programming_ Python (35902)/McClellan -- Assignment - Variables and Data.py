#MPH Caculator
miles = int(input('How many MILES did you drive? '))
gallons = int(input('How GALLONS of GAS did you use? '))

print('You drove', miles/gallons, 'MPH average\n')

#Total Purchase
price1 = int(input("What's the price of the Carrets? "))
price2 = int(input("What's the price of the Computer? "))
price3 = int(input("What's the price of the Car? "))
price4 = int(input("What's the price of that Cat? "))
price5 = int(input("What's the price of the Caculator? "))

pricet= price1+price2+price3+price4+price5
tax = pricet*0.07
total = tax+pricet

print("The price (minuse tax) is ${}".format(pricet))
print("The tax is ${}".format(tax))
print("The total price is ${}\n".format(total))

#Tip, Tax, and Total
food_price = int(input("What's the price of the food? "))

tax = food_price*0.07
print(tax)
tip = food_price*0.18
print(tip)
total = tax+tip+food_price

print("The price (minuse tax) is ${}".format(pricet))
print("The tax is ${}".format(tax))
print("Your tip is ${}".format(tip))
print("The total price is of dinner is ${}".format(total))