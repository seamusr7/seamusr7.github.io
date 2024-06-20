import customtkinter as ctk
from tkinter import messagebox
from bson.objectid import ObjectId
from animal_shelter import AnimalShelter

# Initialize the AnimalShelter instance
shelter = AnimalShelter()

# Enable dark mode for the application
ctk.set_appearance_mode("dark")

# Function to format the search results for display
def format_result(result):
    """
    Formats a MongoDB document for display in the result textbox.
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
        "---------------------------------------------\n"
    )
    return formatted_result

# Login screen class
class LoginScreen(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("500x400")

        # Title label
        self.label = ctk.CTkLabel(self, text="Login to Animal Shelter Management")
        self.label.pack(pady=20)

        # Username entry
        self.user_label = ctk.CTkLabel(self, text="Username:")
        self.user_label.pack(pady=5)
        self.user_entry = ctk.CTkEntry(self)
        self.user_entry.pack(pady=5)
        self.user_entry.bind("<Return>", lambda event: self.login())  # Bind Enter key to login

        # Password entry
        self.pass_label = ctk.CTkLabel(self, text="Password:")
        self.pass_label.pack(pady=5)
        self.pass_entry = ctk.CTkEntry(self, show="*")
        self.pass_entry.pack(pady=5)
        self.pass_entry.bind("<Return>", lambda event: self.login())  # Bind Enter key to login

        # Login and Register buttons
        self.login_button = ctk.CTkButton(self, text="Login", command=self.login)
        self.login_button.pack(pady=10)
        self.register_button = ctk.CTkButton(self, text="Register", command=self.show_register)
        self.register_button.pack(pady=10)

    def login(self, username=None, password=None):
        """
        Handle the login functionality.
        """
        if username is None:
            username = self.user_entry.get()
        if password is None:
            password = self.pass_entry.get()
        if shelter.login_user(username, password):
            self.destroy()
            app = MainApp()
            app.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    def show_register(self):
        """
        Show the registration screen.
        """
        self.destroy()
        register_screen = RegisterScreen()
        register_screen.mainloop()

# Register screen class
class RegisterScreen(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Register")
        self.geometry("500x400")

        # Title label
        self.label = ctk.CTkLabel(self, text="Register New User")
        self.label.pack(pady=20)

        # Username entry
        self.user_label = ctk.CTkLabel(self, text="Username:")
        self.user_label.pack(pady=5)
        self.user_entry = ctk.CTkEntry(self)
        self.user_entry.pack(pady=5)
        self.user_entry.bind("<Return>", lambda event: self.register())  # Bind Enter key to register

        # Password entry
        self.pass_label = ctk.CTkLabel(self, text="Password:")
        self.pass_label.pack(pady=5)
        self.pass_entry = ctk.CTkEntry(self, show="*")
        self.pass_entry.pack(pady=5)
        self.pass_entry.bind("<Return>", lambda event: self.register())  # Bind Enter key to register

        # Register and Back to Login buttons
        self.register_button = ctk.CTkButton(self, text="Register", command=self.register)
        self.register_button.pack(pady=20)
        self.back_button = ctk.CTkButton(self, text="Back to Login", command=self.show_login)
        self.back_button.pack(pady=10)

    def register(self):
        """
        Handle the registration functionality.
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
        Show the login screen.
        """
        self.destroy()
        login_screen = LoginScreen()
        if autologin:
            login_screen.login(username=username, password=password)
        else:
            login_screen.mainloop()

# Add Animal screen class
class AddAnimalScreen(ctk.CTk):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.title("Add Animal")
        self.geometry("400x800")

        # Title label
        self.label = ctk.CTkLabel(self, text="Add New Animal")
        self.label.pack(pady=20)

        # Animal ID entry
        self.animal_id_label = ctk.CTkLabel(self, text="Animal ID:")
        self.animal_id_label.pack(pady=5)
        self.animal_id_entry = ctk.CTkEntry(self)
        self.animal_id_entry.pack(pady=5)

        # Animal Type entry
        self.animal_type_label = ctk.CTkLabel(self, text="Animal Type:")
        self.animal_type_label.pack(pady=5)
        self.animal_type_entry = ctk.CTkEntry(self)
        self.animal_type_entry.pack(pady=5)

        # Breed entry
        self.breed_label = ctk.CTkLabel(self, text="Breed:")
        self.breed_label.pack(pady=5)
        self.breed_entry = ctk.CTkEntry(self)
        self.breed_entry.pack(pady=5)

        # Color entry
        self.color_label = ctk.CTkLabel(self, text="Color:")
        self.color_label.pack(pady=5)
        self.color_entry = ctk.CTkEntry(self)
        self.color_entry.pack(pady=5)

        # Age entry
        self.age_label = ctk.CTkLabel(self, text="Age:")
        self.age_label.pack(pady=5)
        self.age_entry = ctk.CTkEntry(self)
        self.age_entry.pack(pady=5)

        # Outcome Type entry
        self.outcome_type_label = ctk.CTkLabel(self, text="Outcome Type:")
        self.outcome_type_label.pack(pady=5)
        self.outcome_type_entry = ctk.CTkEntry(self)
        self.outcome_type_entry.pack(pady=5)

        # Sex entry
        self.sex_label = ctk.CTkLabel(self, text="Sex:")
        self.sex_label.pack(pady=5)
        self.sex_entry = ctk.CTkEntry(self)
        self.sex_entry.pack(pady=5)

        # Date of Birth entry
        self.date_of_birth_label = ctk.CTkLabel(self, text="Date of Birth:")
        self.date_of_birth_label.pack(pady=5)
        self.date_of_birth_entry = ctk.CTkEntry(self)
        self.date_of_birth_entry.pack(pady=5)

        # Add button
        self.add_button = ctk.CTkButton(self, text="Add Animal", command=self.add_animal)
        self.add_button.pack(pady=20)
        self.add_button.bind("<Return>", lambda event: self.add_animal())  # Bind Enter key to add animal

    def add_animal(self):
        """
        Handle the add animal functionality.
        """
        animal = {
            'animal_id': self.animal_id_entry.get(),
            'animal_type': self.animal_type_entry.get(),
            'breed': self.breed_entry.get(),
            'color': self.color_entry.get(),
            'age_upon_outcome': self.age_entry.get(),
            'outcome_type': self.outcome_type_entry.get(),
            'sex_upon_outcome': self.sex_entry.get(),
            'date_of_birth': self.date_of_birth_entry.get()
        }
        if all(animal.values()):
            shelter.create(animal)
            messagebox.showinfo("Success", "Animal added successfully")
            self.destroy()
            self.parent.update_results()
        else:
            messagebox.showerror("Error", "All fields must be filled")

# Update Animal screen class
class UpdateAnimalScreen(ctk.CTk):
    def __init__(self, parent, animal_id):
        super().__init__()
        self.parent = parent
        self.animal_id = animal_id
        self.title("Update Animal")
        self.geometry("400x800")

        # Title label
        self.label = ctk.CTkLabel(self, text="Update Animal")
        self.label.pack(pady=20)

        # Display Animal ID
        self.animal_id_label = ctk.CTkLabel(self, text=f"Animal ID: {animal_id}")
        self.animal_id_label.pack(pady=5)

        # Animal Type entry
        self.animal_type_label = ctk.CTkLabel(self, text="Animal Type:")
        self.animal_type_label.pack(pady=5)
        self.animal_type_entry = ctk.CTkEntry(self)
        self.animal_type_entry.pack(pady=5)

        # Breed entry
        self.breed_label = ctk.CTkLabel(self, text="Breed:")
        self.breed_label.pack(pady=5)
        self.breed_entry = ctk.CTkEntry(self)
        self.breed_entry.pack(pady=5)

        # Color entry
        self.color_label = ctk.CTkLabel(self, text="Color:")
        self.color_label.pack(pady=5)
        self.color_entry = ctk.CTkEntry(self)
        self.color_entry.pack(pady=5)

        # Age entry
        self.age_label = ctk.CTkLabel(self, text="Age:")
        self.age_label.pack(pady=5)
        self.age_entry = ctk.CTkEntry(self)
        self.age_entry.pack(pady=5)

        # Outcome Type entry
        self.outcome_type_label = ctk.CTkLabel(self, text="Outcome Type:")
        self.outcome_type_label.pack(pady=5)
        self.outcome_type_entry = ctk.CTkEntry(self)
        self.outcome_type_entry.pack(pady=5)

        # Sex entry
        self.sex_label = ctk.CTkLabel(self, text="Sex:")
        self.sex_label.pack(pady=5)
        self.sex_entry = ctk.CTkEntry(self)
        self.sex_entry.pack(pady=5)

        # Date of Birth entry
        self.date_of_birth_label = ctk.CTkLabel(self, text="Date of Birth:")
        self.date_of_birth_label.pack(pady=5)
        self.date_of_birth_entry = ctk.CTkEntry(self)
        self.date_of_birth_entry.pack(pady=5)

        # Update button
        self.update_button = ctk.CTkButton(self, text="Update Animal", command=self.update_animal)
        self.update_button.pack(pady=20)
        self.update_button.bind("<Return>", lambda event: self.update_animal())  # Bind Enter key to update animal

    def update_animal(self):
        """
        Handle the update animal functionality.
        """
        update_data = {
            'animal_type': self.animal_type_entry.get(),
            'breed': self.breed_entry.get(),
            'color': self.color_entry.get(),
            'age_upon_outcome': self.age_entry.get(),
            'outcome_type': self.outcome_type_entry.get(),
            'sex_upon_outcome': self.sex_entry.get(),
            'date_of_birth': self.date_of_birth_entry.get()
        }
        if any(update_data.values()):
            shelter.update({'animal_id': self.animal_id}, {k: v for k, v in update_data.items() if v})
            messagebox.showinfo("Success", "Animal updated successfully")
            self.destroy()
            self.parent.update_results()
        else:
            messagebox.showerror("Error", "At least one field must be filled")

# Main application class
class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Animal Shelter Management System")
        self.geometry("800x800")

        # Title label
        self.label = ctk.CTkLabel(self, text="Animal Shelter Management System")
        self.label.pack(pady=20)

        # Frame for search filters
        self.filters_frame = ctk.CTkFrame(self)
        self.filters_frame.pack(pady=10, padx=10, fill="x")

        # Animal Type filter
        self.type_label = ctk.CTkLabel(self.filters_frame, text="Animal Type:")
        self.type_label.grid(row=0, column=0, padx=10, pady=5)
        self.type_entry = ctk.CTkEntry(self.filters_frame)
        self.type_entry.grid(row=0, column=1, padx=10, pady=5)

        # Breed filter
        self.breed_label = ctk.CTkLabel(self.filters_frame, text="Breed:")
        self.breed_label.grid(row=0, column=2, padx=10, pady=5)
        self.breed_entry = ctk.CTkEntry(self.filters_frame)
        self.breed_entry.grid(row=0, column=3, padx=10, pady=5)

        # Age filter
        self.age_label = ctk.CTkLabel(self.filters_frame, text="Age:")
        self.age_label.grid(row=1, column=0, padx=10, pady=5)
        self.age_entry = ctk.CTkEntry(self.filters_frame)
        self.age_entry.grid(row=1, column=1, padx=10, pady=5)

        # Color filter
        self.color_label = ctk.CTkLabel(self.filters_frame, text="Color:")
        self.color_label.grid(row=1, column=2, padx=10, pady=5)
        self.color_entry = ctk.CTkEntry(self.filters_frame)
        self.color_entry.grid(row=1, column=3, padx=10, pady=5)

        # Search button
        self.search_button = ctk.CTkButton(self.filters_frame, text="Search", command=self.search)
        self.search_button.grid(row=2, column=0, columnspan=4, pady=10)
        self.type_entry.bind("<Return>", lambda event: self.search())
        self.breed_entry.bind("<Return>", lambda event: self.search())
        self.age_entry.bind("<Return>", lambda event: self.search())
        self.color_entry.bind("<Return>", lambda event: self.search())
        self.search_button.bind("<Return>", lambda event: self.search())

        # Sort options
        self.sort_label = ctk.CTkLabel(self.filters_frame, text="Sort By:")
        self.sort_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.sort_var = ctk.StringVar()
        self.sort_options = ["", "Animal ID", "Animal Type", "Breed", "Age"]
        self.sort_menu = ctk.CTkOptionMenu(self.filters_frame, variable=self.sort_var, values=self.sort_options)
        self.sort_menu.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        self.sort_button = ctk.CTkButton(self.filters_frame, text="Sort", command=self.sort_records)
        self.sort_button.grid(row=3, column=2, columnspan=2, padx=5, pady=5, sticky="ew")
        self.sort_button.bind("<Return>", lambda event: self.sort_records())

        # Textbox for displaying results
        self.result_text = ctk.CTkTextbox(self, width=700, height=300)
        self.result_text.pack(pady=20)

        # Frame for CRUD operations
        self.crud_frame = ctk.CTkFrame(self)
        self.crud_frame.pack(pady=10, padx=10, fill="x")

        # Add Animal button
        self.add_button = ctk.CTkButton(self.crud_frame, text="Add Animal", command=self.show_add_animal)
        self.add_button.grid(row=0, column=0, columnspan=3, padx=10, pady=5, sticky="ew")
        self.add_button.bind("<Return>", lambda event: self.show_add_animal())

        # Update Animal section
        self.update_label = ctk.CTkLabel(self.crud_frame, text="Animal ID for Update:")
        self.update_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.update_id_entry = ctk.CTkEntry(self.crud_frame)
        self.update_id_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        self.update_button = ctk.CTkButton(self.crud_frame, text="Update Animal", command=self.show_update_animal)
        self.update_button.grid(row=1, column=2, padx=10, pady=5, sticky="ew")
        self.update_id_entry.bind("<Return>", lambda event: self.show_update_animal())
        self.update_button.bind("<Return>", lambda event: self.show_update_animal())

        # Delete Animal section
        self.delete_label = ctk.CTkLabel(self.crud_frame, text="Animal ID for Delete:")
        self.delete_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.delete_id_entry = ctk.CTkEntry(self.crud_frame)
        self.delete_id_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        self.delete_button = ctk.CTkButton(self.crud_frame, text="Delete Animal", command=self.delete_animal)
        self.delete_button.grid(row=2, column=2, padx=10, pady=5, sticky="ew")
        self.delete_id_entry.bind("<Return>", lambda event: self.delete_animal())
        self.delete_button.bind("<Return>", lambda event: self.delete_animal())

        # Logout button
        self.logout_button = ctk.CTkButton(self, text="Logout", command=self.logout)
        self.logout_button.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

    def search(self):
        """
        Handle the search functionality.
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

    def sort_records(self):
        """
        Handle the sort functionality.
        """
        sort_by = self.sort_var.get()
        if sort_by == "":
            return

        key_mapping = {
            "Animal ID": lambda x: x.get('animal_id', ''),
            "Animal Type": lambda x: x.get('animal_type', ''),
            "Breed": lambda x: x.get('breed', ''),
            "Age": lambda x: x.get('age_upon_outcome', '')
        }
        animals = shelter.read({})
        sorted_animals = shelter.merge_sort(animals, key=key_mapping[sort_by])
        self.result_text.delete("1.0", ctk.END)
        for animal in sorted_animals:
            self.result_text.insert(ctk.END, format_result(animal))

    def show_add_animal(self):
        """
        Show the Add Animal screen.
        """
        add_animal_screen = AddAnimalScreen(self)
        add_animal_screen.mainloop()

    def show_update_animal(self):
        """
        Show the Update Animal screen.
        """
        animal_id = self.update_id_entry.get()
        if animal_id:
            update_animal_screen = UpdateAnimalScreen(self, animal_id)
            update_animal_screen.mainloop()
        else:
            messagebox.showerror("Error", "Animal ID cannot be empty")

    def delete_animal(self):
        """
        Handle the delete animal functionality.
        """
        animal_id = self.delete_id_entry.get()
        if animal_id:
            if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this animal?"):
                shelter.delete({'animal_id': animal_id})
                messagebox.showinfo("Success", "Animal deleted successfully")
        else:
            messagebox.showerror("Error", "Animal ID cannot be empty")

    def logout(self):
        """
        Handle the logout functionality.
        """
        self.destroy()
        login_screen = LoginScreen()
        login_screen.mainloop()

    def update_results(self):
        """
        Update the search results.
        """
        self.search()

# Main execution
if __name__ == "__main__":
    login_screen = LoginScreen()
    login_screen.mainloop()
