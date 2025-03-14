
history = []

def user_input():
    try:
        first_number = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        second_number = float(input("Enter the second number: "))
        return first_number, operator, second_number
    except ValueError:
        print("It's wrong entry. Please try one more time.")
        return None

def calculations(first_number, operator, second_number):
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        if second_number == 0:
            return "Error"
        return first_number / second_number
    else: 
        return "Wrong entry"
    
def display_history():
    if not history:
        print("History is empty.")
    else: 
        print("Operations history: ")
        for items in history:
            print(items)

while True:
    user_data = user_input()
    if user_data:
        first_number, operator, second_number = user_data
        result = calculations(first_number, operator, second_number)
        print(f"= {result}")
        history.append(f"{first_number} {operator} {second_number} = {result}")

        choice = input("Continue (y/n), show history (h) or remove history (r)?")
        if choice == 'n':
            break
        elif choice == 'h':
            display_history()
            print(choice)
        elif choice == 'r':
            history.clear()
            display_history()
            

