from login_module import connect_db, login

conn = connect_db()
cursor = conn.cursor()

def create_product():
    product_id = input("Enter product ID: ")
    cursor.execute("SELECT * FROM stock WHERE id=%s", (product_id,))
    if cursor.fetchone():
        print("Product with this ID already exists.\n")
        return
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    category = input("Enter category (electronic/fashion/grocery): ").lower()
    if category not in ['electronic', 'fashion', 'grocery']:
        print("Invalid category.\n")
        return
    cursor.execute("INSERT INTO stock (id, name_product, quantity, price, category) VALUES (%s, %s, %s, %s, %s)",
                   (product_id, name, quantity, price, category))
    conn.commit()
    print("Product added successfully.\n")

def delete_product():
    product_id = input("Enter the ID of the product you want to delete: ")
    cursor.execute("DELETE FROM stock WHERE id=%s", (product_id,))
    if cursor.rowcount == 0:
        print("Product not found.\n")
    else:
        conn.commit()
        print("Product deleted successfully.\n")

def edit_quantity():
    product_id = input("Enter the ID of the product you want to update: ")
    cursor.execute("SELECT * FROM stock WHERE id=%s", (product_id,))
    if cursor.fetchone() is None:
        print("Product not found.\n")
        return
    
    new_quantity = int(input("Enter the new quantity: "))
    cursor.execute("UPDATE stock SET quantity=%s WHERE id=%s", (new_quantity, product_id))
    conn.commit()
    print("Quantity updated successfully.\n")

def view_by_category():
    category = input("Enter the category to view (electronic/fashion/grocery): ").lower()
    if category not in ['electronic', 'fashion', 'grocery']:
        print("Invalid category.\n")
        return
    cursor.execute("SELECT * FROM stock WHERE category=%s", (category,))
    rows = cursor.fetchall()
    if not rows:
        print("No products found in this category.\n")
    else:
        print(f"\n--- Products in category: {category} ---")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Quantity: {row[2]}, Price: {row[3]}")
        print("")

def main_menu():
    while True:
        print("Welcome to the Stock Management System!")
        print("Please select an option below:")
        print("1. Create a new product")
        print("2. Delete a product (by ID)")
        print("3. Edit product quantity (by ID)")
        print("4. View products by category")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            create_product()
        elif choice == '2':
            delete_product()
        elif choice == '3':
            edit_quantity()
        elif choice == '4':
            view_by_category()
        elif choice == '5':
            print("Happy shopping!!!")
            break
        else:
            print("Invalid choice. Please try again.\n")
if login(cursor):
    main_menu()

cursor.close()
conn.close()
