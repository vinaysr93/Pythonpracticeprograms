### TODO:
#   - code a Pants class with the following attributes
#   - color (string) eg 'red', 'yellow', 'orange'
#   - waist_size (integer) eg 8, 9, 10, 32, 33, 34
#   - length (integer) eg 27, 28, 29, 30, 31
#   - price (float) eg 9.28

class Pants:

    def __init__(self, color, waist_size, length, price):
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price

    ### TODO: Declare the Pants Class

    ### TODO: write an __init__ function to initialize the attributes

    ### TODO: write a change_price method:
    #    Args:
    #        new_price (float): the new price of the shirt
    #    Returns:
    #        None
    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return ((1 - discount) * self.price)

### TODO: write a discount method:
#    Args:
#        discount (float): a decimal value for the discount.
#            For example 0.05 for a 5% discount.
#
#    Returns:
#        float: the discounted price


### TODO:
#   Code a SalesPerson class with the following attributes
#   - first_name (string), the first name of the salesperson
#   - last_name (string), the last name of the salesperson
#   - employee_id (int), the employee ID number like 5681923
#   - salary (float), the monthly salary of the employee
#   - pants_sold (list of Pants objects),
#            pants that the salesperson has sold
#   - total_sales (float), sum of sales of pants sold

### TODO: Declare the SalesPerson Class
class SalesPerson:

    ### TODO: write an __init__ function to initialize the attributes
    ###    Input Args for the __init__ function:
    #        first_name (str)
    #        last_name (str)
    #        employee_id (int)
    # .      salary (float)
    #
    def __init__(self, first_name, last_name, employee_id, salary):

        self.pants_sold = []
        self.total_sales = 0
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary

    # You can initialize pants_sold as an empty list
    # You can initialize total_sales to zero.
    #
    ###
    def sell_pants(self, pants):

        self.pants_sold.append(pants)

    ### TODO: write a sell_pants method:
    #
    #    This method receives a Pants object and appends
    #    the object to the pants_sold attribute list
    #
    #    Args:
    #        pants (Pants object): a pants object
    #    Returns:
    #        None
    def display_sales(self):

        for x in self.pants_sold:
            print("color:", x.color, end=", ")
            print("waist_size:", x.waist_size, end=", ")
            print("length:", x.length, end=", ")
            print("price:", x.price, end=" ")
            print("\n")

    ### TODO: write a display_sales method:
    #
    #    This method has no input or outputs. When this method
    #    is called, the code iterates through the pants_sold list
    #    and prints out the characteristics of each pair of pants
    #    line by line. The print out should look something like this
    #
    #   color: blue, waist_size: 34, length: 34, price: 10
    #   color: red, waist_size: 36, length: 30, price: 14.15
    #
    #
    #
    ###
    def calculate_sales(self):

        for y in self.pants_sold:
            self.total_sales += y.price

        return self.total_sales

    ### TODO: write a calculate_sales method:
    #      This method calculates the total sales for the sales person.
    #      The method should iterate through the pants_sold attribute list
    #      and sum the prices of the pants sold. The sum should be stored
    #      in the total_sales attribute and then return the total.
    #
    #      Args:
    #        None
    #      Returns:
    #        float: total sales
    #
    ###

    ### TODO: write a calculate_commission method:
    #
    #   The salesperson receives a commission based on the total
    #   sales of pants. The method receives a percentage, and then
    #   calculate the total sales of pants based on the price,
    #   and then returns the commission as (percentage * total sales)
    #
    #    Args:
    #        percentage (float): comission percentage as a decimal
    #
    #    Returns:
    #        float: total commission
    #
    #
    ###
    def calculate_commission(self, percentage):

        total_commission = 0
        total_commission = self.total_sales * percentage

        return total_commission