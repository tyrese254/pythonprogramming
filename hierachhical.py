class Hotel:
    def food(self):
        print("welcome to Las-Devas foods")

    def receipt(self):
        print("LAS-DEVAS menu"
              "1 Releve  / Joints "
              "2 Sorbet / Sorbet"
              "3 Entrée / Entree"
              "4 Poisson / Fish"
              "5 Farinaceous / Farineaux / Pasta or Rice"
              "6 Oeuf / Egg")
class Motel:
    def rooms(self):
        print("welcome to las-Devas motels")
    def description(self):
        print("Rooms are available")
    def room(self):
        print("would you like to set a reservation")

class Staff(Hotel,Motel):
    def pay(self):
        print("LAS-DEVAS HOTEL - Comfort ,Quality and cuisine food  and services")

    def logo(self):
        print("LAS-DEVAS HOTEL - We value You")


l = Staff()
l.food()
l.receipt()
l.rooms()
l.description()
l.room()

