class hotelManagement:

    def __init__(self, rt='', s=0, p=0, r=0, t=0, a=700, name='', address='', cindate='', coutdate='', rno=101):

        print("\t\t\t\t\t*******************************************")
        print("\t\t\t\t\t**********HOTEL MANAGEMENT SYSTEM**********")
        print("\t\t\t\t\t*******************************************")
        self.rt = rt
        self.r = r
        self.t = t
        self.p = p
        self.s = s
        self.a = a
        self.name = name
        self.address = address
        self.cindate = cindate
        self.coutdate = coutdate
        self.rno = rno

    def inputData(self):
        self.name = input("\nEnter Your Name: ")
        self.address = input("\nEnter Your Address: ")
        self.cindate = input("\nEnter Your CheckIn Date: ")
        self.coutdate = input("\nEnter Your CheckOut Date: ")
        print("\nYour Room Number Is: ", self.rno)
        print("\n")

    def roomRent(self):
        print("We Have The Following Rooms For You:")
        print("1. Type A = 5000 $")
        print("2. Type B = 4000 $")
        print("3. Type C = 3000 $")
        print("4. Type D = 2000 $")

        x = int(input("Enter Your Choice: "))
        n = int(input("How Many Nights Did You Stay: "))

        if x == 1:
            print("You Have Opted Room Type A")
            self.s = 5000 * n

        elif x == 2:
            print("You Have Opted Room Type B")
            self.s = 4000 * n

        elif x == 3:
            print("You Have Opted Room Type C")
            self.s = 3000 * n

        elif x == 4:
            print("You Have Opted Room Type D")
            self.s = 2000 * n

        else:
            print("Please Choose A Room: ")

        print("Your Room Rent Is: ", self.s, "\n")

    def restaurantBill(self):
        print("\t\t\t\t\t**********RESTAURANT MENU**********")
        print("1. Water     = 01 $")
        print("2. Tea       = 01 $")
        print("3. Breakfast = 10 $")
        print("4. Lunch     = 13 $")
        print("5. Dinner    = 10 $")
        print("6. Exit")

        while 1:
            c = int(input("Enter Your Choice: "))

            if c == 1:
                d = int(input("Enter The Quantity: "))
                self.r = self.r + 1 * d

            elif c == 2:
                d = int(input("Enter The Quantity: "))
                self.r = self.r + 1 * d

            elif c == 3:
                d = int(input("Enter The Quantity: "))
                self.r = self.r + 10 * d

            elif c == 4:
                d = int(input("Enter The Quantity: "))
                self.r = self.r + 13 * d

            elif c == 5:
                d = int(input("Enter The Quantity: "))
                self.r = self.r + 10 * d

            elif c == 6:
                break
            else:
                print("Invalid Option")

        print("Total Food Cost: ", self.r, "\n")

    def laundryBill(self):
        print("\t\t\t\t\t**********LAUNDRY MENU*********")
        print("1. Shorts    = 3 $")
        print("2. Trousers  = 4 $")
        print("3. Shirt     = 5 $")
        print("4. Jeans     = 6 $")
        print("5. Girl Suit = 8 $")
        print("6. Exit")

        while 1:
            e = int(input("Enter Your Choice: "))

            if e == 1:
                f = int(input("Enter The Quantity: "))
                self.t = self.t + 3 * f

            elif e == 2:
                f = int(input("Enter The Quantity: "))
                self.t = self.t + 4 * f

            elif e == 3:
                f = int(input("Enter The Quantity: "))
                self.t = self.t + 5 * f

            elif e == 4:
                f = int(input("Enter The Quantity: "))
                self.t = self.t + 6 * f

            elif e == 5:
                f = int(input("Enter The Quantity: "))
                self.t = self.t + 8 * f

            elif e == 6:
                break
            else:
                print("Invalid Option")

        print("Total Laundry Cost: ", self.t, "\n")

    def gameBill(self):
        print("\t\t\t\t\t**********GAME MENU**********")
        print("1. Table Tennis = 6 $")
        print("2. Bowling      = 8 $")
        print("3. Snooker      = 7 $")
        print("4. Video Games  = 9 $")
        print("5. Pool         = 5 $")
        print("6. Exit")

        while 1:
            g = int(input("Enter Your Choice: "))

            if g == 1:
                h = int(input("Number Of Hours: "))
                self.p = self.p + 6 * h

            elif g == 2:
                h = int(input("Number Of Hours: "))
                self.p = self.p + 8 * h

            elif g == 3:
                h = int(input("Number Of Hours: "))
                self.p = self.p + 7 * h

            elif g == 4:
                h = int(input("Number Of Hours: "))
                self.p = self.p + 9 * h

            elif g == 5:
                h = int(input("Number Of Hours: "))
                self.p = self.p + 5 * h

            elif g == 6:
                break

            else:
                print("Invalid option")

        print("Total Game Bill: ", self.p, "\n")

    def display(self):
        print("\t\t\t\t\t**********HOTEL BILL**********")
        print("Customer Details: ")
        print("Customer Name: ", self.name)
        print("Customer Address: ", self.address)
        print("Check In Date: ", self.cindate)
        print("Check Out Date: ", self.coutdate)
        print("Room Number: ", self.rno)
        print("Your Room Rent Is: ", self.s)
        print("Your Food Bill Is: ", self.r)
        print("Your Laundry Bill Is: ", self.t)
        print("Your Game Bill Is: ", self.p)

        self.rt = self.s + self.t + self.p + self.r

        print("Your Sub-Total Bill Is: ", self.rt)
        print("Additional Service Charges Is: ", self.a)
        print("Your Grand Total Bill Is: ", self.rt + self.a, "\n")

        self.rno += 1


def main():
    a = hotelManagement()

    while 1:
        print("1. Enter Customer Data")
        print("2. Calculate Room Rent")
        print("3. Calculate Restaurant Bill")
        print("4. Calculate Laundry Bill")
        print("5. Calculate Game Bill")
        print("6. Show Total Cost")
        print("7. Exit")

        b = int(input("\nEnter Your Choice: "))

        if b == 1:
            a.inputData()

        if b == 2:
            a.roomRent()

        if b == 3:
            a.restaurantBill()

        if b == 4:
            a.laundryBill()

        if b == 5:
            a.gameBill()

        if b == 6:
            a.display()

        if b == 7:
            quit()


main()
