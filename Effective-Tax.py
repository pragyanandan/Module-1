def calculate_tax(income):
    brackets = [(14000, 0.105), (48000, 0.175), (70000, 0.30), (180000, 0.33)]
    tax = 0
    for i, (limit, rate) in enumerate(brackets):
        if income <= limit:
            tax += income * rate
            break
        else:
            tax += limit * rate
            income -= limit
    else:
        tax += income * 0.39
    return tax

def effective_tax_rate(income):
    tax = calculate_tax(income)
    return tax / income

# Example usage
income = 145000
tax_rate = effective_tax_rate(income)
print("Effective Tax Rate:", tax_rate)
