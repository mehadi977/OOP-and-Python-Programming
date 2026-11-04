# Customer
# Employee
# Admin

from abc import ABC
from orders import Order


class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        super().__init__()


class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item quantity exceeded")
            else:
                item.quantity = quantity  # cart e add kora hobe
                self.cart.add_item(item)
                print("item added")
        else:
            print("item not found")

    def view_cart(self):
        print("~~~View Cart~~~")
        print("Nome\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price: {self.cart.total_price}")

    def pay_bill(self):
        print(f'Total{self.cart.total_price} paid successfully :)')
        self.cart.clear()
    


class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, selary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.selary = selary


# emp =Employee('Rahim',9939,'rahm@gmail.com','Dhaka',22,'Chef',21000)
# print(emp.name)
class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.employees = []  # eta hocche database

    def add_employees(self, restaurent, employee):
        restaurent.add_employees(employee)

    def view_employee(self, restaurent):
        restaurent.view_employee()

    def add_new_item(self, restaurent, item):
        restaurent.menu.add_menu_item(item)

    def delete_item(self, restaurent, item):
        restaurent.menu.remove_item(item)

    def view_menu(self,restaurent):
        restaurent.menu.show_menu()


class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


# ad = Admin("korim", 324234, "kor@gmil.com", "Dhaka")
# ad.add_employees("Sagor", "s@gmil.com", "24243", "Dhaka", 35, "chef", 12000)
# ad.view_employ()

# mamar_res = Restaurent("Mamar Restaurent")
# mn = Menu()
# item = FoodItem("Pizza", 80.50, 15)
# item2 = FoodItem("Burger", 22, 90)
# admim = Admin("Admn", 9249284, "ad@gmail.com", "Dhaka")
# admim.add_new_item(mamar_res, item)
# admim.add_new_item(mamar_res, item2)
# # admim.show_menu()


# customer1 = Customer("Rahim", 343424, "rhm@gmail.com", "Dhaka")
# customer1.view_menu(mamar_res)

# item_name = input("Enter item Name: ")
# item_quantity = int(input("Enter item Quantit: "))
# customer1.add_to_cart(mamar_res, item_name, item_quantity)
# customer1.view_cart()
