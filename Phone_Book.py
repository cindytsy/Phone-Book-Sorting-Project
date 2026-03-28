"""
Phone Book App

This module implements a phone book using a list of dictionaries.
Each entry contains:
- name (string)
- phone (string)
- email (optional string)
- address (optional string)

Features:
- Add entry
- Update entry
- Delete entry
- Sort entries by different fields
"""

class PhoneBook:
    def __init__(self):
        """Initialize an empty phone book."""
        self.entries = []

    def add_entry(self, name, phone, email=None, address=None):
        """Add a new entry to the phone book."""
        entry = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        self.entries.append(entry)

    def update_entry(self, name, **kwargs):
        """
        Update an existing entry by name.
        kwargs can include phone, email, address.
        """
        for entry in self.entries:
            if entry["name"].lower() == name.lower():
                for key, value in kwargs.items():
                    if key in entry:
                        entry[key] = value
                return True
        return False

    def delete_entry(self, name):
        """Delete an entry by name."""
        for i, entry in enumerate(self.entries):
            if entry["name"].lower() == name.lower():
                del self.entries[i]
                return True
        return False

    def sort_entries(self, by="name"):
        """
        Sort entries by a given field.
        Supported fields: name, phone, email, address
        Uses Python's built-in Timsort (O(n log n)).
        """
        if by not in ["name", "phone", "email", "address"]:
            raise ValueError("Invalid sorting field")

        self.entries.sort(key=lambda x: (x[by] or "").lower())

    def display_entries(self):
        """Print all entries in a readable format."""
        for entry in self.entries:
            print(entry)


# Example usage
if __name__ == "__main__":
    pb = PhoneBook()

    pb.add_entry("Alice", "123456789", "alice@email.com")
    pb.add_entry("Bob", "987654321")
    pb.add_entry("Charlie", "555555555", address="Vancouver")

    print("\n--- Original ---")
    pb.display_entries()

    pb.sort_entries(by="name")
    print("\n--- Sorted by Name ---")
    pb.display_entries()

    pb.sort_entries(by="phone")
    print("\n--- Sorted by Phone ---")
    pb.display_entries()

    pb.update_entry("Alice", phone="111111111")
    pb.delete_entry("Bob")

    print("\n--- After Update/Delete ---")
    pb.display_entries()