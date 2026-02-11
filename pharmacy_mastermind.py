# FrancisTechKing Pharmacy - Mastermind Edition
import os

def save_sale(drug, price):
    with open("sales_report.txt", "a") as file:
        file.write(f"Sold: {drug} for GH₵ {price}\n")

def start_pharmacy():
    # Starting inventory
    inventory = {"Paracetamol": 5, "Vitamin C": 10}
    money_made = 0

    while True:
        print(f"\n--- KING'S SYSTEM | Money: GH₵ {money_made} ---")
        print("1. View Stock")
        print("2. Sell Medicine")
        print("3. Add New Stock (Admin)")
        print("4. View/Clear Receipts")
        print("5. Exit")
        
        choice = input("\nSelect (1-5): ")

        if choice == "1":
            for drug, price in inventory.items():
                print(f"- {drug}: GH₵ {price}")
        
        elif choice == "2":
            name = input("Drug name: ")
            if name in inventory:
                price = inventory[name]
                money_made += price
                save_sale(name, price)
                print("✅ Recorded.")
            else: print("❌ Not in stock.")

        elif choice == "3":
            new_drug = input("Enter new drug name: ")
            new_price = int(input("Enter price in GH₵: "))
            inventory[new_drug] = new_price
            print(f"📦 Added {new_drug} to shelf.")

        elif choice == "4":
            action = input("Type 'V' to View or 'C' to Clear: ").upper()
            if action == 'V':
                if os.path.exists("sales_report.txt"):
                    with open("sales_report.txt", "r") as f: print(f.read())
                else: print("Book is empty.")
            elif action == 'C':
                if os.path.exists("sales_report.txt"):
                    os.remove("sales_report.txt")
                    print("🧹 Book cleared!")

        elif choice == "5":
            break

start_pharmacy()
