import pyfiglet
import money_splitter as mon_split

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
                bill_counts = mon_split.money_converter(amount)
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

