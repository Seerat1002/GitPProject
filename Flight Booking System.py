#Class 12 Computer Science Project using python and MySql Database


import qrcode
import random
import mysql.connector as sqltor

mycon = sqltor.connect(host = 'localhost' ,user = 'root' ,passwd = 'Seer@tk@ur' ,database = 'SCENIK_AIRLINES')
cursor = mycon.cursor()

def NewFlight():
    print('\nNew flight details')
    Dep = input('From: ')
    Des = input('To: ')
    date = input('Date (YYYY-MM-DD): ')
    TOD = input('Time of departure (HH:MM:SS): ')
    FH = input('Flight hours: ')
    FN = input('Flight number: ')
    F = int(input('Fare: '))
    query = '''
        INSERT INTO flight (Departure, Destination, Date, Time_of_Departure, Flight_Hours, Flight_no, Fare) 
        VALUES ('{}', '{}', '{}', '{}', '{}', '{}', {});
    '''
    cursor.execute(query.format(Dep, Des, date, TOD, FH, FN, F))
    mycon.commit()
    print('Flight details added successfully.')

def EditFlight():
    print('''
COLUMN TO EDIT
1. Departure
2. Destination
3. Date
4. Time of departure
5. Flight hours
6. Flight number
7. Flight fare
''')
    column_map = {
        1: "Departure",
        2: "Destination",
        3: "Date",
        4: "Time_of_Departure",
        5: "Flight_Hours",
        6: "Flight_no",
        7: "Fare"
    }
    while True:
        try:
            col_choice = int(input('Enter the column number to edit (1-7): '))
            if col_choice in column_map:
                column_name = column_map[col_choice]
                FN = input('Flight number: ')
                DODep = input("Date of Departure: ")
                newFN = input(f'Enter new {column_name}: ')
                query = f"UPDATE flight SET {column_name} = %s WHERE Flight_no = %s AND Date = %s;"
                cursor.execute(query,(newFN, FN, DODep))
                mycon.commit()
                print(f'{column_name} updated successfully.')
                break
            else:
                print('Invalid choice, try again.')
        except ValueError:
            print('Invalid input, please enter a number.')
                
def DeleteFlight():
    print('\nDelete Flight Details')
    FN = input('Flight number: ')
    date = input('Date (YYYY-MM-DD): ')
    query = "DELETE FROM flight WHERE Flight_no = '{}' AND Date = '{}';"
    cursor.execute(query.format(FN, date))
    mycon.commit()
    print('Flight details deleted successfully.')
    
def AddFood():
    print('''
MENU CATEGORIES
1. Beverages
2. Snacks/Starters
3. Meals
4. Dessert
''')
    menu_map = {1: "beverages", 2: "snacks", 3: "meals", 4: "dessert"}
    while True:
        try:
            menu_choice = int(input('Choose menu to add into (1-4): '))
            if menu_choice in menu_map:
                menu = menu_map[menu_choice]
                Sno = int(input('Serial no.: '))
                Name = input('Name: ')
                Price = int(input('Price: '))
                if menu != "beverages":
                    V_NV = input('Veg/Non-Veg: ')
                    query = f'INSERT INTO {menu} (Sno, Name, V_NV, Price) VALUES (%s, %s, %s, %s);'
                    cursor.execute(query,(Sno, Name, V_NV, Price))
                else:
                    query = f'INSERT INTO {menu} (Sno, Name, Price) VALUES (%s, %s, %s)'
                    cursor.execute(query,(Sno, Name, Price))
                
                mycon.commit()
                print(f'{menu.capitalize()} added successfully.')
                break
            else:
                print('Invalid choice, try again.')
        except ValueError:
            print('Invalid input, please enter a number.')

def RevisePrice():
    print('''\nMENU
1. Beverages
2. Snacks
3. Meals
4. Dessert''')
    
    category = {1: "beverages", 2: "snacks", 3: "Meals", 4: "Dessert"}
    
    C = int(input('Revise price of (1-4): '))
    if C in category:
        N = input(f'Name of {category[C][:-1]}: ')  # Removing last character 's' for plural form
        P = int(input('Old price: '))
        NewP = int(input('New price: '))
        cursor.execute(f'UPDATE {category[C]} SET Price = {NewP} WHERE Name = "{N}" and Price = {P};')
        mycon.commit()
        
    else:
        print("Invalid choice. Please select a valid option (1-4).")

