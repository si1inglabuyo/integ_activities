salary_rates = {
    'Instructor 1': (29165, 150),
    'Instructor 2': (31320, 200),
    'Instructor 3': (33843, 250),
    'Assistant Professor 1': (36619, 300),
    'Assistant Professor 2': (39672, 350),
    'Assistant Professor 3': (43030, 400),
    'Assistant Professor 4': (46725, 450),  
}

employee_list = []

def get_valid_input(prompt, valid_options):

    while True:
        value = input(prompt)
        if value in valid_options:
            return value
        else:
            print("\nInvalid option. Please choose a valid input.")

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")

def get_details():
    
    print("\n\033[1mPROVIDE THE FOLLOWING DETAILS\033[0m")
    print("-" * 30)
    name = input("Name: ")
    age = get_valid_int("Age: ")
    gender = get_valid_input("Gender: ", {"Female", "Male"})
    civil = get_valid_input("Civil Status: ", {"Single", "Married"})
    college = input("College: ")
    position = get_valid_input("Position: ", salary_rates.keys())
    hours_worked = get_valid_int("Hours Worked: ")

    return {
        'name': name,
        'age': age,
        'gender': gender,
        'civil_status': civil,
        'college': college,
        'position': position,
        'hours_worked': hours_worked  
    }

def calculate_gross_salary(employee):

    regular_salary, rate_per_hour = salary_rates.get(employee['position'], (0,0))
    gross_salary = regular_salary + (rate_per_hour * employee['hours_worked'])
    return gross_salary

def summary_details():

    total_employees = len(employee_list)
    male_employees = sum(1 for emp in employee_list if emp['gender'].lower() == 'male')
    female_employees = sum(1 for emp in employee_list if emp['gender'].lower() == 'female')
    single_employees = sum(1 for emp in employee_list if emp['civil_status'].lower() == 'single')
    married_employees = sum(1 for emp in employee_list if emp['civil_status'].lower() == 'married')
    total_salaries = sum(emp['gross_salary'] for emp in employee_list)

    column_width = 34
    print("\n\033[1mS U M M A R Y   D E T A I L S\033[0m")
    print("-" * column_width)
    print(f"| {'Total Employees':20}|{total_employees:^10}|")
    print("-" * column_width)
    print(f"| {'Male Employees':<20}|{male_employees:^10}|")
    print("-" * column_width)
    print(f"| {'Female Employees':<20}|{female_employees:^10}|")
    print("-" * column_width)
    print(f"| {'Single Employees':<20}|{single_employees:^10}|")
    print("-" * column_width)
    print(f"| {'Married Employees':<20}|{married_employees:^10}|")
    print("-" * column_width)

    print(f"\nTotal Accumulated Salaries of all Employees: Php {total_salaries:,.2f}")
    
def main():

    while True:
        employee = get_details()
        employee['gross_salary'] = calculate_gross_salary(employee)
        employee_list.append(employee)

        print(f"\nTotal Monthly Gross Salary: Php {employee['gross_salary']:,.2f}")

        repeat = input("\nEnter another [Y/N]? ")
        while repeat not in ("Y", "N"):
            repeat = input("Invalid input. Please enter Y or N: ")

        if repeat == "N":
            break  

    summary_details()

if __name__ == "__main__":
    main()
