# material prices
print("---------------")
print("|  MATERIALS  |")
print("---------------")
print("Enter the Cost of the Following:")
paper_price = float(input(f"{'Paper':<10}: "))
pencil_price = float(input(f"{'Pencil':<10}: "))
scissor_price = float(input(f"{'Scissor':<10}: "))
eraser_price = float(input(f"{'Eraser':<10}: "))

# material units
print("\n--------------")
print("|  PURCHASE  |")
print("--------------")
print("How many items of the following did you bought?")
paper_unit = int(input(f"{'Paper':<10}: "))
pencil_unit = int(input(f"{'Pencil':<10}: "))
scissor_unit = int(input(f"{'Scissor':<10}: "))
eraser_unit = int(input(f"{'Eraser':<10}: "))

# total units calculation
material_units = paper_unit + scissor_unit +\
              pencil_unit + eraser_unit

# total price calculation
total_price = (paper_price * paper_unit) + (pencil_price * pencil_unit) + \
              (scissor_price * scissor_unit) + (eraser_price * eraser_unit)

# payment input
print(f"\nTotal Amount: ₱ {total_price:.2f}")
payment = float(input("\nEnter Cash: "))

# change calculation
change = payment - total_price

# receipt
print("\n_______________________________________________________________")
print(f"|{'*** Revi and Gab\'s Bookstore ***':^62}|")
print(f"|{'SALES INVOICE':^62}|")
print("|--------------------------------------------------------------|")
print(f"|{'Units Bought':^14}|{'Materials':^14}|{'Price per Unit':^18}|{'Total Price':^13}|")
print("|--------------------------------------------------------------|")
print(f"| {paper_unit:^14}|{'Paper 📰':^12}|₱{paper_price:^17.2f}|₱{paper_price * paper_unit:^12.2f}|")
print(f"| {pencil_unit:^14}|{'Pencil ✏️':^14}|₱{pencil_price:^17.2f}|₱{pencil_price * pencil_unit:^12.2f}|")
print(f"| {scissor_unit:^14}|{'Scissor ✂️':^14}|₱{scissor_price:^17.2f}|₱{scissor_price * scissor_unit:^12.2f}|")
print(f"| {eraser_unit:^14}|{'Eraser 👝':^12}|₱{eraser_price:^17.2f}|₱{eraser_price * eraser_unit:^12.2f}|")
print("|--------------------------------------------------------------|")
print(f"|{' TOTAL':<20}: ₱{total_price:<38.2f} |")
#eraser_unit = int(input(f"{'Eraser':<10}: "))
print(f"|{' CASH':<20}: ₱{payment:<38.2f} |")
print(f"|{' CHANGE':<20}: ₱{change:<38.2f} |")

before_vat = total_price / (1 + 0.12)

print("|                                                              |")
print(f"|{' Price before VAT':<20}: ₱{before_vat:<38.2f} |")
vat = total_price - before_vat
print(f"|{' VAT (12%)':20}: ₱{vat:<38.2f} |")
print(f"|{' Total Items':<20}: {material_units:<39} |")
print("|______________________________________________________________|")