def DeleteFood():
    print('''\nMENU
1. Beverages
2. Snacks
3. Meals
4. Dessert''')

    category = {1: "beverages", 2: "snacks", 3: "Meals", 4: "Dessert"}

    C = int(input('Delete (1-4): '))
    if C in category:
        N = input(f'Name of {category[C][:-1]}: ')
        cursor.execute(f'DELETE FROM {category[C]} WHERE Name = "{N}";')
        print(f'{N} has been successfully deleted from {category[C]}.')
        mycon.commit()
    else:
        print("Invalid choice. Please select a valid option (1-4).")
            
def AMenu():

    while True:
        print('''
ADMIN MENU
1. Add new flight details
2. Edit flight details
3. Delete flight details
4. Add new food menu
5. Revise food prices
6. Delete food menu
7. Exit
''')
        choice = int(input("Enter your choice (1-7): "))
        if choice == 1:
            NewFlight()
        elif choice == 2:
            EditFlight()
        elif choice == 3:
            DeleteFlight()
        elif choice == 4:
            AddFood()
        elif choice == 5:
            RevisePrice()
        elif choice == 6:
            DeleteFood()
        elif choice == 7:
            print("Exiting Admin Menu.")
            break
        else:
            print("Invalid choice. Try again.")

def Seat():
    global price
    price = 0
    class_prices = {"Business":15000, "First": 1000, "Economy": 5000}
    seats = [
        ["[ ] 1A", "[ ] 1B", "                ", "[ ] 1D", "[ ] 1E"],
        ["[ ] 2A", "[ ] 2B", "                ", "[ ] 2D", "[ ] 2E"],
        ["[ ] 3A", "[ ] 3B", "                ", "[ ] 3D", "[ ] 3E"],
        ["[ ] 4A", "[ ] 4B", "                ", "[ ] 4D", "[ ] 4E"],
        ["[ ] 5A", "[ ] 5B", "                ", "[ ] 5D", "[ ] 5E"],
        ["[ ] 6A", "[ ] 6B", "[ ] 6C", "[ ] 6D", "[ ] 6E", "[ ] 6F"],
        ["[ ] 7A", "[ ] 7B", "[ ] 7C", "[ ] 7D", "[ ] 7E", "[ ] 7F"],
        ["[ ] 8A", "[ ] 8B", "[ ] 8C", "[ ] 8D", "[ ] 8E", "[ ] 8F"]
    ]
    while True:
        
        print("\nSeating Layout:")
        for i, row in enumerate(seats):
            if i == 0: print("Business Class")
            elif i == 2: print("\nFirst Class")
            elif i == 5: print("\nEconomy Class")
            print("  ".join(row))
        
        global seat
        seat = input("\nEnter the seat to book (e.g., 2A): ").upper()
        try:
            row, col = int(seat[:-1]) - 1, ord(seat[-1]) - ord('A')
            if "[ ]" in seats[row][col]:
                seats[row][col] = seats[row][col].replace("[ ]", "[X]")
                if row < 2:
                    seat_class = "Business"
                elif row < 5:
                    seat_class = "First"
                else:
                    seat_class = "Economy"
                price = class_prices[seat_class]
                
                print(f'''Seat {seat} Chosen in {seat_class} Class. 
Price: ₹{price}''')
            
            else:
                print("Seat already booked.")
        except (IndexError, ValueError):
            print("Invalid seat. Try again.")
        
        price =+ price 
        break
        
def SearchFlights():
    print('\n')
    trip_type = input('Round trip or one way: ').strip().upper().replace(' ', '')

    if trip_type in ['ROUNDTRIP', 'ONEWAY']:
        if trip_type == 'ROUNDTRIP':
            TOD = int(input('Total destinations: '))
        else:
            TOD = 1

        for i in range(TOD):
            if trip_type == 'ROUNDTRIP':
                print(f"\nDetails for travel {i + 1}")
            Dep = input('Departure from (City/State Code): ')
            Des = input('Destination (City/State Code): ')
            DODep = input('Date of departure (YY/MM/DD): ')
            
            cursor.execute(f'SELECT * FROM flight WHERE Departure = "{Dep}" AND destination = "{Des}" AND Date = "{DODep}";')
            results = cursor.fetchall()

            if results:
                for row in results:
                    print(row)
            else:
                print('No flights available for the given details.')
    else:
        print('Invalid choice. Please enter "Round trip" or "One way".')

