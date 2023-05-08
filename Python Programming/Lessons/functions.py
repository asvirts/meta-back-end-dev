def calculate_tax(bill, tax_rate):
    return round(bill * tax_rate / 100.00, 2)


print(calculate_tax(1532.24, 12.00))
