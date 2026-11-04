class Hall:
    def __init__(
        self,
        hall_no,
        row,
        col,
    ):
        self.row = row
        self.col = col
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []

    def enter_show(self, show_id, movie_name, time):
        self.tuple = (show_id, movie_name, time)
        self.show_list.append(self.tuple)
        self.seat_list = []
        for i in range(self.row):
            row = []
            for j in range(self.col):
                row.append("free")
            self.seat_list.append(row)
        self.seats[show_id] = self.seat_list

    def view_show_list(self):
        for i in self.show_list:
            print(f"Show id: {i[0]}\tMovie: {i[1]}\tTime: {i[2]}")

    def view_avalable_seats(self, id):
        if id not in self.seats:
            print("Wrong show id!")
        else:
            for i in self.show_list:
                if i[0] == id:
                    print(f"Movie: {i[1]}\tTime: {i[2]}\n")
            for i in range(self.row):
                for j in range(self.col):
                    if self.seats[id][i][j] == "free":
                        print(f"{chr(i+65)}{j+1}\t", end="")
                    else:
                        print("X\t", end=" ")
                print("\n")

    def book_tickets(self, id, name, phone, booking_seats):
        self.booked_list = []
        flag = 0
        if id not in self.seats:
            print("Wrong show id!")
        else:
            for x in booking_seats:
                r = ord(x[0]) - 65
                c = ord(x[1]) - 49
                if r >= self.row or c >= self.col or r < 0 or c < 0:
                    print("Seat dosen't Exits!")
                elif self.seats[id][r][c] != "free":
                    print("Seats already booked")
                else:
                    flag = 1
                    self.booked_list.append(x)
                    self.seats[id][r][c] = "X"
                    # print(f'ticket: {x[0]}{x[1]} successfully booked')
            if flag == 1:
                print("\t***** Ticket booked Successfully****")
                print("\n-----------------------------\n")
                print("Name: ", name)
                print(f"Phone: {phone}")
                for i in self.show_list:
                    if i[0] == id:
                        print("Movie: ", i[1], "Time: today at ", i[2])
                print("Tickets: ", end="")
                for i in self.booked_list:
                    print(i, end=" ")
                print("\nHall Number: ", self.hall_no)
                print("Price:", 500 * len(self.booked_list), "TK")


my_hall = Hall(2, 6, 8)
my_hall.enter_show(121, "Game of Thrones", "10:00 AM")
my_hall.enter_show(122, "Breaking Bad", "12:00 AM")
my_hall.enter_show(123, "Interstaler", "5:00 PM")
my_hall.enter_show(124, "Lord of the Rings", "8:00 PM")


while True:
    print("\n---------------------------\n")
    print("1. view all show today.")
    print("2. view avalible seats.")
    print("3. Book tickets.")
    option = int(input("Enter your option: "))

    if option == 1:
        my_hall.view_show_list()

    elif option == 2:
        id = int(input("Enter show id: "))
        my_hall.view_avalable_seats(id)

    elif option == 3:
        id = int(input("Entetr the show id: "))
        name = input("Enter your name: ")
        phone = input("Enter your phone: ")
        tickets = int(input("Enter number of tickets: "))
        booking_seats = []
        for i in range(tickets):
            booking_seats.append(input("Enter your seat no.: "))
        my_hall.book_tickets(id, name, phone, booking_seats)

    else:
        print("Wrong option, chose again\n")
