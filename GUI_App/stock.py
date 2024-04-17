import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import db

connection = db.Connection()

class StockPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Setup the notebook widget
        notebook = ttk.Notebook(self)
        notebook.grid(row=0, column=0, sticky="nsew")

        # Stock display frame
        self.stock_frame = tk.Frame(notebook)
        notebook.add(self.stock_frame, text='Stock View')

        # Setup the stock view
        self.setup_stock_view()

        # Buttons for operations
        btn_frame = tk.Frame(self)
        btn_frame.grid(row=1, column=0, pady=10)
        tk.Button(btn_frame, text="Add Item", command=self.add_item).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Edit Item", command=self.edit_item).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Remove Item", command=self.remove_item).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Search Items", command=self.search_items).pack(side=tk.LEFT, padx=5)
        #Add home button
        self.add_home_button()

    def setup_stock_view(self):
        self.tree = ttk.Treeview(self.stock_frame, columns=("ID", "Type", "Title", "ISBN", "Author/Volume", "Year/Month", "PublisherID"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Title", text="Title")
        self.tree.heading("ISBN", text="ISBN")
        self.tree.heading("Author/Volume", text="Author/Volume")
        self.tree.heading("Year/Month", text="Year/Month")
        self.tree.heading("PublisherID", text="PublisherID")
        self.tree.grid(row=0, column=0, sticky="nsew")

        # Load initial stock data
        self.load_stock_data()

    def load_stock_data(self):
        # Clear existing data
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Fetch and display data from Books
        with connection.cursor() as cursor:
            cursor.execute("SELECT BookID, 'Book', Title, ISBN, MainAuthor, YearPublished, PublisherID FROM Books")
            books = cursor.fetchall()
            for book in books:
                self.tree.insert('', 'end', values=book)

            # Fetch and display data from Serials
            cursor.execute("SELECT SerialID, 'Serial', Title, ISBN, Volume, MonthYearPublished, PublisherID FROM Serials")
            serials = cursor.fetchall()
            for serial in serials:
                self.tree.insert('', 'end', values=serial)

            # Fetch and display data from DVDs
            cursor.execute("SELECT DVDID, 'DVD', Title, ISBN, MainAuthor, YearPublished, PublisherID FROM DVDs")
            dvds = cursor.fetchall()
            for dvd in dvds:
                self.tree.insert('', 'end', values=dvd)

    def load_items(self):
        # Load books, serials, and DVDs from the database
        # You would replace this with actual database queries to fetch the items
        pass

    def add_item(self):
        item_type = simpledialog.askstring("Add Item", "Enter item type (book, serial, dvd):")
        if item_type not in ['book', 'serial', 'dvd']:
            messagebox.showerror("Error", "Invalid item type")
            return

        title = simpledialog.askstring("Add Item", "Enter title:")
        isbn = simpledialog.askstring("Add Item", "Enter ISBN:")
        publisher_id = simpledialog.askinteger("Add Item", "Enter Publisher ID:")

        if item_type == 'book':
            author = simpledialog.askstring("Add Book", "Enter author:")
            year_published = simpledialog.askstring("Add Book", "Enter year published (YYYY-MM-DD):")
            query = "INSERT INTO Books (Title, ISBN, MainAuthor, YearPublished, PublisherID) VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5)"
            data = (title, isbn, author, year_published, publisher_id)
        elif item_type == 'serial':
            volume = simpledialog.askinteger("Add Serial", "Enter volume:")
            month_year_published = simpledialog.askstring("Add Serial", "Enter month and year published (YYYY-MM-DD):")
            query = "INSERT INTO Serials (Title, ISBN, Volume, MonthYearPublished, PublisherID) VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5)"
            data = (title, isbn, volume, month_year_published, publisher_id)
        elif item_type == 'dvd':
            author = simpledialog.askstring("Add DVD", "Enter main author:")
            year_published = simpledialog.askstring("Add DVD", "Enter year published (YYYY-MM-DD):")
            query = "INSERT INTO DVDs (Title, ISBN, MainAuthor, YearPublished, PublisherID) VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5)"
            data = (title, isbn, author, year_published, publisher_id)

        # Print debug information
        print("Executing query:", query)
        print("Data:", data)

        # Execute the query
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, data)
                connection.commit()
            messagebox.showinfo("Success", "Item added successfully")
            self.load_stock_data()
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to add item: {str(e)}")
            print(e)

    def edit_item(self):
        cur_item = self.tree.focus()
        item_values = self.tree.item(cur_item)['values']
        if not item_values:
            messagebox.showerror("Error", "No item selected")
            return

        # Extract values from the selected row
        item_id, item_type, title, isbn, author_volume, year_month, publisher_id = item_values

        # Open dialogues to edit information
        new_title = simpledialog.askstring("Edit Item", "Enter new title:", initialvalue=title)
        new_isbn = simpledialog.askstring("Edit Item", "Enter new ISBN:", initialvalue=isbn)

        # Prepare data based on item type
        if item_type.lower() == 'book':
            new_author = simpledialog.askstring("Edit Item", "Enter new author:", initialvalue=author_volume)
            new_year = simpledialog.askstring("Edit Item", "Enter new year (YYYY-MM-DD):", initialvalue=year_month)
            update_query = """
                UPDATE Books SET Title = :1, ISBN = :2, MainAuthor = :3, YearPublished = TO_DATE(:4, 'YYYY-MM-DD'), PublisherID = :5 
                WHERE BookID = :6
            """
            update_data = (new_title, new_isbn, new_author, new_year, publisher_id, item_id)

        elif item_type.lower() == 'serial':
            new_volume = simpledialog.askinteger("Edit Item", "Enter new volume:", initialvalue=author_volume)
            new_month_year = simpledialog.askstring("Edit Item", "Enter new month and year (YYYY-MM):", initialvalue=year_month)
            update_query = """
                UPDATE Serials SET Title = :1, ISBN = :2, Volume = :3, MonthYearPublished = TO_DATE(:4, 'YYYY-MM'), PublisherID = :5 
                WHERE SerialID = :6
            """
            update_data = (new_title, new_isbn, new_volume, new_month_year, publisher_id, item_id)

        elif item_type.lower() == 'dvd':
            new_author = simpledialog.askstring("Edit Item", "Enter new main author:", initialvalue=author_volume)
            new_year = simpledialog.askstring("Edit Item", "Enter new year (YYYY-MM-DD):", initialvalue=year_month)
            update_query = """
                UPDATE DVDs SET Title = :1, ISBN = :2, MainAuthor = :3, YearPublished = TO_DATE(:4, 'YYYY-MM-DD'), PublisherID = :5 
                WHERE DVDID = :6
            """
            update_data = (new_title, new_isbn, new_author, new_year, publisher_id, item_id)

        # Execute update query
        try:
            with connection.cursor() as cursor:
                cursor.execute(update_query, update_data)
                connection.commit()
            messagebox.showinfo("Success", "Item updated successfully")
            self.load_stock_data()
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to update item: {str(e)}")
            print(e)

    def remove_item(self):
        cur_item = self.tree.focus()
        item_values = self.tree.item(cur_item)['values']
        if not item_values:
            messagebox.showerror("Error", "No item selected")
            return

        item_id, item_type = item_values[0], item_values[1].lower()
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this item?")
        if confirm:
            delete_query = f"DELETE FROM {item_type.capitalize()}s WHERE {item_type.capitalize()}ID = :1"
            with connection.cursor() as cursor:
                cursor.execute(delete_query, [item_id])
                connection.commit()
            self.load_stock_data()
            messagebox.showinfo("Success", "Item deleted successfully")

    def search_items(self):
        # Prompt the user for a search term
        search_term = simpledialog.askstring("Search Items", "Enter search keyword:")
        # Define the search queries for Books, Serials, and DVDs, adjusted to handle empty search
        book_query = """
        SELECT BookID, 'Book' AS Type, Title, ISBN, MainAuthor, 
            TO_CHAR(YearPublished, 'YYYY-MM-DD') AS YearPublished, PublisherID
        FROM Books
        WHERE UPPER(Title) LIKE UPPER(:search) OR UPPER(ISBN) LIKE UPPER(:search) OR UPPER(MainAuthor) LIKE UPPER(:search)
        """

        serial_query = """
        SELECT SerialID, 'Serial' AS Type, Title, ISBN, Volume, 
            TO_CHAR(MonthYearPublished, 'YYYY-MM') AS MonthYearPublished, PublisherID
        FROM Serials
        WHERE UPPER(Title) LIKE UPPER(:search) OR UPPER(ISBN) LIKE UPPER(:search) OR UPPER(Volume) LIKE UPPER(:search)
        """

        dvd_query = """
        SELECT DVDID, 'DVD' AS Type, Title, ISBN, MainAuthor, 
            TO_CHAR(YearPublished, 'YYYY-MM-DD') AS YearPublished, PublisherID
        FROM DVDs
        WHERE UPPER(Title) LIKE UPPER(:search) OR UPPER(ISBN) LIKE UPPER(:search) OR UPPER(MainAuthor) LIKE UPPER(:search)
        """

        # Adjust search term to always have a value
        search_term = '%' + (search_term if search_term is not None else '') + '%'

        # Execute each query and aggregate results
        results = []
        try:
            with connection.cursor() as cursor:
                # Search in Books
                cursor.execute(book_query, {'search': search_term})
                results.extend(cursor.fetchall())

                # Search in Serials
                cursor.execute(serial_query, {'search': search_term})
                results.extend(cursor.fetchall())

                # Search in DVDs
                cursor.execute(dvd_query, {'search': search_term})
                results.extend(cursor.fetchall())

        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to search items: {str(e)}")
            return

        # Clear existing data and repopulate the Treeview
        self.tree.delete(*self.tree.get_children())
        for result in results:
            self.tree.insert('', 'end', values=result)

        if not results:
            messagebox.showinfo("Search", "No items found matching your search criteria.")
        else:
            messagebox.showinfo("Search", f"Found {len(results)} items matching your search criteria.")

    def add_home_button(self):
        # Create a Home button at the bottom of the frame
        home_button = tk.Button(self, text="Home", command=self.go_home)
        home_button.grid(row=2, column=0, pady=10, padx=10, sticky="ew")
        home_button.config(font=("Arial", 12), bg="#4CAF50", fg="white", bd=0, padx=20, pady=10)
        home_button.bind("<Enter>", lambda e: home_button.config(bg="#45a049"))
        home_button.bind("<Leave>", lambda e: home_button.config(bg="#4CAF50"))

    def go_home(self):
        # Call the controller's method to show the home page or main frame
        self.controller.show_frame("HomePage")