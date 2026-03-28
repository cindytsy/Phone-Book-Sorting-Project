# Phone Book Sorting
## Overview
This project implements a simple phone book system using Python. It allows users to store, manage, and sort contact entries efficiently.

---

## Data Structure
The phone book is implemented using a **list of dictionaries**.

Each entry contains:
- `name` (string)
- `phone` (string)
- `email` (optional)
- `address` (optional)

---

## Features

### Add Entry
Adds a new contact to the phone book.

### Update Entry
Updates an existing contact using their name.

### Delete Entry
Removes a contact by name.

### Sorting
Entries can be sorted by:
- Name
- Phone number
- Email
- Address

Sorting uses Python’s built-in **Timsort algorithm**, which runs in:
- Best case: O(n)
- Average/Worst case: O(n log n)

---

## How to Run

1. Make sure you have Python installed (Python 3+)
2. Run the script:

```bash
python phone_book.py
