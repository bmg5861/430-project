import tkinter as tk
from tkinter import ttk
# import cx_Oracle here if you're using it

class StockPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        tk.Label(self, text="Stock Management Page").pack(pady=10)

        # Search Bar
        search_frame = tk.Frame(self)
        search_frame.pack(fill='x', padx=10)
        self.search_var = tk.StringVar()
        tk.Entry(search_frame, textvariable=self.search_var).pack(side='left', fill='x', expand=True, padx=(0, 5))
        tk.Button(search_frame, text="Search", command=self.search_items).pack(side='right')

        # Notebook (Tabbed Interface)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        # Tabs
        self.books_tab = ttk.Frame(self.notebook)
        self.serials_tab = ttk.Frame(self.notebook)
        self.dvds_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.books_tab, text='Books')
        self.notebook.add(self.serials_tab, text='Serials')
        self.notebook.add(self.dvds_tab, text='DVDs')

        # Tables
        self.book_tree = self.create_item_table(self.books_tab, ("BookID", "Title", "ISBN", "Author", "Year Published"))
        self.serial_tree = self.create_item_table(self.serials_tab, ("SerialID", "Title", "Volume", "ISBN", "Year Published"))
        self.dvd_tree = self.create_item_table(self.dvds_tab, ("DVDID", "Title", "ISBN", "Author", "Year Published"))

        # Buttons Frame for each Tab
        self.create_buttons_frame(self.books_tab, self.book_tree, "book").pack(fill='x', padx=10, pady=(0, 10))
        self.create_buttons_frame(self.serials_tab, self.serial_tree, "serial").pack(fill='x', padx=10, pady=(0, 10))
        self.create_buttons_frame(self.dvds_tab, self.dvd_tree, "dvd").pack(fill='x', padx=10, pady=(0, 10))

        # Enhanced Back to Home button with styling
        back_button = tk.Button(self, text="← Back to Home", command=lambda: controller.show_frame("HomePage"))
        back_button.pack(pady=10)
        back_button.config(font=("Arial", 12), bg="#4CAF50", fg="white", bd=0, padx=10, pady=5)
        back_button.bind("<Enter>", lambda e: back_button.config(bg="#45a049"))
        back_button.bind("<Leave>", lambda e: back_button.config(bg="#4CAF50"))

    def create_item_table(self, tab, columns):
        tree = ttk.Treeview(tab, columns=columns, show='headings')
        for col in columns:
            tree.heading(col, text=col)
        tree.pack(expand=True, fill='both')

        # Scrollbar
        scrollbar = ttk.Scrollbar(tab, orient='vertical', command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')

        return tree

    def create_buttons_frame(self, tab, tree, category):
        buttons_frame = tk.Frame(tab)
        tk.Button(buttons_frame, text=f"Add {category.title()}", command=lambda: self.add_item(category)).pack(side='left')
        tk.Button(buttons_frame, text=f"Edit Selected {category.title()}", command=lambda: self.edit_item(tree, category)).pack(side='left')
        tk.Button(buttons_frame, text=f"Remove Selected {category.title()}", command=lambda: self.remove_item(tree, category)).pack(side='right')
        return buttons_frame

    def load_items(self):
        # Load books, serials, and DVDs from the database
        # You would replace this with actual database queries to fetch the items
        pass

    def add_item(self, category):
        # Open form to add new item to the category
        pass

    def edit_item(self, tree, category):
        # Open form to edit the selected item in the category
        pass

    def remove_item(self, tree, category):
        # Remove the selected item from the category
        pass

    def search_items(self):
        # Search and filter items in the tables
        pass