users = {
    "admin": {"password": "admin", "role": "admin"},
    "user": {"password": "user", "role": "User"}
}

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: ${self.price}, Stock: {self.stock_quantity}"

class Inventory:
    def __init__(self):
        self.products = {}
        self.low_stock_threshold = 5
        self._add_sample_products()

    def _add_sample_products(self):
        self.add_product("P001", "Apple", "Fruit", 0.5, 10)
        self.add_product("P002", "Banana", "Fruit", 0.3, 8)
        self.add_product("P003", "Carrot", "Vegetable", 1.0, 12)
        self.add_product("P004", "Laptop", "Electronics", 999.99, 3)
        self.add_product("P005", "Smartphone", "Electronics", 599.99, 2)

    def add_product(self, product_id, name, category, price, stock_quantity):
        if product_id in self.products:
            print("Product with this ID already exists.")
            return
        self.products[product_id] = Product(product_id, name, category, price, stock_quantity)
        print("Product added successfully.")

    def edit_product(self, product_id, name=None, category=None, price=None, stock_quantity=None):
        if product_id not in self.products:
            print("Product not found.")
            return
        product = self.products[product_id]
        if name: product.name = name
        if category: product.category = category
        if price is not None: product.price = price
        if stock_quantity is not None: product.stock_quantity = stock_quantity
        print("Product updated successfully.")

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    def view_products(self):
        if not self.products:
            print("No products in inventory.")
            return
        for product in self.products.values():
            print(product)
            if product.stock_quantity <= self.low_stock_threshold:
                print("** Low Stock Warning! Please consider restocking **")

    def search_product(self, search_term):
        found = [p for p in self.products.values() if search_term.lower() in p.name.lower() or search_term.lower() in p.category.lower()]
        if found:
            for product in found:
                print(product)
        else:
            print("No matching products found.")

    def adjust_stock(self, product_id, quantity):
        if product_id not in self.products:
            print("Product not found.")
            return
        product = self.products[product_id]
        product.stock_quantity += quantity
        print("Stock updated successfully.")
        if product.stock_quantity <= self.low_stock_threshold:
            print("** Low Stock Warning! Please consider restocking **")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username]["password"] == password:
        print(f"Login successful! Welcome {username}.")
        return users[username]["role"]
    else:
        print("Invalid username or password.")
        return None

def main():
    inventory = Inventory()

    while True:
        role = login()
        if role is None:
            continue

        while True:
            print("\n--- Inventory Management System ---")
            print("1. View Products")
            if role == "Admin":
                print("2. Add Product")
                print("3. Edit Product")
                print("4. Delete Product")
                print("5. Adjust Stock")
            print("6. Search Product")
            print("7. Logout")
            print("8. Exit Program")

            choice = input("Enter your choice: ")

            if choice == "1":
                inventory.view_products()
            elif choice == "2" and role == "Admin":
                product_id = input("Enter product ID: ")
                name = input("Enter product name: ")
                category = input("Enter category: ")
                try:
                    price = float(input("Enter price: "))
                    stock_quantity = int(input("Enter stock quantity: "))
                    inventory.add_product(product_id, name, category, price, stock_quantity)
                except ValueError:
                    print("Invalid input. Price and stock quantity should be numbers.")
            elif choice == "3" and role == "Admin":
                product_id = input("Enter product ID to edit: ")
                name = input("Enter new name (leave blank to skip): ")
                category = input("Enter new category (leave blank to skip): ")
                price = input("Enter new price (leave blank to skip): ")
                stock_quantity = input("Enter new stock quantity (leave blank to skip): ")
                try:
                    price = float(price) if price else None
                    stock_quantity = int(stock_quantity) if stock_quantity else None
                    inventory.edit_product(product_id, name, category, price, stock_quantity)
                except ValueError:
                    print("Invalid input. Price and stock quantity should be numbers.")
            elif choice == "4" and role == "Admin":
                product_id = input("Enter product ID to delete: ")
                inventory.delete_product(product_id)
            elif choice == "5" and role == "Admin":
                product_id = input("Enter product ID to adjust stock: ")
                try:
                    quantity = int(input("Enter quantity to adjust (+ or -): "))
                    inventory.adjust_stock(product_id, quantity)
                except ValueError:
                    print("Invalid input. Quantity should be a number.")
            elif choice == "6":
                search_term = input("Enter product name or category to search: ")
                inventory.search_product(search_term)
            elif choice == "7":
                print("Logging out...")
                break
            elif choice == "8":
                print("Exiting program. Goodbye!")
                return
            else:
                print("Invalid choice or insufficient permissions.")

if __name__ == "__main__":
    main()
