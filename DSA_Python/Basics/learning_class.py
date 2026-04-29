
class Users:
    # This is a class-level variable; all instances share this dictionary
    user_database = {}

    def __init__(self, username, password):
        self.name = username
        self.password = password

    def display(self) -> None:
        """Print current object data."""
        # Fixed: Changed self.username to self.name to match __init__
        print(f"Username: {self.name}\nPassword: {self.password}")

    def save(self) -> None:
        """
        Save this user into the shared dictionary database.
        """
        # We map the username as the Key and password as the Value
        Users.user_database[self.name] = self.password
        print(f"User '{self.name}' has been saved to the database.")

    @classmethod
    def show_database(cls):
        """Display all users currently in the dictionary."""
        print("\n--- Current User Database ---")
        for username, password in cls.user_database.items():
            print(f"User: {username} | Password: {password}")
        print("-----------------------------\n")

# --- Execution ---

# 1. Create users
user1 = Users("Anuj", "as123")
user2 = Users("Anuj Nagar", "paswword123")

# 2. Save users to the database
user1.save()
user2.save()

# 3. Display individual user data
print("\nIndividual Display:")
user1.display()

# 4. Enquire/Show the entire database
Users.show_database()


# import sqlite3


# class User:
#     """
#     Beginner-friendly User class.

#     Each object stores one user's data and can save itself into a database.
#     """

#     def __init__(self, username: str, password: str):
#         self.username = username
# class Users:
#     def __init__(self, username, password):
#         self.name = username
#         self.password = password

#     def display(self) -> None:
#         """Print current object data."""
#         print(f"Username: {self.username}\nPassword: {self.password}")
#         self.user_database = {
#             "Name": username,
#             "Password": password
#         }

#     def save(self, db_name: str = "users.db") -> None:
#         """
#         Save this user into SQLite database.
#     def display(self):
#         print(f"Username: {self.name}\nPassword: {self.password}")

#         `db_name` is the database file name.
#         If table does not exist, it will be created automatically.
#         """
#         conn = sqlite3.connect(db_name)
#         cursor = conn.cursor()
#     def save(self):
#         self.user_database["Name"] = self.name
#         self.user_database["Password"] = self.password

#         cursor.execute(
#             """
#             CREATE TABLE IF NOT EXISTS users (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 username TEXT NOT NULL,
#                 password TEXT NOT NULL
#             )
#             """
#         )

#         cursor.execute(
#             "INSERT INTO users (username, password) VALUES (?, ?)",
#             (self.username, self.password),
#         )

#         conn.commit()
#         conn.close()


# if __name__ == "__main__":
#     user1 = User("Anuj", "as123")
#     user2 = User("Anuj Nagar", "password123")

#     user1.display()
#     user2.display()

#     user1.save()
#     user2.save()

#     print("Users saved to users.db successfully.")
# user1 = Users("Anuj", "as123")
# user2 = Users("Anuj Nagar", "paswword123")
# user1.display()
# 