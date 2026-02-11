# FrancisTechKing Pharmacy - Pro Edition
# Built in Duayaw Nkwanta

def start_pharmacy():
    print("---------------------------------")
    print("   FRANCIS TECH KING PHARMACY   ")
    print("---------------------------------")
    
    inventory = {"Paracetamol": 5, "Vitamin C": 10, "Amoxicillin": 20}
    money_made = 0

    while True:
        print(f"\nTotal Money Earned: GH₵ {money_made}")
        print("1. View Stock")
        print("2. Make a Sale")
        print("3. Exit System")
        
        choice = input("\nSelect an option (1-3): ")

        if choice == "1":
            for drug, price in inventory.items():
                print(f"- {drug}: GH₵ {price}")
        
        elif choice == "2":
            drug_name = input("Enter drug name: ")
            if drug_name in inventory:
                money_made += inventory[drug_name]
                print(f"✅ SOLD! Added GH₵ {inventory[drug_name]} to balance.")
            else:
                print("❌ Drug not found!")
        
        elif choice == "3":
            print("Closing System. Stay healthy King!")
            break
        else:
            print("Invalid choice, try again.")

start_pharmacy()
