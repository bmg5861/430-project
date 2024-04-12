import tkinter as tk
from tkinter import ttk
# import cx_Oracle here if you're using it

class CustomersPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        tk.Label(self, text="Customers Page").pack(pady=10)

        # Search Bar
        search_frame = tk.Frame(self)
        search_frame.pack(fill='x', padx=10)
        self.search_var = tk.StringVar()
        tk.Entry(search_frame, textvariable=self.search_var).pack(side='left', fill='x', expand=True, padx=(0, 5))
        tk.Button(search_frame, text="Search", command=self.search_customer).pack(side='right')

        # Table for Customers
        self.tree = ttk.Treeview(self, columns=('CustomerID', 'FirstName', 'LastName', 'Email', 'PhoneNumber'), show='headings')
        for col in self.tree['columns']:
            self.tree.heading(col, text=col)
        self.tree.pack(expand=True, fill='both', padx=10, pady=10)

        # Add Scrollbar
        scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')

        # Load Customers into the Table
        self.load_customers()

        # Buttons Frame
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(fill='x', padx=10, pady=(0, 10))
        tk.Button(buttons_frame, text="Add Customer", command=self.add_customer).pack(side='left')
        tk.Button(buttons_frame, text="Edit Selected Customer", command=self.edit_customer).pack(side='right')

        # Enhanced Back to Home button with styling
        back_button = tk.Button(self, text="← Back to Home", command=lambda: controller.show_frame("HomePage"))
        back_button.pack(pady=10)
        back_button.config(font=("Arial", 12), bg="#4CAF50", fg="white", bd=0, padx=10, pady=5)

        back_button.bind("<Enter>", lambda e: back_button.config(bg="#45a049"))
        back_button.bind("<Leave>", lambda e: back_button.config(bg="#4CAF50"))

    def load_customers(self):
        # Fetch customers from the database and insert them into the Treeview
        # Assume get_customers is a function that fetches customer data from the database
        for customer in self.get_customers():
            self.tree.insert('', 'end', values=customer)

    def add_customer(self):
        # Functionality to add a new customer to the database
        # This should bring up a form where you can enter customer details, and then insert them into the database
        pass

    def edit_customer(self):
        # Functionality to edit an existing customer in the database
        # This should get the selected item's ID, bring up a form with current details filled in, and update upon submission
        pass

    def search_customer(self):
        # Functionality to search the database for customers matching the search criteria
        # This should update the Treeview with the search results
        pass

    def get_customers(self):
        # Placeholder for a database query to get all customers
        # You would replace this with your actual database query
        return [
            # Replace this with real data fetched from the database
            (1, 'John', 'Doe', 'john.doe@example.com', '123-456-7890'),
            (2, 'Jane', 'Smith', 'jane.smith@example.com', '098-765-4321'),
        ]