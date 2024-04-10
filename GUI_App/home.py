import tkinter as tk
from stock import StockPage
from customers import CustomersPage
from transaction import TransactionsPage

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='#eeeeee')  # Set the background to light gray
        self.controller = controller

        # Header
        header_frame = tk.Frame(self, bg='#1155cc')
        header_frame.pack(side='top', fill='x')
        header_label = tk.Label(header_frame, text='Library Management System', bg='#1155cc', fg='white', font=('Arial', 24, 'bold'))
        header_label.pack(pady=20)

        # Main Content Area
        content_frame = tk.Frame(self, bg='#eeeeee')
        content_frame.pack(expand=True, fill='both', padx=50, pady=30)

        btn_manage_stock = tk.Button(content_frame, text='Manage Stock', font=('Arial', 14), bg='#1155cc', fg='white', bd=0,
                                     padx=20, pady=10, command=lambda: controller.show_frame('StockPage'))
        btn_manage_stock.pack(pady=10)

        btn_browse_customers = tk.Button(content_frame, text='Browse Customers', font=('Arial', 14), bg='#1155cc', fg='white', bd=0,
                                         padx=20, pady=10, command=lambda: controller.show_frame('CustomersPage'))
        btn_browse_customers.pack(pady=10)

        btn_handle_transactions = tk.Button(content_frame, text='Handle Transactions', font=('Arial', 14), bg='#1155cc', fg='white', bd=0,
                                            padx=20, pady=10, command=lambda: controller.show_frame('TransactionsPage'))
        btn_handle_transactions.pack(pady=10)

        # Footer
        footer_frame = tk.Frame(self, bg='gray')
        footer_frame.pack(side='bottom', fill='x')
        footer_label = tk.Label(footer_frame, text='© 2024 Library Management System', bg='gray', fg='white', font=('Arial', 12))
        footer_label.pack(pady=10)

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Library Management Home')
        self.geometry('800x600')  # Set a default size for the application window
        self.frames = {}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.config(bg='#eeeeee')  # Set the container background to match the theme

        # Initializing and storing frames
        for F in (HomePage, StockPage, CustomersPage, TransactionsPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        '''Raise the frame of the given page name to the top of the stack'''
        if page_name in self.frames:
            frame = self.frames[page_name]
            frame.tkraise()
        else:
            print(f"Page {page_name} not found.")

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
