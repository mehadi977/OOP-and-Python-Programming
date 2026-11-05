# ---Final Exam----
# Bangladesh Bus Ticket Booking System


# 1 Bus Class
class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

    def available_seats(self):
        return self.total_seats - self.booked_seats

    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            return True
        return False


# 2 Passenger Class
class Passenger:
    def __init__(self, name, phone, bus):
        # bus class er ekte object ashbe
        self.name = name
        self.phone = phone
        self.bus = bus


# 3 BusSystem Class
class BusSystem:
    def __init__(self):
        self.buses = []
        self.passengers = []
        self.fare = 500

    # 5 Add Bus Method
    def add_bus(self, number, route, total_seats):
        for bus in self.buses:
            if bus.number == number:
                print("Bus is Already Exists!")
                return
        bus = Bus(number, route, total_seats)
        self.buses.append(bus)
        print("\nBus Added Successfully")

    # 6 Book Ticket Method
    def book_ticket(self, bus_number, name, phone):
        for bus in self.buses:
            if bus.number == bus_number:
                if bus.book_seat():
                    pasngr = Passenger(name, phone, bus)
                    self.passengers.append(pasngr)
                    print("\nTicket booked Successfully")
                    print(f"Passenger Name: {name}")
                    print(f"Bus NUmber: {bus.number}")
                    print(f"Route: {bus.route}")
                    print(f"Fare: ৳{self.fare} ")
                else:
                    print("No availible sit!")
                return
        print("Bus Not found")

    # 7 View Buses Method
    def show_buses(self):
        print("--All busses here--")
        for bus in self.buses:
            print(
                f"Bus No: {bus.number}\tBus route is: {bus.route}\tTotal avalible sites: {bus.available_seats() } "
            )


# 4 Admin Class
class Admin:
    def __init__(self):
        self.username = "admin"
        self.password = "1234"

    def login(self, user, pas):
        if self.username == user and self.password == pas:
            return True
        else:
            return False

    # def add_bus(self, bus):
    #     pass


bus_system = BusSystem()
admin = Admin()


# 9 User Menu (for everyone)
while True:
    print("\n---Welcome To Bangladesh Bus Ticket Booking System---\n")
    print("Press 1 for Admin Login")
    print("Press 2 for Book Ticket")
    print("Press 3 for View Buses")
    print("Press 4 for Exit\n")
    choise = input("Enter your choice : ")

    if choise == "1":
        # 8 Admin Login (Feature)
        print("\n##Adimn Login##\n")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        # 10 Admin Menu (after successful login)
        if admin.login(username, password):
            print("Login Successfull~\n")
            while True:
                print(f"\nWelcome Admin {username}")
                print("Press 1 for Add Bus. ")
                print("Press 2 for View All Busess. ")
                print("Press 3 for Logout. \n")

                chois = input("Enter your Choise: ")
                if chois == "1":
                    # Add Bus
                    print("Add Bus---->")
                    number = input("Enter Bus Number: ")
                    route = input("Enter Bus Route: ")
                    try:
                        seats = int(input("Enter Total Seats: "))
                        if seats <= 0:
                            print("Seats must greater then 0!")
                        else:
                            bus_system.add_bus(number, route, seats)
                    except ValueError:
                        print("Please Entr valid number!!!")

                elif chois == "2":
                    # View all busess
                    bus_system.show_buses()

                elif chois == "3":
                    break
                else:
                    print("Value not valid!!")

        else:
            print("Invalid Username or Password!")

    elif choise == "2":
        # book ticket
        bus_number = input("Enter Bus Number: ")
        name = input("Enter Passengr Name: ")
        phone = input("Enter Phone Number: ")
        bus_system.book_ticket(bus_number, name, phone)
    elif choise == "3":
        # view busses
        bus_system.show_buses()
    elif choise == "4":
        break
    else:
        print("Value not valid")
