# FrancisTechKing Pharmacy - Database Edition

def save_sale(drug, price):
    # This part opens a file and writes the sale down forever
    with open("sales_report.txt", "a") as file:
        file.write(f"Sold: {drug} for GH₵ {price}\n")

def start_pharmacy():
    print("--- FRANCIS TECH KING PHARMACY ---")
    inventory = {"Paracetamol": 5, "Vitamin C": 10, "Amoxicillin": 20}
    money_made = 0

    while True:
        print(f"\nTotal Money Earned: GH₵ {money_made}")
        print("1. View Stock | 2. Make a Sale | 3. View Saved Receipts | 4. Exit")
        
        choice = input("\nSelect (1-4): ")

        if choice == "1":
            for drug, price in inventory.items():
                print(f"- {drug}: GH₵ {price}")
        
        elif choice == "2":
            drug_name = input("Enter drug name: ")
            if drug_name in inventory:
                price = inventory[drug_name]
                money_made += price
                save_sale(drug_name, price) # Calling the save function!
                print(f"✅ SOLD! Saved to Receipt Book.")
            else:
                print("❌ Drug not found!")

        elif choice == "3":
            print("\n--- SAVED RECEIPTS ---")
            try:
                with open("sales_report.txt", "r") as file:
                    print(file.read())
            except FileNotFoundError:
                print("No sales recorded yet.")

        elif choice == "4":
            break

start_pharmacy()
