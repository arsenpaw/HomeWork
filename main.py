from decimal import *
import pytest


class Getter:
    """
    A non-data descriptor that provides a custom getter method for attributes.

   Attributes defined using this descriptor are stored as private attributes
   prefixed with "__". The getter method retrieves the value of the private
   attribute when the attribute is accessed on an instance of the class.
    """

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Sneakers:
    """
    Represents a pair of sneakers with various attributes.

   Attributes:
       brand (str): The brand name of the sneakers.
       size (float): The size of the sneakers.
       color (str): The color of the sneakers.
       price (Decimal): The price of the sneakers.
       quantity (int): The quantity of sneakers in stock.
       material (str): The material of the sneakers.
       numberOfSales (int): The number of times the sneakers have been sold.
    """

    brand = Getter()
    size = Getter()
    color = Getter()
    price = Getter()
    quantity = Getter()
    material = Getter()
    numberOfSales = Getter()

    def __init__(
        self,
        brand: str,
        size: float,
        color: str,
        price: int | float,
        quantity: int,
        material: str,
        numberOfSales: int,
    ):
        """
        Initialize a sneaker object with the provided attributes .
        """
        self.__validator_brand_name(brand)
        self.__validator_size(size)
        self.__validator_color(color)
        self.__validator_price(price)
        self.__validator_quantity(quantity)
        self.__validator_material(material)
        self.__validator_numberOfSales(numberOfSales)
        self.brand = brand
        self.size = size
        self.color = color
        self.price = price
        self.quantity = quantity
        self.material = material
        self.numberOfSales = numberOfSales

    def __str__(self):
        return f"Brand is: {self.brand},Size is: {self.size} , Color is: {self.color}"

    @classmethod
    def __validator_brand_name(cls, brand):
        if type(brand) != str:
            raise TypeError("Brand have tp be STRING")

    @classmethod
    def __validator_size(cls, size):
        try:
            size = float(size)
        except:
            raise ValueError("Parse size exeption")

    @classmethod
    def __validator_color(cls, color):
        if type(color) != str:
            raise TypeError("Color have tp be STRING")

    @classmethod
    def __validator_price(cls, price):
        try:
            price = Decimal(price)
        except:
            raise ValueError("Parse price exeption")

    @classmethod
    def __validator_quantity(cls, quantity):
        if type(quantity) != int:
            raise TypeError("Quantyity have tp be INT")

    @classmethod
    def __validator_material(cls, material):
        if type(material) != str:
            raise TypeError("Material have tp be STRING")

    @classmethod
    def __validator_numberOfSales(cls, numberOfSales):
        if type(numberOfSales) != int:
            raise TypeError("numberOfSales have tp be INT")


class ShoesStore:
    """
     A store that manages a collection of sneakers.

   Attributes:
       things (list): A list of Sneakers objects representing the inventory.
    """

    @classmethod
    def __validator_sneakers(cls, sneakrs):
        if type(sneakrs) != Sneakers:
            raise TypeError("Only Sneakers can be added to this shop")

    def __init__(self, *args):
        """
        Initialize the inventory with sneakers.
        """
        self.__things = []
        for sneakrs in args:
            self.__validator_sneakers(sneakrs)
            self.__things.append(sneakrs)

    def add_sneaker(self, *args):
        """
        Add one or more sneakers to the inventory.
        """
        for sneakrs in args:
            self.__validator_sneakers(sneakrs)
            self.__things.append(sneakrs)

    def print_inventory(self):
        """
        Print all information from ShoesStore: class
        """
        for item in self.__things:
            print("-" * 130)
            print(f"Brand is: {item.brand}", end=" | ")
            print(f"Size is: {item.size}", end=" | ")
            print(f"Color is: {item.color}", end=" | ")
            print(f"Price is: {item.price}", end=" | ")
            print(f"Quantity: {item.quantity}", end=" | ")
            print(f"Material is: {item.material}")
            print("-" * 130)

    def sort_by_cost(self):
        """
        Sort the inventory by the cost (price) of each item in descending order.
        """
        self.__things.sort(key=lambda x: x.price, reverse=True)
        print("SPRTED BY COST")
        self.print_inventory()

    def sort_by_quantity(self):
        """
        Sort the inventory by the quantity of each item in descending order.
        """
        self.__things.sort(key=lambda x: x.quantity, reverse=True)
        print("SPRTED BY QUANTITY")
        self.print_inventory()

    def sort_by_top(self):
        """
        Sort the inventory by the number of sales for each item in descending order.
        """
        self.__things.sort(key=lambda x: x.numberOfSales, reverse=True)
        print("TOP SNEAKERS")
        self.print_inventory()

    def chose_by_brand(self, s_brand):
        """
        Filter and print items in the inventory based on the specified brand.
        """
        find_sneakr = []
        for senaker in self.__things:
            if senaker.brand == s_brand:
                find_sneakr.append(senaker)
        for item in find_sneakr:
            print(item)


if __name__ == "__main__":
    nike = Sneakers("Nike", 10, "Black", 100, 35, "Leather", 1000)
    adidas = Sneakers("Adidas", 9, "White", 80, 3, "Mesh", 800)
    reebok = Sneakers("Reebok", 11, "Red", 120, 9, "Synthetic", 1200)
    vans = Sneakers("Vans", 9, "Checkerboard", 65, 3, "Canvas", 750)
    new_balance = Sneakers("New Balance", 10, "Gray", 95, 4, "Mesh", 850)
    puma = Sneakers("Puma", 8, "Red", 75, 2, "Suede", 750)
    puma2 = Sneakers("Puma", 4, "Reed", 755, 2, "Suede", 750)
    shoesstorepro = ShoesStore(nike, adidas, reebok, vans, new_balance, puma2, puma)
    shoesstorepro.print_inventory()

else:
    print("Code is imported")
