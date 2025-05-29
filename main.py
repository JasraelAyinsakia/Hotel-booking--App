import pandas
from pandas.plotting import hist_frame

df = pandas.read_csv("hostels.csv")


class Hostel:
    def __init__(self, id):
        pass

    def book(self):
        pass

    def available(self):
        pass

class ReservationTicket:
    def __init__(self, customer_name, hostel_object):
        pass

    def generate(self):
        content = f"Name of the customer hostel"
        return  content



print(df)
id = input("Enter the id of the hostel: ")
hostel_id = Hostel(id)

if hostel.available():
    hostel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hostel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free.")