def MBooking():
    print('\nMENU')
    print('''
1. Passenger Details
2. Seat selection
3. Meals
4. Booking Details
5. Payment''')
    
    Cost = 0

    print("\nPASSENGER DETAILS")
    print("Enter details below to book a flight ticket")
    
    NoP = int(input("No of Passengers: "))
    FNo = input("Enter Flight number: ")
    DODep = input('Date of departure (YYYY-MM-DD): ')

    for i in range(NoP):
        global Cn,FN,SA
        print(f"Fill Details for passenger {i + 1}")
        Pre = input("Mr./Mrs./Ms: ")
        FN = input("First Name: ")
        LN = input("Last Name: ")
        DOB = input("Date of Birth (YYYY-MM-DD): ")
        Em = input("Email: ")
        Cn = int(input("Enter 10-digit contact number: "))
        SA = input("Special attention/Wheelchair services (Yes/No): ")
        
        cursor.execute("INSERT INTO booking (Prefix,First_Name,Last_Name,DOB,Email,Contact,Special_Attention) values ('{}','{}','{}','{}','{}',{},'{}');".format(Pre,FN,LN,DOB,Em,Cn,SA))
        
        print('\n')
        cursor.execute("SELECT Fare FROM flight WHERE Flight_no = %s AND Date = %s;", (FNo, DODep))
        fares = cursor.fetchall()
        for fare_tuple in fares:
            fare = int(fare_tuple[0])  # Extract the first element from the tuple
            Cost += fare
         
        # Seat selection
        print("SEAT SELECTION")
        SnS = input("Do you want to select a seat (Yes/No)? ").strip().upper()
        if SnS == 'YES':
            Seat()
            global price
            Cost += price
            cursor.execute(
                "UPDATE Booking SET Seat = '{}', Cost = {} WHERE Contact = {};".format(seat,Cost,Cn)
                )
            mycon.commit()
        elif SnS == 'NO':
            print("Your seat will be allotted on the day of departure.")
        else:
            print("Invalid input. Please try again.")
    
    print('\nMEALS')
    print("Complementary meal will be provided.")
    A = input("Would you like to add a meal (Yes/No)? ").strip().upper()

    if A == 'YES':
        cursor.execute("SELECT * FROM Meals")
        print("Available Meals:")
        for row in cursor.fetchall():
            print(row)
    
        N = str(input("Name of meal: "))
        cursor.execute("UPDATE Booking SET Add_In = '{}' WHERE Contact = {};".format(N, Cn))
        print('Add in meal added successfully')
        cursor.execute("SELECT Price FROM Meals WHERE Name = '{}';".format(N))
        meal_prices = cursor.fetchall()
        mycon.commit()
        for price_tuple in meal_prices:
            price = int(price_tuple[0])  # Extract the first element from the tuple
            Cost += price  # Update the total cost
            
        
    print('\nBOOKING DETAILS')
    print("Flight Details:")
    cursor.execute('''
                   SELECT flight.Date, flight.Departure, flight.Destination, flight.Time_of_Departure, 
                   flight.flight_no, booking.Prefix, booking.First_Name, booking.Last_Name, 
                   booking.DOB, booking.Email, booking.Contact, booking.Special_attention, 
                   booking.Seat, booking.Cost, booking.Add_In 
                   FROM booking,flight WHERE Booking.flight_no = flight.flight_no AND 
                   flight.Flight_No = '{}' AND flight.Date = '{}' AND Contact = {} AND First_Name = '{}';'''.format(FNo, DODep,Cn,FN))
    for row in cursor.fetchall():
        print(row)
            
    cursor.execute("SELECT Prefix,First_Name,Last_Name,Email,Contact, Special_Attention,Seat,Add_In FROM Booking WHERE Contact = {};".format(Cn))
    print("Booking Details:")
    for row in cursor.fetchall():
        print(row)

    print(f"Total Cost: ₹{Cost}")
    cursor.execute("UPDATE Booking SET Cost = {} WHERE First_Name = '{}' AND Contact = {};".format(Cost,FN,Cn))
    
    print('\nPAYMENT')
    print(f"Total Cost = ₹{Cost}")
    print('''PAYMENT METHOD
1. Credit Card
2. Debit Card
3. UPI''')
    
    PM = int(input("Choose payment method (1-3): "))
    if PM in [1, 2]:
        card_no = input('Enter 16-digit card number: ')
        expiry = input("Card expiry date (YYYY-MM-DD): ")
        cvv = input("Enter 3-digit CVV code: ")
        name = input("Cardholder full name: ")
        pin = input("Enter 4-digit authorized PIN: ")
        print("Payment made successfully! Booking confirmation will be sent to the registered email and phone.")
    elif PM == 3:
        img = qrcode.make("Go back to the Python window and enter the authorized UPI PIN.")
        img.save("upi_payment.jpg")
        print("Scan to make payment", img.show())
        input("Enter UPI authorized 4-digit PIN: ")
        print("Payment Successful")
    else:
        print("Invalid payment method. Please try again.")

    # Generate PNR
    pnr = random.randint(1000000000, 9999999999)
    img2 = qrcode.make(f"PNR = {pnr}")
    img2.save("pnr_code.jpg")
    print("Scan to get PNR number") 
    img2.show()
    cursor.execute(
        '''INSERT INTO Booking (PNR,Flight_no) VALUES ({},"{}");'''.format(pnr,FNo)
    )
    print("Thank you for choosing SCENIK AIRLINES")
    mycon.commit()
                
