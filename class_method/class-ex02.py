# Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.
# Perform the following tasks now:
#   Now add items to the menu. O
#   Make table reservations. O
#   Take customer orders. O
#   Print the menu.
#   Print table reservations.
#   Print customer orders.

# Note: Use dictionaries and lists to store the data.


class Resturant:

  def __init__(self, menu_items, num_table):
    # Initialize the menu item list
    self.menu_items = menu_items  # list

    # Initialize the table dictionary
    self.book_table = {}  # dictionary
    for i in range(1, 21):
      self.book_table[i] = "available"

    self.customer_orders = {}  # dictionary
    for i in range(1, 21):
      self.customer_orders[i] = []

  def add_item_to_menu(self, new_menu):
    self.menu_items.extend(new_menu)

    print(new_menu, "have been added.")
    print(self.menu_items)

  def book_tables(self, table_number):
    self.book_table
    if self.book_table[table_number] == 'available':
      self.book_table[table_number] = 'unavailable'
    else:
      print('Table', table_number, 'is already booked.')

  def customer_orders(self, order, table_number):
    self.customer_order[table_number].extend(order)


Rosalyn_Pasta = Resturant(["pasta"], 20)
Rosalyn_Pasta.add_item_to_menu(["pizza", "spanich_artichoke"])
