def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage to apply.

    Returns:
        float: The final price after applying the discount.
    """

    if discount_percent >= 20:
        discount_amount = price * discount_percent / 100
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percent)

print(f"The final price after applying the discount is: {final_price}")