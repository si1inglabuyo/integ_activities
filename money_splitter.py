def money_converter(amount):
    denominations = [1000, 500, 100, 50, 20, 10, 1]
    counts = {}
    for denom in denominations:
        bill_count = amount // denom
        counts[denom] = bill_count
        amount = amount % denom
    
    return counts

#this is the module file I used in denomination_module.py
