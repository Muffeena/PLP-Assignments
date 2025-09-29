price = float(input('Enter the original price : '))
discount_percent = float(input('Enter the discount percentage: '))
def calculate_discount(price, discount_percent):
    return price - price * discount_percent/100
if discount_percent < 0:
    print(price)
else:
    print(calculate_discount(price, discount_percent))