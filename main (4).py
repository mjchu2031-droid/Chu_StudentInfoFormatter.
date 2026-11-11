# ==========================================
# VERSION 1: Initial Input Gathering
# ==========================================
print("--- Student Information Input ---")
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
section = input("Enter Section: ")
subject = input("Enter Favorite Subject: ")

# Combining names for full name processing
# .strip() is used to remove accidental leading/trailing spaces from inputs
full_name_raw = f"{first_name.strip()} {last_name.strip()}"