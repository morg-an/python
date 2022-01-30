import datetime

#create business class
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
#create franchise class
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    print("Store located at " + self.address)

  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu.name)
    return available_menus
#create menu class
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return(str("The {} menu is served from {} to {}.".format(self.name, self.start_time, self.end_time)))
  
  def calculate_bill(self, purchased_items):
    bill_amount = 0
    for item in purchased_items:
      if item in self.items:
        bill_amount += self.items[item]
    return bill_amount

#create instances of menus
brunch = Menu("Brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, datetime.time(11,00), datetime.time(16,00))

early_bird = Menu("Early Bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, datetime.time(15, 00), datetime.time(18, 00))

dinner = Menu("Dinner", {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}, datetime.time(17,00), datetime.time(23,00))

kids = Menu("Kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, datetime.time(11,00), datetime.time(21,00))

arepas_menu = Menu("Take a’ Arepa", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, datetime.time(10,00), datetime.time(20,00))

#create instances of franchise stores
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

#create instance of business
business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
business = Business("Take a' Arepa", arepas_place)

#testing
#bill calculation method
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

#menu availability method
print(flagship_store.available_menus(datetime.time(12,00)))
print(flagship_store.available_menus(datetime.time(17,00)))
