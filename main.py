from abc import ABC, abstractmethod


# Class representing a cake order
class CakeOrder:
    def __init__(self, flavor, size, topping):
        self.flavor = flavor
        self.size = size
        self.topping = topping


# Abstract class that defines the interface for calculating the price of a cake order
class CakePriceCalculator(ABC):
    @abstractmethod
    def calculate_price(self, order):
        pass


# Concrete class that implements the price calculation logic for simple cake orders
class SimpleCakePriceCalculator(CakePriceCalculator):
    def calculate_price(self, order):
        base_price = 10
        if order.size == "large":
            base_price += 5
        if order.topping == "chocolate":
            base_price += 2
        return base_price


# Concrete class that implements the price calculation logic for premium cake orders
class PremiumCakePriceCalculator(CakePriceCalculator):
    def calculate_price(self, order):
        base_price = 15
        if order.size == "large":
            base_price += 8
        if order.topping == "chocolate":
            base_price += 5
        if order.topping == "strawberry":
            base_price += 7
        return base_price


# Interface that defines methods for adding, getting, and removing cake orders
class OrderRepositoryInterface(ABC):
    @abstractmethod
    def add_order(self, order):
        pass

    @abstractmethod
    def get_orders(self):
        pass

    @abstractmethod
    def remove_order(self, order):
        pass


# Implementation of the OrderRepositoryInterface that stores cake orders
class OrderRepository(OrderRepositoryInterface):
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def get_orders(self):
        return self.orders

    def remove_order(self, order):
        self.orders.remove(order)


# Class that creates price calculator objects based on the specified type
class CakePriceCalculatorFactory:
    @staticmethod
    def create_calculator(calc_type):
        if calc_type == "simple":
            return SimpleCakePriceCalculator()
        elif calc_type == "premium":
            return PremiumCakePriceCalculator()
        else:
            raise ValueError("Invalid calculator type")


# Function that displays the menu options
def display_menu():
    print("\nSelect the calculation mode:")
    print("1. Simple Cake Orders")
    print("2. Premium Cake Orders")
    print("0. Exit")


# Function that calculates and displays the prices of orders
def calculate_and_display_prices(order_calculator, orders):
    print("-----------------------------------------")
    for order in orders:
        price = order_calculator.calculate_price(order)
        print(f"Order: {order.flavor}, Price: ${price}")


# Main function that manages the program
def main():
    repository = OrderRepository()

    order1 = CakeOrder("chocolate", "large", "chocolate")
    order2 = CakeOrder("vanilla", "medium", "strawberry")

    repository.add_order(order1)
    repository.add_order(order2)

    print("Cake Order Price Calculator")
    print("---------------------------")

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nCalculating prices for Simple Cake Orders:")
            calculator = CakePriceCalculatorFactory.create_calculator("simple")
            calculate_and_display_prices(calculator, repository.get_orders())

        elif choice == "2":
            print("\nCalculating prices for Premium Cake Orders:")
            calculator = CakePriceCalculatorFactory.create_calculator("premium")
            calculate_and_display_prices(calculator, repository.get_orders())

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
