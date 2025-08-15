from routes import Select_route
from calculator import TicketCalculator

#enter details of customers->name,age,phone,category
name=input("Customer Name: ")
age=int(input("Age: "))
phone=input("Enter your phone: ")
category=input("Enter your category out of (Student, Senior, General)").lower()

#routes available and take up routes
print("Available Routes:")
r=Select_route()
selected_route, route_price_time=r.routes_choice()

#no of seats
n=int(input("Enter your no of seats "))


#price calculation
s=TicketCalculator(route_price_time["price"],n,age,category)
rate,total,discount,final=s.discount_total()



# booking summary
print("\n----------------------------------------")
print("        BUS TICKET - TRAVEL AGENCY")
print("-----------------------------------------")
print(f"Passenger Name : {name}")
print(f"Phone Number   : {phone}")
print(f"Age            : {age}")
print(f"Category       : {category.capitalize()}")
print()
print(f"Route          : {selected_route}")
print(f"Departure Time : {route_price_time['time']}")
print(f"Seats Booked   : {n}")
print("-----------------------------------------")
print(f"Ticket Price   : ₹{route_price_time['price']}")
print(f"Total Amount   : ₹{total}")
print(f"Discount rate  : {rate}")
print(f"Discount       : ₹{discount}")
print(f"Final Amount   : ₹{final}")
print("-----------------------------------------")
print(f"\nThank you for booking with us {name}!")

#ticket in file
file_n=f"ticket{name}{phone}.txt"
f1=open(file_n,"w")

f1.write("-------------------------------------------------------------\n")
f1.write("                 BUS TICKET - TRAVEL AGENCY                \n")
f1.write("-------------------------------------------------------------\n")
f1.write("\n")
f1.write(f"Passenger Name : {name}\n")
f1.write(f"Phone Number   : {phone}\n")
f1.write(f"Age            : {age}\n")
f1.write(f"Category       : {category.title()}\n")
f1.write("\n")
f1.write(f"Route          : {selected_route}\n")
f1.write(f"Departure Time : {route_price_time['time']}\n")
f1.write(f"Seats Booked   : {n}\n")
f1.write("\n")
f1.write(f"Ticket Price   : <UNK>{route_price_time['price']}\n")
f1.write(f"Total Amount   : <UNK>{total}\n")
f1.write(f"Discount rate  : <UNK>{discount}\n")
f1.write(f"Final Amount   : <UNK>{final}\n")
f1.write("\n")
f1.write("-------------------------------------------------------------\n")
f1.write(f"\nThank you for booking with us {name}!\n")
f1.close()
