import pyfiglet

def money_converter(amount):
    denominations = [1000, 500, 100, 50, 20, 10, 1]
    counts = {}
    for denom in denominations:
        bill_count = amount // denom
        counts[denom] = bill_count
        amount = amount % denom

    return counts

def converted_value(counts):
    print()
    print("-" * 19)
    print("|  Denominations  |")
    print("-" * 19)
    for denom, count in counts.items():
        print(f"{denom}\t-\t{count}")

def main():
    header = pyfiglet.figlet_format("Money Splitter", font="slant")
    print(header)
    print("-" * 70)

    while(True):
        try:
            amount = int(input("\nEnter the amount of money: Php "))
            if amount <= 0:
                print("\nPlease enter a non-zero / positive number")
            else:
                bill_counts = money_converter(amount)
                converted_value(bill_counts)

            while(True):
                try:
                    choice = input("\nDo you want to convert bill again? (Y/N) ").strip().upper()
                    if not choice:  
                        raise ValueError("Empty input")
                    if choice not in ('Y', 'N'):
                        raise ValueError(f"'{choice}' is not a valid choice")
                        
                    if choice == 'Y':
                        break
                    elif choice == 'N':
                        print("\nThank you for using Money Splitter!")
                        return

                except Exception as e:
                    print(f"\n{e}. Please enter a valid choice (Y/N).")

        except ValueError:
            print("\nInvalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()

