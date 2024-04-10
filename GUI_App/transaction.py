import tkinter as tk

class TransactionsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='#eeeeee')  # Set the background to light gray
        self.controller = controller
        
        # Header Label
        tk.Label(self, text="Transactions Page", font=("Arial", 18, 'bold'), bg='#eeeeee', fg='#1155cc').pack(pady=(20, 10))
        
        # Main Content Frame
        content_frame = tk.Frame(self, bg='#eeeeee')
        content_frame.pack(fill='both', expand=True, padx=50, pady=20)
        
        # Transaction Functionality Buttons
        btn_checkout_item = tk.Button(content_frame, text="Checkout Item", font=("Arial", 14), bg='#1155cc', fg='white', bd=0,
                                      padx=20, pady=10, command=self.checkout_item)
        btn_checkout_item.pack(pady=10)
        
        btn_return_item = tk.Button(content_frame, text="Return Item", font=("Arial", 14), bg='#1155cc', fg='white', bd=0,
                                    padx=20, pady=10, command=self.return_item)
        btn_return_item.pack(pady=10)
        
        btn_renew_item = tk.Button(content_frame, text="Renew Item", font=("Arial", 14), bg='#1155cc', fg='white', bd=0,
                                   padx=20, pady=10, command=self.renew_item)
        btn_renew_item.pack(pady=10)

        # Back to Home Button with Enhanced Styling
        back_button = tk.Button(self, text="← Back to Home", font=("Arial", 12), bg='#1155cc', fg='white', bd=0,
                                padx=10, pady=5, command=lambda: controller.show_frame("HomePage"))
        back_button.pack(side='bottom', pady=(10, 20))
        
        # Mouse Hover Effects for the Back Button
        back_button.bind("<Enter>", lambda e: back_button.config(bg="#0d3d82"))
        back_button.bind("<Leave>", lambda e: back_button.config(bg="#1155cc"))

    def checkout_item(self):
        print("Checkout item functionality goes here.")

    def return_item(self):
        print("Return item functionality goes here.")

    def renew_item(self):
        print("Renew item functionality goes here.")









'''''
import tkinter as tk

class TransactionsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='#eeeeee')  # Set the background to light gray
        self.controller = controller
        
        # Header Label
        tk.Label(self, text="Transactions Page", font=("Arial", 18, 'bold'), bg='#eeeeee', fg='#1155cc').pack(pady=(20, 10))
        
        # Main Content Frame
        content_frame = tk.Frame(self, bg='#eeeeee')
        content_frame.pack(fill='both', expand=True, padx=50, pady=20)
        
        # Transaction Functionality Buttons
        btn_checkout_item = tk.Button(content_frame, text="Checkout Item", font=("Arial", 14), bg='#1155cc', fg='white', bd=0,
                                      padx=20, pady=10, command=self.checkout_item)
        btn_checkout_item.pack(pady=10)
        
        btn_return_item = tk.Button(content_frame, text="Return Item", font=("Arial", 14), bg='#1155cc', fg='white', bd=0,
                                    padx=20, pady=10, command=self.return_item)
        btn_return_item.pack(pady=10)
        
        btn_renew_item = tk.Button(content_frame, text="Renew Item", font=("Arial", 14), bg='#1155cc', fg='white', bd=0,
                                   padx=20, pady=10, command=self.renew_item)
        btn_renew_item.pack(pady=10)

        # Back to Home Button with Enhanced Styling
        back_button = tk.Button(self, text="← Back to Home", font=("Arial", 12), bg='#1155cc', fg='white', bd=0,
                                padx=10, pady=5, command=lambda: controller.show_frame("HomePage"))
        back_button.pack(side='bottom', pady=(10, 20))
        
        # Mouse Hover Effects for the Back Button
        back_button.bind("<Enter>", lambda e: back_button.config(bg="#0d3d82"))
        back_button.bind("<Leave>", lambda e: back_button.config(bg="#1155cc"))

    def checkout_item(self):
        print("Checkout item functionality goes here.")

    def return_item(self):
        print("Return item functionality goes here.")

    def renew_item(self):
        print("Renew item functionality goes here.")



'''''
