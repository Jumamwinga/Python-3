def calculate_discount (price,discount_percent):
    if discount_percent >= 20:
        final_price = price-(price*(discount_percent/100))
        return final_price
    else:
        return price
    #prompting the user to enter the original price

original_price=float(input("Enter the original price of the item:"))
discount_percent=float(input("Enter the discount percent:"))

    #Calculating the final price

    
final_price=calculate_discount(original_price,discount_percent)

    #Displaying results
if final_price != original_price:
        print ("Final price after discount: Ksh", round(final_price,2))
else:
        print("No discount applied. Original price: Ksh", round (original_price,2))
        

