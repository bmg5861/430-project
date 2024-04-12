import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# import cx_Oracle here if you're using it

class TransactionsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        tk.Label(self, text="Transactions Management").pack(pady=10)

        # Search Bar
        search_frame = tk.Frame(self)
        search_frame.pack(fill='x', padx=10)
        self.search_var = tk.StringVar()
        tk.Entry(search_frame, textvariable=self.search_var).pack(side='left', fill='x', expand=True, padx=(0, 5))
        tk.Button(search_frame, text="Search", command=self.search_items).pack(side='right')

        # Transaction Table
        self.transaction_tree = self.create_transaction_table()
        self.load_transactions()

        # Transaction buttons
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text='Checkout', command=self.handle_checkout).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text='Return', command=self.handle_return).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text='Renew', command=self.handle_renew).pack(side=tk.LEFT, padx=5)

        # Enhanced Back to Home button with styling
        back_button = tk.Button(self, text="← Back to Home", command=lambda: controller.show_frame("HomePage"))
        back_button.pack(pady=10)
        back_button.config(font=("Arial", 12), bg="#4CAF50", fg="white", bd=0, padx=10, pady=5)
        back_button.bind("<Enter>", lambda e: back_button.config(bg="#45a049"))
        back_button.bind("<Leave>", lambda e: back_button.config(bg="#4CAF50"))

    def create_transaction_table(self):
        columns = ('Title', 'ISBN', 'Borrow Date', 'Return Date')
        tree = ttk.Treeview(self, columns=columns, show='headings')
        tree.heading('Title', text='Title')
        tree.heading('ISBN', text='ISBN')
        tree.heading('Borrow Date', text='Borrow Date')
        tree.heading('Return Date', text='Return Date')
        tree.pack(expand=True, fill='both', padx=10, pady=10)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self, orient='vertical', command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')

        return tree

    def load_transactions(self):
        # Replace this with actual data fetching logic
        for item in self.get_all_items():
            self.transaction_tree.insert('', 'end', values=(item['title'], item['isbn'], item['borrow date'], item['return date']))

    def get_selected_item(self):
        selection = self.transaction_tree.selection()
        if selection:
            return self.transaction_tree.item(selection[0])['values']
        else:
            messagebox.showwarning("Selection", "No item selected")
            return None

    def handle_checkout(self):
        item = self.get_selected_item()
        if item:
            # Implement the checkout functionality here
            pass

    def handle_return(self):
        item = self.get_selected_item()
        if item:
            # Implement the return functionality here
            pass

    def handle_renew(self):
        item = self.get_selected_item()
        if item:
            # Implement the renew functionality here
            pass

    def search_items(self):
        # Filter and update the table with search results
        pass

    def get_all_items(self):
        # Placeholder for a database query to get all items (books, serials, DVDs)
        return [
            {'title': 'Example Book Title', 'isbn': '1234567890123', 'borrow date': '1/2/12', 'return date': 'Never'},
            {'title': 'Example DVD Title', 'isbn': '9876543210987', 'borrow date': '1/3/12', 'return date': 'Maybe'},
            # ... add more items
        ]

# The actual transaction logic would interact with the database to check out, return, or renew items.