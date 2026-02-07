# FrancisTechKing - Master Pharmacy System 2026

def check_stock(name, current_quantity):
    if current_quantity < 5:
        print(f"!!! ALERT: {name} is almost finished! Only {current_quantity} left.")
    else:
        print(f"STOCKS OK: {name} level is healthy.")

# Your Database from your notes
pharmacy_stock = {
    "Insulin": 10,
    "Paracetamol": 3,
    "Arthemether": 20
}

while True:
    drug = input("\nDrug name (or 'exit'): ")
    if drug == "exit":
        break
        
    if drug in pharmacy_stock:
        # Call the function from your notes
        check_stock(drug, pharmacy_stock[drug])
        
        try:
            sold = int(input(f"How many {drug} sold? "))
            pharmacy_stock[drug] -= sold
            print(f"New {drug} stock: {pharmacy_stock[drug]}")
        except ValueError:
            print("❌ Use number only!")
    else:
        print("Item not in database.")
