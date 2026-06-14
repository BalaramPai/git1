def calculate_total(cart_items):
    total = 0
    for i in cart_items:
        # if i["qty"]<0:
        #     return -1
        if i["price"]<0:
            return -1
        total += (i["price"] * i["qty"])
    
    #If the price is entered in negative or qty is entered in negative    
    if total<0:
        return -1
    
    return total


def apply_coupon(total, coupon_code):
    #If by chance total entered is less that 0.
    if total<0:
        return -1
    values = {
        f"SAVE{i}":i/100 for i in range(10,110,10)
    }
    #Here if any wrong coupone code is entered then it wont be detected , it will return same total.
    if not coupon_code:
        return total
    else:
        if coupon_code.upper() in values:
            total = total - values[coupon_code.upper()]*total
        
    return total


def shipping_charge(total):
    #If anything more that 1000 in cart.
    if total>=1000:
        return total
    #If nothing in cart.
    elif total == 0:
        return 0
    #If something less that 1000 in cart.
    else:
        return total+1000
    
def final_bill(cart_items, coupon_code):
    c_value = calculate_total(cart_items)
    if c_value == -1:
        return "Invalid Data cannot calculate bill."
    cart_value = c_value
    
    a_value = apply_coupon(cart_value,coupon_code)
    if a_value == -1:
        return "Invalid Data cannot calculate bill."
    cart_after_discount = a_value

    final_cost = shipping_charge(cart_after_discount)
    
    return final_cost
    

    
    

  