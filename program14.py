import pickle
import shelve
import os

class UserSession:
    """
    A complex class instance representing a user's active session to demonstrate object persistence.
    """
    def __init__(self, username: str, role: str, settings: dict):
        self.username = username
        self.role = role
        self.settings = settings
        self.is_active = True

    def __str__(self):
        return f"User: {self.username} | Role: {self.role} | Settings: {self.settings} | Active: {self.is_active}"


def save_with_pickle(obj: object, filepath: str) -> None:
    """
    Serializes a Python object to a binary file using pickle.
    Input:
        obj (object): The Python object to serialize.
        filepath (str): The destination file path.
    Output:+-
        None (Writes binary stream safely to disk)
    """
    with open(filepath, 'wb') as file:
        pickle.dump(obj, file)
    print(f"[*] Object successfully pickled to '{filepath}'")


def load_with_pickle(filepath: str) -> object:
    """
    Deserializes a Python object from a binary file using pickle.
    Input:
        filepath (str): The source file path to read from.
    Output:
        object: The restored Python object.
    """
    with open(filepath, 'rb') as file:
        obj = pickle.load(file)
    print(f"[*] Object successfully loaded from '{filepath}'")
    return obj


def save_with_shelve(db_path: str, key: str, obj: object) -> None:
    """
    Persists a Python object to disk using the shelve dictionary-like database.
    Input:
        db_path (str): The path to the shelve database.
        key (str): The string key to store the object under.
        obj (object): The Python object to store.
    Output:
        None (Writes safely to disk)
    """
    with shelve.open(db_path) as db:
        db[key] = obj
    print(f"[*] Object stored in shelve DB '{db_path}' under key '{key}'")


def load_with_shelve(db_path: str, key: str) -> object:
    """
    Restores a Python object from a shelve database using its key.
    Input:
        db_path (str): The path to the shelve database.
        key (str): The string key associated with the stored object.
    Output:
        object: The restored Python object, or None if not found.
    """
    with shelve.open(db_path) as db:
        obj = db.get(key)
    print(f"[*] Object retrieved from shelve DB '{db_path}' with key '{key}'")
    return obj


if __name__ == "__main__":
    print("--- Object Persistence Engine via Serialization ---\n")
    
    session1 = UserSession("Alice", "Admin", {"theme": "dark", "notifications": True})
    session2 = UserSession("Bob", "Guest", {"theme": "light", "notifications": False})
    
    pickle_file = "user_session.pkl"
    shelve_db = "app_database"
    
    print("1. Testing Pickle Serialization:")
    save_with_pickle(session1, pickle_file)
    
    restored_session1 = load_with_pickle(pickle_file)
    print(f"Restored Object state: {restored_session1}\n")
    print("2. Testing Shelve Database:")
    save_with_shelve(shelve_db, "session_bob", session2)
    
    restored_session2 = load_with_shelve(shelve_db, "session_bob")
    print(f"Restored Object state: {restored_session2}\n")
    
    if os.path.exists(pickle_file):
        os.remove(pickle_file)
    
    for ext in ['', '.db', '.bak', '.dir', '.dat']:
        if os.path.exists(shelve_db + ext):
            os.remove(shelve_db + ext)