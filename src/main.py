import os


class Product:

    def __init__(self, pid, name, qty, price):
        self.pid = pid
        self.name = name
        self.qty = qty
        self.price = price


class Inventory:

    def __init__(self, filename="data/inventory.txt"):
        self.filename = filename
        self.products = {}
        self.load_inventory()

    def add_product(self, pid, name, qty, price):
        self.products[pid] = Product(pid, name, qty, price)
        self.save_inventory()

    def update_stock(self, pid, qty):
        if pid in self.products:
            self.products[pid].qty += qty
            self.save_inventory()
        else:
            print("\nProduct ID not found!")

    def search(self, name):
        found = False
        print("\n--- Search Results ---")
        for p in self.products.values():
            if name.lower() in p.name.lower():
                print(f"{p.pid} - {p.name} | Qty: {p.qty} | Price: {p.price}")
                found = True
        if not found:
            print("No products found.")

    def save_inventory(self):
        # Siguraduhing gawa ang 'data' folder bago mag-save para iwas error
        dirname = os.path.dirname(self.filename)
        if dirname and not os.path.exists(dirname):
            os.makedirs(dirname)

        with open(self.filename, "w") as f:
            for p in self.products.values():
                f.write(f"{p.pid},{p.name},{p.qty},{p.price}\n")

    def load_inventory(self):
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    # Siguraduhing may laman ang linya bago i-split
                    if line.strip():
                        pid, name, qty, price = line.strip().split(",")
                        self.products[pid] = Product(
                            pid, name, int(qty), float(price)
                        )
        except FileNotFoundError:
            pass


def main():
    inv = Inventory()
    while True:
        print("\n1. Add Product\n2. Update Stock\n3. Search Product\n4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            pid = input("Product ID: ")
            name = input("Name: ")
            try:
                qty = int(input("Quantity: "))
                price = float(input("Price: "))
                inv.add_product(pid, name, qty, price)
                print("\nProduct added/updated successfully.")
            except ValueError:
                print("\nInvalid input for Quantity or Price.")

        elif choice == "2":
            pid = input("Product ID: ")
            try:
                qty = int(input("Quantity to Add: "))
                inv.update_stock(pid, qty)
                print("\nStock updated successfully.")
            except ValueError:
                print("\nInvalid quantity input.")

        elif choice == "3":
            name = input("Search Name: ")
            inv.search(name)

        elif choice == "4":
            print("\nExiting inventory system...")
            break
        else:
            print("\nInvalid choice. Try again.")


if __name__ == "__main__":
    main()