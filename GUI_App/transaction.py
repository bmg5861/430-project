import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
import db

connection = db.Connection()

class TransactionsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        tk.Label(self, text="Transactions Management", font=("Arial", 16)).pack(pady=10)

        # Search Bar
        search_frame = tk.Frame(self)
        search_frame.pack(fill='x', padx=10)
        self.search_var = tk.StringVar()
        tk.Entry(search_frame, textvariable=self.search_var).pack(side='left', fill='x', expand=True, padx=(0, 5))
        tk.Button(search_frame, text="Search", command=self.search_transactions).pack(side='right')

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
        columns = ('TransactionID', 'CustomerID', 'ItemType', 'ISBN', 'TransactionType', 'TransactionDate')
        tree = ttk.Treeview(self, columns=columns, show='headings')
        for col in columns:
            tree.heading(col, text=col.replace('ID', ' ID').replace('Type', ' Type').replace('Date', ' Date'))
            tree.column(col, anchor='center')
        tree.pack(expand=True, fill='both', padx=10, pady=10)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self, orient='vertical', command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')

        return tree

    def load_transactions(self):
        """Fetches all transactions from the database and displays them in the treeview."""
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT t.TransactionID, t.CustomerID, 
                        i.ItemType,
                        CASE i.ItemType 
                            WHEN 'book' THEN b.ISBN
                            WHEN 'serial' THEN s.ISBN
                            WHEN 'dvd' THEN d.ISBN
                        END AS ISBN,
                        t.TransactionType, TO_CHAR(t.TransactionDate, 'YYYY-MM-DD') AS TransactionDate
                    FROM Transactions t
                    JOIN ItemLoans i ON t.LoanID = i.LoanID
                    LEFT JOIN Books b ON i.ItemID = b.BookID AND i.ItemType = 'book'
                    LEFT JOIN Serials s ON i.ItemID = s.SerialID AND i.ItemType = 'serial'
                    LEFT JOIN DVDs d ON i.ItemID = d.DVDID AND i.ItemType = 'dvd'
                """)
                rows = cursor.fetchall()

            self.transaction_tree.delete(*self.transaction_tree.get_children())
            for row in rows:
                self.transaction_tree.insert('', 'end', values=row)
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to load transactions: {str(e)}")
            print(e)

    def search_transactions(self):
        """Searches transactions based on the provided search term in the search bar."""
        search_term = self.search_var.get().strip()
        if not search_term:
            messagebox.showwarning("Search", "Please enter a search term.")
            return

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT t.TransactionID, t.CustomerID, t.ItemType, 
                        CASE t.ItemType 
                            WHEN 'book' THEN b.ISBN
                            WHEN 'serial' THEN s.ISBN
                            WHEN 'dvd' THEN d.ISBN
                        END AS ISBN,
                        t.TransactionType, t.TransactionDate
                    FROM Transactions t
                    LEFT JOIN Books b ON t.ItemID = b.BookID AND t.ItemType = 'book'
                    LEFT JOIN Serials s ON t.ItemID = s.SerialID AND t.ItemType = 'serial'
                    LEFT JOIN DVDs d ON t.ItemID = d.DVDID AND t.ItemType = 'dvd'
                    WHERE UPPER(t.TransactionType) LIKE UPPER(:1) OR UPPER(b.ISBN) LIKE UPPER(:1) OR UPPER(s.ISBN) LIKE UPPER(:1) OR UPPER(d.ISBN) LIKE UPPER(:1)
                """, ('%' + search_term + '%',))
                rows = cursor.fetchall()

            self.transaction_tree.delete(*self.transaction_tree.get_children())
            for row in rows:
                self.transaction_tree.insert('', 'end', values=row)
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to search transactions: {str(e)}")
            print(e)

    def handle_checkout(self):
    #"""Handles checkout operations for selected items."""
        item = self.get_selected_item()
        if item:
            customer_id = simpledialog.askstring("Input", "Enter Customer ID:")
            item_id = item[0]  # Assuming the first value in the item tuple is the item ID
            item_type = item[2]  # Assuming the third value is the item type

            if not customer_id:
                messagebox.showwarning("Input Error", "Customer ID is required for checkout.")
                return

            try:
                with connection.cursor() as cursor:
                    cursor.execute("""
                        INSERT INTO Transactions (CustomerID, LoanID, TransactionType, TransactionDate)
                        VALUES (:1, :2, 'checkout', SYSDATE)
                    """, (customer_id, item_id))
                    connection.commit()
                messagebox.showinfo("Checkout", f"Item {item_id} checked out successfully to customer {customer_id}.")
            except Exception as e:
                messagebox.showerror("Database Error", f"Failed to checkout item: {str(e)}")
                print(e)

    def handle_return(self):
        """Handles return operations for selected items."""
        item = self.get_selected_item()
        if item:
            transaction_id = item[0]  # Assuming the first value in the item tuple is the transaction ID

            try:
                with connection.cursor() as cursor:
                    cursor.execute("""
                        UPDATE Transactions
                        SET TransactionType = 'return', TransactionDate = SYSDATE
                        WHERE TransactionID = :1 AND TransactionType = 'checkout'
                    """, (transaction_id,))
                    connection.commit()
                messagebox.showinfo("Return", f"Item associated with transaction {transaction_id} returned successfully.")
            except Exception as e:
                messagebox.showerror("Database Error", f"Failed to return item: {str(e)}")
                print(e)

    def handle_renew(self):
        """Handles renew operations for selected items."""
        item = self.get_selected_item()
        if item:
            transaction_id = item[0]  # Assuming the first value in the item tuple is the transaction ID

            try:
                with connection.cursor() as cursor:
                    cursor.execute("""
                        UPDATE Transactions
                        SET TransactionDate = SYSDATE
                        WHERE TransactionID = :1 AND TransactionType = 'checkout'
                    """, (transaction_id,))
                    connection.commit()
                messagebox.showinfo("Renew", f"Transaction {transaction_id} renewed successfully.")
            except Exception as e:
                messagebox.showerror("Database Error", f"Failed to renew transaction: {str(e)}")
                print(e)
