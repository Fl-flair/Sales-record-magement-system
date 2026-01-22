sales_records = []

def add_sale():
    item = input("Enter item sold: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))
    total = quantity * price
    sales_records.append({
        "item": item,
        "quantity": quantity,
        "total": total
    })
    print("Sale recorded successfully")

def view_sales():
    if not sales_records:
        print("No sales records found")
    else:
        for s in sales_records:
            print("Item:", s["item"])
            print("Quantity:", s["quantity"])
            print("Total Amount:", s["total"])
            print("------------------")

def main():
    while True:
        print("1. Add Sale")
        print("2. View Sales")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_sale()
        elif choice == "2":
            view_sales()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()
