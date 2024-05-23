import customtkinter as ctk
from tkinter import messagebox
from bson.objectid import ObjectId
from animal_shelter import AnimalShelter

# Initialize the AnimalShelter instance
shelter = AnimalShelter()

# Function to format the search results
def format_result(result):
    """
    This function takes a MongoDB document and returns a formatted string
    that presents the document's data in a readable format for the user.
    """
    formatted_result = (
        f"Animal ID: {result.get('animal_id', 'N/A')}\n"
        f"Animal Type: {result.get('animal_type', 'N/A')}\n"
        f"Breed: {result.get('breed', 'N/A')}\n"
        f"Color: {result.get('color', 'N/A')}\n"
        f"Age Upon Outcome: {result.get('age_upon_outcome', 'N/A')}\n"
        f"Outcome Type: {result.get('outcome_type', 'N/A')}\n"
        f"Sex: {result.get('sex_upon_outcome', 'N/A')}\n"
        f"Date of Birth: {result.get('date_of_birth', 'N/A')}\n"
        f"Location: ({result.get('location_lat', 'N/A')}, {result.get('location_long', 'N/A')})\n"
        "---------------------------------------------\n"
    )
    return formatted_result

# Login screen class
class LoginScreen(ctk.CTk):
    """
    This class represents the login screen of the application.
    It provides fields for the user to enter their username and password,
    and buttons to log in or register a new account.
    """
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("500x400")

        # Label for the login screen title
        self.label = ctk.CTkLabel(self, text="Login to Animal Shelter Management")
        self.label.pack(pady=20)

        # Username entry
        self.user_label = ctk.CTkLabel(self, text="Username:")
        self.user_label.pack(pady=5)
        self.user_entry = ctk.CTkEntry(self)
        self.user_entry.pack(pady=5)

        # Password entry
        self.pass_label = ctk.CTkLabel(self, text="Password:")
        self.pass_label.pack(pady=5)
        self.pass_entry = ctk.CTkEntry(self, show="*")
        self.pass_entry.pack(pady=5)

        # Login button
        self.login_button = ctk.CTkButton(self, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        # Register button
        self.register_button = ctk.CTkButton(self, text="Register", command=self.show_register)
        self.register_button.pack(pady=10)

    def login(self, username=None, password=None):
        """
        This method handles the login functionality.
        If the username and password parameters are provided, it uses them to log in,
        otherwise it retrieves the values from the entry fields.
        """
        if username is None:
            username = self.user_entry.get()
        if password is None:
            password = self.pass_entry.get()
        if shelter.login_user(username, password):
            self.destroy()  # Close the login screen
            app = MainApp()  # Open the main application
            app.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    def show_register(self):
        """
        This method closes the login screen and opens the registration screen.
        """
        self.destroy()
        register_screen = RegisterScreen()
        register_screen.mainloop()

# Register screen class
class RegisterScreen(ctk.CTk):
    """
    This class represents the registration screen of the application.
    It provides fields for the user to enter a new username and password,
    and buttons to register or go back to the login screen.
    """
    def __init__(self):
        super().__init__()
        self.title("Register")
        self.geometry("500x400")

        # Label for the registration screen title
        self.label = ctk.CTkLabel(self, text="Register New User")
        self.label.pack(pady=20)

        # Username entry
        self.user_label = ctk.CTkLabel(self, text="Username:")
        self.user_label.pack(pady=5)
        self.user_entry = ctk.CTkEntry(self)
        self.user_entry.pack(pady=5)

        # Password entry
        self.pass_label = ctk.CTkLabel(self, text="Password:")
        self.pass_label.pack(pady=5)
        self.pass_entry = ctk.CTkEntry(self, show="*")
        self.pass_entry.pack(pady=5)

        # Register button
        self.register_button = ctk.CTkButton(self, text="Register", command=self.register)
        self.register_button.pack(pady=20)

        # Back to login button
        self.back_button = ctk.CTkButton(self, text="Back to Login", command=self.show_login)
        self.back_button.pack(pady=10)

    def register(self):
        """
        This method handles the registration functionality.
        It retrieves the username and password from the entry fields,
        registers the user, and then logs them in automatically.
        """
        username = self.user_entry.get()
        password = self.pass_entry.get()
        if shelter.register_user(username, password):
            messagebox.showinfo("Registration Successful", "User registered successfully")
            self.show_login(autologin=True, username=username, password=password)
        else:
            messagebox.showerror("Registration Failed", "Failed to register user")

    def show_login(self, autologin=False, username=None, password=None):
        """
        This method closes the registration screen and opens the login screen.
        If autologin is True, it logs in the user automatically using the provided credentials.
        """
        self.destroy()
        login_screen = LoginScreen()
        if autologin:
            login_screen.login(username=username, password=password)
        else:
            login_screen.mainloop()

# Main application class
class MainApp(ctk.CTk):
    """
    This class represents the main application screen.
    It provides a user interface for searching animals and performing CRUD operations.
    """
    def __init__(self):
        super().__init__()
        self.title("Animal Shelter Management System")
        self.geometry("800x600")

        # Label for the main application title
        self.label = ctk.CTkLabel(self, text="Animal Shelter Management System")
        self.label.pack(pady=20)

        # Search filters
        self.filters_frame = ctk.CTkFrame(self)
        self.filters_frame.pack(pady=10, padx=10, fill="x")

        self.type_label = ctk.CTkLabel(self.filters_frame, text="Animal Type:")
        self.type_label.grid(row=0, column=0, padx=10, pady=5)
        self.type_entry = ctk.CTkEntry(self.filters_frame)
        self.type_entry.grid(row=0, column=1, padx=10, pady=5)

        self.breed_label = ctk.CTkLabel(self.filters_frame, text="Breed:")
        self.breed_label.grid(row=0, column=2, padx=10, pady=5)
        self.breed_entry = ctk.CTkEntry(self.filters_frame)
        self.breed_entry.grid(row=0, column=3, padx=10, pady=5)

        self.age_label = ctk.CTkLabel(self.filters_frame, text="Age:")
        self.age_label.grid(row=1, column=0, padx=10, pady=5)
        self.age_entry = ctk.CTkEntry(self.filters_frame)
        self.age_entry.grid(row=1, column=1, padx=10, pady=5)

        self.color_label = ctk.CTkLabel(self.filters_frame, text="Color:")
        self.color_label.grid(row=1, column=2, padx=10, pady=5)
        self.color_entry = ctk.CTkEntry(self.filters_frame)
        self.color_entry.grid(row=1, column=3, padx=10, pady=5)

        # Search button
        self.search_button = ctk.CTkButton(self, text="Search", command=self.search)
        self.search_button.pack(pady=20)

        # Textbox for displaying results
        self.result_text = ctk.CTkTextbox(self, width=700, height=300)
        self.result_text.pack(pady=20)

        # CRUD operations
        self.name_label = ctk.CTkLabel(self, text="Name:")
        self.name_label.pack(pady=5)
        self.name_entry = ctk.CTkEntry(self)
        self.name_entry.pack(pady=5)

        self.add_button = ctk.CTkButton(self, text="Add Animal", command=self.add_animal)
        self.add_button.pack(pady=20)

        self.update_label = ctk.CTkLabel(self, text="Update Animal (by ID):")
        self.update_label.pack(pady=5)
        self.id_entry = ctk.CTkEntry(self)
        self.id_entry.pack(pady=5)

        self.update_button = ctk.CTkButton(self, text="Update Animal", command=self.update_animal)
        self.update_button.pack(pady=20)

        self.delete_button = ctk.CTkButton(self, text="Delete Animal", command=self.delete_animal)
        self.delete_button.pack(pady=20)

    def search(self):
        """
        This method handles the search functionality.
        It retrieves the search criteria from the entry fields,
        constructs a query using regular expressions for partial and case-insensitive matches,
        and displays the results in a formatted way.
        """
        type_query = self.type_entry.get()
        breed_query = self.breed_entry.get()
        age_query = self.age_entry.get()
        color_query = self.color_entry.get()

        query = {}
        if type_query:
            query['animal_type'] = {'$regex': type_query, '$options': 'i'}
        if breed_query:
            query['breed'] = {'$regex': breed_query, '$options': 'i'}
        if age_query:
            try:
                # Convert age to the format in the database
                age_int = int(age_query)
                if age_int == 1:
                    query['age_upon_outcome'] = f"{age_int} year"
                else:
                    query['age_upon_outcome'] = f"{age_int} years"
            except ValueError:
                messagebox.showerror("Error", "Age must be a number")
                return
        if color_query:
            query['color'] = {'$regex': color_query, '$options': 'i'}

        results = shelter.read(query)
        self.result_text.delete("1.0", ctk.END)
        for result in results:
            self.result_text.insert(ctk.END, format_result(result))

    def add_animal(self):
        """
        This method handles adding a new animal to the database.
        It retrieves the name from the entry field and calls the create method from AnimalShelter.
        """
        name = self.name_entry.get()
        if name:
            shelter.create({'name': name})
            messagebox.showinfo("Success", "Animal added successfully")
        else:
            messagebox.showerror("Error", "Name cannot be empty")

    def update_animal(self):
        """
        This method handles updating an existing animal's information in the database.
        It retrieves the animal ID and new name from the entry fields and calls the update method from AnimalShelter.
        """
        animal_id = self.id_entry.get()
        name = self.name_entry.get()
        if animal_id and name:
            shelter.update({'_id': ObjectId(animal_id)}, {'name': name})
            messagebox.showinfo("Success", "Animal updated successfully")
        else:
            messagebox.showerror("Error", "ID and Name cannot be empty")

    def delete_animal(self):
        """
        This method handles deleting an animal from the database.
        It retrieves the animal ID from the entry field and calls the delete method from AnimalShelter.
        """
        animal_id = self.id_entry.get()
        if animal_id:
            shelter.delete({'_id': ObjectId(animal_id)})
            messagebox.showinfo("Success", "Animal deleted successfully")
        else:
            messagebox.showerror("Error", "ID cannot be empty")

# Main execution
if __name__ == "__main__":
    login_screen = LoginScreen()
    login_screen.mainloop()
