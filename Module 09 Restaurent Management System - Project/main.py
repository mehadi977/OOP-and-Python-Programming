from food_item import FoodItem
from menu import Menu
from users import Customer, Admin, Employee
from orders import Order
from restaurent import Restaurent

mamr_res = Restaurent("Mamar restaurent")


def customer_menu():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    phone = input("Enter Your Phone: ")
    address = input("Enter Your Address: ")
    customer = Customer(
        name=name,
        phone=phone,
        email=email,
        address=address,
    )

    while True:
        print(f"Welcome {customer.name}!!!")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            customer.view_menu(mamr_res)
        elif choice == 2:
            item_name = input("Enter item name: ")
            item_quantity = int(input("Enter item quantity: "))
            customer.add_to_cart(mamr_res, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("value not valid")


def admin_menu():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    phone = input("Enter Your Phone: ")
    address = input("Enter Your Address: ")
    admin = Admin(name=name, phone=phone, email=email, address=address)

    while True:
        print(f"Welcome {admin.name}!!!")
        print("1. Add new Item")
        print("2. Add new Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete Items")
        print("6. Exit")

        choice = int(input("Enter Your Choice: "))
        # Add new Item
        if choice == 1:
            # item_name
            name = input("Enter Item name: ")
            price = int(input("Enter Item Price: "))
            quantity = int(input("Enter Item Quantity: "))
            item = FoodItem(name, price, quantity)
            admin.add_new_item(mamr_res, item)

        # Add new Employee
        elif choice == 2:
            employee_name = input("Enter Employee Name: ")
            employee_phone = input("Enter Employee Phone: ")
            employee_email = input("Enter Employee Email: ")
            employee_address = input("Enter Employee Address: ")
            employee_age = input("Enter Employee Age: ")
            employee_designation = input("Enter Employee Designation: ")
            employee_selary = input("Enter Employee Selary: ")

            employee = Employee(
                employee_name,
                employee_phone,
                employee_email,
                employee_address,
                employee_age,
                employee_designation,
                employee_selary,
            )
            admin.add_employees(mamr_res, employee)

        # View Employee
        elif choice == 3:
            admin.view_employee(mamr_res)

        # View Items
        elif choice == 4:
            admin.view_menu(mamr_res)

        # Delete Items
        elif choice == 5:
            item_name = input("Enter Item Name: ")
            admin.delete_item(mamr_res, item_name)

        # Exit
        elif choice == 6:
            break

        else:
            print("value not valid")


while True:
    print("---Welcome---")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break

    else:
        print("Invalid Input!!")
