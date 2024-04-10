import tkinter as tk
from stock import StockPage
from customers import CustomersPage
from transaction import TransactionsPage

class RoundedButton(tk.Canvas):
    def __init__(self, parent, text, command=None, width=200, height=50, corner_radius=20, color="#6495ED", text_color="black"):
        super().__init__(parent, borderwidth=0, highlightthickness=0, bg='#18181A', width=width, height=height)
        self.command = command

        # Draw rounded rectangle
        self.create_oval((0, 0, corner_radius * 2, corner_radius * 2), fill=color, outline=color)
        self.create_oval((width - corner_radius * 2, 0, width, corner_radius * 2), fill=color, outline=color)
        self.create_oval((0, height - corner_radius * 2, corner_radius * 2, height), fill=color, outline=color)
        self.create_oval((width - corner_radius * 2, height - corner_radius * 2, width, height), fill=color, outline=color)
        self.create_rectangle((0, corner_radius, width, height - corner_radius), fill=color, outline=color)
        self.create_rectangle((corner_radius, 0, width - corner_radius, height), fill=color, outline=color)

        # Add text
        self.create_text(width / 2, height / 2, text=text, fill=text_color, font=('Arial', 16, 'bold'))

        # Bind click event
        self.bind("<Button-1>", self._on_click)

    def _on_click(self, event):
        if self.command:
            self.command()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='#18181A')  
        self.controller = controller

        # Header
        header_frame = tk.Frame(self, bg='#18181A')
        header_frame.pack(side='top', fill='x')
        header_label = tk.Label(header_frame, text='Library Management System', bg='#18181A', fg='cornflower blue', font=('Arial', 24, 'bold'))
        header_label.pack(pady=20)

        # Main Content Area
        content_frame = tk.Frame(self, bg='#18181A')
        content_frame.pack(expand=True, fill='both', padx=50, pady=30)

        # Buttons
        btn_manage_stock = RoundedButton(content_frame, text='Manage Stock', command=lambda: controller.show_frame('StockPage'), width=250, height=60, corner_radius=25)
        btn_manage_stock.pack(pady=20)  # Increased padding for better spacing

        btn_browse_customers = RoundedButton(content_frame, text='Browse Customers', command=lambda: controller.show_frame('CustomersPage'), width=250, height=60, corner_radius=25)
        btn_browse_customers.pack(pady=20)  # Increased padding for better spacing

        btn_handle_transactions = RoundedButton(content_frame, text='Handle Transactions', command=lambda: controller.show_frame('TransactionsPage'), width=250, height=60, corner_radius=25)
        btn_handle_transactions.pack(pady=20)  # Increased padding for better spacing

        # Footer
        footer_frame = tk.Frame(self, bg='#18181A')
        footer_frame.pack(side='bottom', fill='x')
        footer_label = tk.Label(footer_frame, text='© 2024 Library Management System', bg='#18181A', fg='white', font=('Arial', 12))
        footer_label.pack(pady=10)



class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Library Management Home')
        self.geometry('800x600')  # Set a default size for the application window
        self.configure(bg='black')  # Set the main application window background to black
        self.frames = {}

        container = tk.Frame(self, bg='black')  # Ensure the container also follows the dark theme
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

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
