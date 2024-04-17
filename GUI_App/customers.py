import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import db

connection = db.Connection()

class CustomersPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        tk.Label(self, text="Customers Page", font=("Arial", 16)).pack(pady=10)
        
        # Creating the Treeview widget to display the customer data
        self.tree = ttk.Treeview(self, columns=("CustomerID", "FirstName", "LastName", "Email", "PhoneNumber"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        self.tree.pack(expand=True, fill='both', pady=10)

        # Search bar setup
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(self, textvariable=self.search_var)
        self.search_entry.pack(pady=5)
        self.search_button = tk.Button(self, text="Search for Customer", command=self.search_customer)
        self.search_button.pack()

        # Buttons for Add and Edit Customer
        tk.Button(self, text="Add Customer", command=self.add_customer).pack()
        tk.Button(self, text="Edit Customer", command=self.edit_customer).pack()
        tk.Button(self, text="Remove Customer", command=self.remove_customer).pack()

        # Enhanced Back to Home button with styling
        back_button = tk.Button(self, text="← Back to Home", command=lambda: controller.show_frame("HomePage"))
        back_button.pack(pady=10)
        back_button.config(font=("Arial", 12), bg="#4CAF50", fg="white", bd=0, padx=10, pady=5)
        back_button.bind("<Enter>", lambda e: back_button.config(bg="#45a049"))
        back_button.bind("<Leave>", lambda e: back_button.config(bg="#4CAF50"))

        # Load initial customer data
        self.load_customers()

    def load_customers(self):
        """Load customer data from the database and display in the treeview."""
        with connection.cursor() as cursor:
            cursor.execute("SELECT CustomerID, FirstName, LastName, Email, PhoneNumber FROM Customers")
            rows = cursor.fetchall()

        # Clear existing data in the treeview
        self.tree.delete(*self.tree.get_children())
        
        # Insert new data
        for row in rows:
            self.tree.insert('', 'end', values=row)

    def add_customer(self):
        first_name = simpledialog.askstring("Input", "Enter first name:")
        last_name = simpledialog.askstring("Input", "Enter last name:")
        email = simpledialog.askstring("Input", "Enter email:")
        phone_number = simpledialog.askstring("Input", "Enter phone number:")

        if not all([first_name, last_name, email, phone_number]):
            messagebox.showerror("Error", "All fields are required.")
            return

        add_query = """
            INSERT INTO Customers (FirstName, LastName, Email, PhoneNumber)
            VALUES (:1, :2, :3, :4)
        """
        try:
            with connection.cursor() as cursor:
                cursor.execute(add_query, [first_name, last_name, email, phone_number])
                connection.commit()
                messagebox.showinfo("Success", "Customer added successfully")
                self.load_customers()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add customer: {e}")
            print(e)

    def edit_customer(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "No customer selected")
            return

        values = self.tree.item(selected_item)['values']
        customer_id = values[0]

        # Example input from user
        first_name = simpledialog.askstring("Input", "Enter new first name:", initialvalue=values[1])
        last_name = simpledialog.askstring("Input", "Enter new last name:", initialvalue=values[2])
        email = simpledialog.askstring("Input", "Enter new email:", initialvalue=values[3])
        phone_number = simpledialog.askstring("Input", "Enter new phone number:", initialvalue=values[4])

        edit_query = """
            UPDATE Customers
            SET FirstName = :1, LastName = :2, Email = :3, PhoneNumber = :4
            WHERE CustomerID = :5
        """
        try:
            with connection.cursor() as cursor:
                cursor.execute(edit_query, [first_name, last_name, email, phone_number, customer_id])
                connection.commit()
                messagebox.showinfo("Success", "Customer updated successfully")
                self.load_customers()
        except Exception as e:
            print(e)

    def remove_customer(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "No customer selected")
            return

        customer_id = self.tree.item(selected_item)['values'][0]
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this customer?"):
            remove_query = "DELETE FROM Customers WHERE CustomerID = :1"
            try:
                with connection.cursor() as cursor:
                    cursor.execute(remove_query, [customer_id])
                    connection.commit()
                    messagebox.showinfo("Success", "Customer removed successfully")
                    self.load_customers()
            except Exception as e:
                print(e)
        
    def search_customer(self):
        search_term = self.search_var.get()
        # Create a parameterized SQL query
        searchquery = """
            SELECT * FROM Customers 
            WHERE UPPER(FirstName) LIKE UPPER(:search) 
            OR UPPER(LastName) LIKE UPPER(:search) 
            OR UPPER(Email) LIKE UPPER(:search) 
            OR UPPER(PhoneNumber) LIKE UPPER(:search)
        """
        search = connection.cursor()
        # Execute the query with a dictionary to safely inject the search term
        search.execute(searchquery, {'search': '%' + search_term + '%'})

        rows = search.fetchall()

        # Clear existing data in the treeview
        self.tree.delete(*self.tree.get_children())

        search.close()
        

          # Depending on your need, this might not be necessary if just printing

# Example of how to instantiate and use the frame within a Tkinter application
# This assumes there is a Tk root window or another parent frame named `controller` that has a method `show_frame`

# root = tk.Tk()
# cp = CustomersPage(root, controller)
# cp.pack(expand=True, fill='both')
# root.mainloop()