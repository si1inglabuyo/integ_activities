months = ("January", "February", "March", "April", "May", "June",\
         "July", "August", "September", "October", "November", "December")

days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
reserved_dates = []

def validate_input(month, day):
    if 1 <= month <= 12:
        if 1 <= day <= days_in_month[month - 1]:
            return True
        
    return False

def print_reserved_dates():
    if reserved_dates:
        print()
        print("-" * 30)
        print(f"|{'\033[1mReserved Dates:\033[0m':^36}|")
        print("-" * 30)
        for month, day in reserved_dates:
            print(f"|{f'{months[month-1]} {day}, 2023':<28}|")
            print("-" * 30)
    else:
        print("\nNo reservations yet.")

def main():

    import pyfiglet
    import time

    ascii_text = pyfiglet.figlet_format("OASIS   HOTEL", font="standard")
    centered = "\n".join(line.center(95) for line in ascii_text.split("\n"))
    print(centered)
    print(f"\033[1m{'B O O K  Y O U R   R E S E R V A T I O N   N O W!'.center(95)}\033[0m")
    print("-" * 100)

    while True:

        try:
            print("\nPlease Choose from the Choices Below:")
            print("1. Book a Reservation")
            print("2. View Reserved Dates")
            print("3. Exit")
            choice = int(input("\nEnter your choice: "))

            match choice:
                case 1:
                    try:
                        month_code = int(input("Input Month Code: "))
                        day = int(input("Input Desired Day: "))

                        if validate_input(month_code, day):

                            reservation_date = (month_code, day)
                            if reservation_date not in reserved_dates:
                            
                                reserved_dates.append((month_code, day))

                                print("\nBooking Your Reservation", end="", flush=True)

                                for i in range(3):  
                                    time.sleep(0.7)
                                    print(".", end="", flush=True)

                                print(f"\n\nYour Reservation on {months[month_code - 1]} {day}, 2023 Has Been Successfully Booked!")
                               
                            else:
                                print(f"\nSorry, {months[month_code - 1]} {day}, 2023 is Already Booked.\nPlease Choose Another Date.")

                        else:
                            print("\nInvalid Input. Please enter a valid month code/day.")

                    except ValueError:
                        print("\nInvalid Input. Please enter a valid month code/day.")

                case 2:
                    print_reserved_dates()

                case 3:
                    print("\nExiting Program", end="", flush=True)
                    for i in range(3):  
                        time.sleep(0.7)
                        print(".", end="", flush=True)
                    print("\nThanks for using our service!")
                    break
                    
                case _:
                    print("\nInvalid Choice. Please Choose a Valid Option.")
                
        except ValueError:
            print("\nInvalid Input. Please Try Again.")

if __name__ == "__main__":
    main()