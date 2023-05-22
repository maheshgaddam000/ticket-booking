
import random

print("_____________Welcome To IRCTC reservation portal____________")

login_details={ "ravikumar@gmail.com":"1234",
"rajesh12@gmail.com":"5678",
"maheshg46@gmail.com":"0963",
"sirisha78@gmail.com":"2233"
}

a={"Delhi To Mumbai":"Available on every Sunday"}         #source and destination availability


login=input("please Enter Your Id to login")
pin=login_details.get(login)
if pin:
    entered_pin=input("please Enter Your Pin to Continue")
    if entered_pin == pin:
        print("login Sucessfull")
    else:
        print("invalid details")
        
while True:
    print("******************************************************")
    print("<<<--- 1. Search For A Train --->>>")
    print("<<<--- 2. Search For Seat Availability --->>>")
    print("<<<--- 3. Book A Train Ticket --->>>")
    print("<<<--- 4. Cancel The Train Ticket --->>>")
    print("<<<--- 5. PNR Enquiry --->>>")
    print("<<<--- 6. EXIT/QUIT --->>>")
    
    
    option=input("Please Enter Your option")
        
    if option=="1":
        print("****************************************")
        print("This Train Running Between Hyderabad To Kurnool")
        class Train:
            def __init__(self, name, departure_time, arrival_time, duration, price):
                self.name = name
                self.departure_time = departure_time
                self.arrival_time = arrival_time
                self.duration = duration
                self.price = price

    # Create a list of trains
        train_list = []

    # Add trains to the list
        train1 = Train("Express 1","09:00", "14:30", "5 hours 30 minutes", 50.0)
        train2 = Train("Superfast 2", "11:30", "16:45", "5 hours 15 minutes", 65.0)
        train3 = Train("Local 3", "14:15", "19:00", "4 hours 45 minutes", 30.0)

        train_list.append(train1)
        train_list.append(train2)
        train_list.append(train3)

    # Access train information
        for train in train_list:
            print("Train:", train.name)
            print("Departure Time:", train.departure_time)
            print("Arrival Time:", train.arrival_time)
            print("Duration:", train.duration)
            print("Price:", train.price)
            print("---------------------")
                

    if option=="2":
        print("1. Train number 12952",
            "2. Train Number 22210")
        train_seats=input("please Enter your train number")
        if train_seats=="1":
            print("180 3A Seats And 115 2A Seats Available")
        
        if train_seats=="2":
            print("120 3A Seats And 180 2A Seats Available")
        

    if option=="3":
        class train:
            def __init__(self,name,age,gender,source,destination,date_of_travel,no_of_tickets,breaths,train_compartment):
                self.n=name
                self.a=age
                self.g=gender
                self.s=source
                self.d=destination
                self.dot=date_of_travel
                self.t=no_of_tickets
                self.b=breaths
                self.c=train_compartment
            def train_details(self):
                print("name:",self.n)
                print("age:",self.a)
                print("gender:",self.g)
                print("source:",self.s)
                print("destination:",self.d)
                print("date_of_travel:",self.dot)
                print("no_of_tickets:",self.t)
                print("breaths:",self.b)
                print("train_compartment:",self.c)
                
        n=input("Please Enter Your Name:")
        a=input("Please Enter Your Age:")
        g=input("Please Enter Your Gender:")
        sot=input("Enter your Source:")
        des=input("Enter Your Destination:")
        dot=input("Enter Your Date Of Travel:")
        nt=input("Enter How Many Tickets Do You Want?:")
        b=input("Enter your prefered breath upper/lower")
        tc=input("Enter Your Compartment sleeper/2AC/3AC:")
        train_obj=train(n,a,g,sot,des,dot,nt,b,tc)
        train_obj.train_details()    
                

    if option=="4":       #cancel the train ticket
        def cancel_ticket(ticket_list, ticket_to_cancel):
            if ticket_to_cancel in ticket_list:
                ticket_list.remove(ticket_to_cancel)
                print("Ticket canceled successfully.")
            else:
                print("Ticket not found.")

    # Example usage
        ticket_list = ['11111','22222','33333','44444','55555']
        ticket_to_cancel = input("Please Enter Your Ticket Number To Cancel")

        cancel_ticket(ticket_list, ticket_to_cancel)
        print("Remaining tickets:", ticket_list)



    if option=="5":
        def pnr_enquiry(pnr):
            status = random.choice(['Confirmed', 'RAC', 'Waiting'])
            return status

        # Generate a random PNR number (10 digits)
        random_pnr = str(random.randint(1000000000, 9999999999))

        # Perform PNR enquiry
        status = pnr_enquiry(random_pnr)

        # Display the results
        print("PNR Number:", random_pnr)
        print("Status:", status)
        
       
    if option=="6":
        print("Thank You For INDIAN RAILWAYS SERVICES Happy Journey")  
        break 
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    