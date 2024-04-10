
# Browse the list of the customers
import tkinter as tk

class CustomersPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        tk.Label(self, text="Customers Page").pack(pady=10)
        
        # Example functionalities for customer management
        tk.Button(self, text="View Customers", command=self.view_customers).pack()
        tk.Button(self, text="Add Customer", command=self.add_customer).pack()
        tk.Button(self, text="Edit Customer", command=self.edit_customer).pack()
        tk.Button(self, text="Search for Customer", command=self.search_customer).pack()

        # Enhanced Back to Home button with styling
        back_button = tk.Button(self, text="← Back to Home", command=lambda: controller.show_frame("HomePage"))
        back_button.pack(pady=10)
        back_button.config(font=("Arial", 12), bg="#4CAF50", fg="white", bd=0, padx=10, pady=5)

        def on_enter(e):
            back_button.config(bg="#45a049")

        def on_leave(e):
            back_button.config(bg="#4CAF50")

        back_button.bind("<Enter>", on_enter)
        back_button.bind("<Leave>", on_leave)


    def view_customers(self):
        print("View customers functionality goes here.")

    def add_customer(self):
        print("Add customer functionality goes here.")

    def edit_customer(self):
        print("Edit customer details functionality goes here.")

    def search_customer(self):
        print("Search for customer functionality goes here.")







'''''

# Browse the list of the customers
import tkinter as tk

class CustomersPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        tk.Label(self, text="Customers Page").pack(pady=10)
        
        # Example functionalities for customer management
        tk.Button(self, text="View Customers", command=self.view_customers).pack()
        tk.Button(self, text="Add Customer", command=self.add_customer).pack()
        tk.Button(self, text="Edit Customer", command=self.edit_customer).pack()
        tk.Button(self, text="Search for Customer", command=self.search_customer).pack()

        # Enhanced Back to Home button with styling
        back_button = tk.Button(self, text="← Back to Home", command=lambda: controller.show_frame("HomePage"))
        back_button.pack(pady=10)
        back_button.config(font=("Arial", 12), bg="#4CAF50", fg="white", bd=0, padx=10, pady=5)

        def on_enter(e):
            back_button.config(bg="#45a049")

        def on_leave(e):
            back_button.config(bg="#4CAF50")

        back_button.bind("<Enter>", on_enter)
        back_button.bind("<Leave>", on_leave)


    def view_customers(self):
        print("View customers functionality goes here.")

    def add_customer(self):
        print("Add customer functionality goes here.")

    def edit_customer(self):
        print("Edit customer details functionality goes here.")

    def search_customer(self):
        print("Search for customer functionality goes here.")


'''''