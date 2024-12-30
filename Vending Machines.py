class VendingMachine:
    def __init__(self):
        #Initialize the vending machine with a list of items.
        self.items = {
            1: {"id": 1, "category": "Drink", "name": "Water", "price": 1.50, "stock": 20},
            2: {"id": 2, "category": "Drink", "name": "Soda", "price": 3.50, "stock": 7},
            3: {"id": 3, "category": "Drink", "name": "Orange Juice", "price": 3.50, "stock": 8},
            4: {"id": 4, "category": "Drink", "name": "Apple Juice", "price": 4.50, "stock": 10},
            5: {"id": 5, "category": "Drink", "name": "Mango Juice", "price": 5.50, "stock": 7},
            6: {"id": 6, "category": "Snack", "name": "Cheese Chips", "price": 4.50, "stock": 3},
            7: {"id": 7, "category": "Snack", "name": "Chocolate", "price": 3.00, "stock": 10},
            8: {"id": 8, "category": "Snack", "name": "Chocolate, With Peanuts", "price": 5.00, "stock": 8},
            9: {"id": 9, "category": "Snack", "name": "Biscuit", "price": 5.50, "stock": 3},
            10: {"id": 10, "category": "Snack", "name": "Salted Chips", "price": 6.00, "stock": 1},
        }

#Show the items available in the vending machine grouped by category.
    def display_items(self):
        
        print("\n--- Welcome to the Vending Machine ---")
        self._show_items_by_category("Drink")
        self._show_items_by_category("Snack")
        
#Display items of a specific category.
    def _show_items_by_category(self, category):
        
        print(f"\n{category}s:")
        for item in self.items.values():
            if item["category"] == category:
                print(f"{item['id']}: {item['name']} - ${item['price']}")
                
#Allow users to select items and proceed to payment.
    def select_items(self):  
        cart = []
        while True:
            item_id = input("\nEnter item number to select (or 0 to finish): ")
            if item_id == "0":
                if cart:
                    break
                print("You haven't selected any items yet!")
                continue
            
            if not self._is_valid_item_id(item_id):
                print("Invalid item number. Try again.")
                continue

            item = self.items[int(item_id)]
            quantity = self._get_quantity(item)
            if quantity > 0:
                cart.append({"name": item["name"], "price": item["price"], "quantity": quantity})
                item["stock"] -= quantity
                print(f"Added {quantity}x {item['name']} to your cart.")
            
            if not self._prompt_continue():
                break

        if cart:
            self._process_payment(cart)

    def _is_valid_item_id(self, item_id):
        #Checks if the item ID is valid.
        return item_id.isdigit() and int(item_id) in self.items

    def _get_quantity(self, item):
        #Prompt the user to enter the quantity of an item.
        try:
            quantity = int(input(f"Enter quantity for {item['name']} (Available: {item['stock']}): "))
            if 0 < quantity <= item["stock"]:
                return quantity
            print("Invalid quantity. Try again.")
            return 0
        except ValueError:
            print("Please enter a valid number.")
            return 0

    def _prompt_continue(self):
        #Ask the user if they want to select another item.
        response = input("Do you want to select another item? (Yes/No): ")
        return response.lower() == "yes"

    def _process_payment(self, cart):
        #Calculate total cost and handle payment.
        total = sum(item["price"] * item["quantity"] for item in cart)
        print("\n--- Payment Summary ---")
        for item in cart:
            print(f"{item['name']} x{item['quantity']} - ${item['price'] * item['quantity']:.2f}")
        print(f"Total Amount: ${total:.2f}")
        
        while True:
            try:
                payment = float(input("Enter payment amount: $"))
                if payment >= total:
                    change = payment - total
                    print(f"Payment successful! Your change: ${change:.2f}")
                    self._print_receipt(cart, total, payment, change)
                    break
                else:
                    print("Insufficient payment. Try again.")
            except ValueError:
                print("Invalid input. Enter a valid amount.")

    def _print_receipt(self, cart, total, payment, change):
        #Generate and display a receipt for the user.
        print("\n--- Receipt ---")
        for item in cart:
            print(f"{item['name']} x{item['quantity']} - ${item['price'] * item['quantity']:.2f}")
        print(f"Total: ${total:.2f}")
        print(f"Payment: ${payment:.2f}")
        print(f"Change: ${change:.2f}")
        print("\nThank you for using the vending machine!")

def main():
    vending_machine = VendingMachine()
    vending_machine.display_items()
    vending_machine.select_items()

if __name__ == "__main__":
    main()
