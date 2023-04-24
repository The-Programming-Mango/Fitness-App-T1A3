print ("Welcome to the Get Fit! app")

def create_menu():
    print("1. Enter 1 to update your measurements")
    print("2. Enter 2 to view your measurements")
    print("3. Enter 3 to calculate your BMI")
    print("4. Enter 4 to add an excersise")
    print("5. Enter 5 to view previous excersises")
    print("6. Enter 6 to exit")
    choice = input("Enter your selection: ")
    return choice

user_choice = ""

while user_choice != "6":
    user_choice = create_menu()

    if (user_choice == "1"):
        print("Update measurements ")
    elif (user_choice == "2"):
        print("View measurements")
    elif (user_choice == "3"):
        print("Calculate BMI")
    elif (user_choice == "4"):
        print("Add excersise")
    elif (user_choice == "5"):
        print("View excersise history")
    elif (user_choice == "6"):
        continue
    else:
        print("Invalid Input")
        
print("Thank you for using the Get Fit! app")