def CheckIn():
    passengers = int(input("Number of passengers: "))
    
    for i in range(passengers):
        print("\nFill details for web check-in and obtain boarding pass:")
        pnr = int(input("Enter 10-digit PNR number: "))
        last_name = input("Last Name: ")
        first_name = input("First Name: ")
        prefix = input("Mr./Mrs./Ms.: ").capitalize()

        cursor.execute("SELECT flight.departure, flight.destination, flight.date, booking.seat, booking.flight_no, PNR FROM Booking, flight WHERE Booking.flight_no = flight.flight_no AND booking.PNR = {} AND booking.First_Name = '{}' AND booking.Last_Name = '{}';".format(pnr,first_name,last_name))
        booking_details = cursor.fetchone()
        for i in booking_details:
            departure = str(booking_details[0])
            destination = str(booking_details[1])
            Date = str(booking_details[2])
            seat = str(booking_details[3])
            flight_number = str(booking_details[4])
            pnr = int(booking_details[5])

        if booking_details:
            booking_details = departure, destination, Date, seat, flight_number
            boarding_pass = f"""                      BOARDING PASS
{last_name}/{first_name}/{prefix}
From: {departure}                                  To: {destination}
Date: {Date}                      Seat: {seat}
Flight Number: {flight_number}
PNR: {pnr}"""
            
            img = qrcode.make(boarding_pass)
            img.save("boarding_pass.jpg")
            print("Scan to get boarding pass")
            img.show()
            print("Web Check-in successful")
        else:
            print("No matching booking found. Please check the details.")
        
def FlightStatus():
    print("Fill in the details to check flight status.")
    Dep = input("Departure: ")
    Des = input("Destination: ")
    DODep = str(input("Date of Departure (YY/MM/DD): "))
    flight_no = input("Flight Number: ")

    cursor.execute("SELECT * FROM flight WHERE Flight_no = '{}' AND Departure = '{}' AND Destination = '{}' AND Date = '{}';".format(flight_no,Dep,Des,DODep))
    results = cursor.fetchall()

    if results:
        for row in results:
            print(row)
    else:
        print("No matching flight found.")
        
def PMenu():
    while True:
        print('''
PASSENGER MENU
1. Search Flights
2. Manage Booking
3. Check In
4. Flight status
5. Exit
''')
        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
            SearchFlights()
        elif choice == 2:
            MBooking()
        elif choice == 3:
            CheckIn()
        elif choice == 4:
            FlightStatus()
        elif choice == 5:
            print("Exiting Passenger Menu.")
            break
        else:
            print("Invalid choice. Try again.")
            
def Menu():
    while True:
        print('''
SCENIK AIRLINES
1. Admin
2. Passenger
3. Exit
''')
        choice = (input('Login as: ')).upper()
        if choice == "ADMIN":
            AMenu()
        elif choice == 'PASSENGER':
            PMenu()
        elif choice == 'EXIT':
            print("Exiting system.")
            break
        else:
            print('Invalid choice. Try again.')

Menu()