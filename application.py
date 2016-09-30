import sys
articles = {}
fulltotal = 0
def enter_products():
    box = True
    while box == True:
        option = raw_input("You want to enter a product Yes / No: ")
        try:
            if option.isalpha() == True:
                if option.lower() == "yes":
                    product = raw_input("Enter the product: ")
                    price = int(raw_input("Enter the price: "))
                    articles[product] = price
                elif option.lower() == "no":
                    box = False
                else:
                    print"Data not recognized"
            else:
                print"The numeric data is not recognized"
        except:
            box = True
    print"Your existing items are: "
    for key in articles:
        print key, ":", articles[key]
def purchases():
	if len(articles) > 0:
	    box_2 = True
	    total = 0
	    while box_2 == True:
	        for key in articles:
	        	print key, ":", articles[key]
	        product = raw_input("Which products must bear?")
	        for element in articles:
	            if element == product:
	                print"You choose %s" % (element)
	                quantity = input("Who wanted quantity?")
	                amount = quantity * articles[element]
	                total = total + amount
	                print"Product: %s, Quantity: %s, Subtotal invoice: Q.%s " %(element, amount, total)
	                turn = True
	                while turn == True:
	                    keep = raw_input("You want to choose another article Yes / No: ")
	                    if keep.lower() == "yes":
	                        box_2 = True
	                        turn = False
	                    elif keep.lower() == "no":
	                        box_2 = False
	                        turn = False
	                        return total
	                    else:
	                        print"Option invalidates"
	                        turn = True
	else:
		print"No existing products"
def bill():
    box_2 = True
    while box_2 == True:
        print"1)Gold"
        print"2)Silver"
        print"3)Any"
        card = raw_input("What kind of card do you have?")
        try:
            if card.isalpha() == False:
                if card == "1":
					print"Gold"
					print"The customer has a discount 5%:"
					print"The subtotal of the invoice is Q.%s" %(fulltotal)
					IVA = (fulltotal * 0.12)
					discount = (fulltotal * 0.05)
					totaltotal = fulltotal + IVA - discount
					print"Debit: %s" %(fulltotal)
					print"________________________________________"
					customer_name = raw_input("Customer name: ")
					nit = raw_input("NIT: ")
					cash = input("Cash:  ")
					exchange = cash - fulltotal
					print"________________________________________"
					print("Price        %.2f\t") % fulltotal
					print("IVA          %.2f\t") % IVA
					print("Total        %.2f\t") % totaltotal
					print("Cash         %.2f\t") % cash
					print"________________________________________"
					print"Exchange:   %s" %(exchange)
					break
                elif card == "2":
                    print"Silver"
                    print"The customer has a discount 2%:"
                    print"The subtotal of the invoice is Q.%s" %(fulltotal)
                    IVA = (fulltotal * 0.12)
                    discount = (fulltotal * 0.02)
                    totaltotal = fulltotal + IVA - discount
                    print"Debit: ", totaltotal
                    print("________________________________________")
                    customer_name = raw_input("Customer name: ")
                    nit = raw_input("NIT: ")
                    cash = input("Cash:  ")
                    exchange = cash - totaltotal
                    print("________________________________________")
                    print("Price        %.2f\t") % fulltotal
                    print("IVA          %.2f\t") % IVA
                    print("Total        %.2f\t") % totaltotal
                    print("Cash         %.2f\t") % cash
                    print("________________________________________")
                    print("Exchange:   "), exchange
                    box_2 = False
                elif card == "3":
                    IVA = (fulltotal * 0.12)
                    totaltotal = fulltotal + IVA
                    print"Debit: ", totaltotal
                    print("________________________________________")
                    customer_name = raw_input("Customer name: ")
                    nit = raw_input("NIT: ")
                    cash = input("Cash:  ")
                    exchange = cash - totaltotal
                    print("________________________________________")
                    print("Price        %.2f\t") % fulltotal
                    print("IVA          %.2f\t") % IVA
                    print("Total        %.2f\t") % totaltotal
                    print("Cash         %.2f\t") % cash
                    print("________________________________________")
                    print("Exchange:   "), exchange
                    box_2 = False
                else:
                    print"Option invalidates"
            else:
                print"Only numbers are accepted"
        except:
            option2 = True
	print"Thanks for your purchase. Come back soon."
leave = False
while leave == False:
    print"Register Machine"
    print"What do you want to perform?"
    print"1.)Login products"
    print"2.)Purchases"
    print"3.)Bill"
    primenu = raw_input("Enter number of menu: ")
    try:
	    if primenu.isalpha()==False:
		    if primenu =="1":
		        enter_products()
		        optionmenu = raw_input("Do you want to return to the menu Yes / No: ")
		        if optionmenu.lower() == "yes":
		        	leave = False
		        else:
		            break
		    elif primenu == "2":
		        fulltotal = purchases()
		        print fulltotal
		        optionmenu = raw_input("Do you want to return to the menu Yes / No: ")
		        if optionmenu.lower() == "yes":
		            leave = False
		        else:
		            break
		    elif primenu == "3":
		        print bill()
		        optionmenu = raw_input("Do you want to return to the menu Yes / No: ")
		        if optionmenu.lower() == "yes":
		            leave = False
		        else:
		            break
    except:
		print""
