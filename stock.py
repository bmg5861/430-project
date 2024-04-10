# look at all of the stock and do crud operations

import tkinter as tk

class StockPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        tk.Label(self, text="Stock Management Page").pack(pady=10)

        # Buttons for Stock Management operations
        tk.Button(self, text="Add Item", command=self.add_item).pack()
        tk.Button(self, text="Edit Item", command=self.edit_item).pack()
        tk.Button(self, text="Remove Item", command=self.remove_item).pack()
        tk.Button(self, text="Search Items", command=self.search_items).pack()

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


    def add_item(self):
        # Placeholder method for adding an item
        print("Add item functionality goes here.")

    def edit_item(self):
        # Placeholder method for editing an item
        print("Edit item functionality goes here.")

    def remove_item(self):
        # Placeholder method for removing an item
        print("Remove item functionality goes here.")

    def search_items(self):
        # Placeholder method for searching items
        print("Search items functionality goes here.")