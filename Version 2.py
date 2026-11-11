# --- VERSION 2: ADDED STRING FORMATTING ---

# Gathering Required Inputs
print("--- Enter Student Information ---")
first_name = input("First name: ")
last_name = input("Last name: ")
section = input("Section: ")
favorite_subject = input("Favorite subject: ")

# Data Cleaning & Manipulation
# .strip() removes any accidental leading/trailing spaces the user might have typed
cleaned_first = first_name.strip()
cleaned_last = last_name.strip()
full_name = f"{cleaned_first} {cleaned_last}"

# 1. Full name in proper title format
full_name_title = full_name.title()

# 2. Full name in uppercase letters
full_name_upper = full_name.upper()

# 3. Section in uppercase letters
section_upper = section.strip().upper()

# 4. Favorite subject in proper title format
subject_title = favorite_subject.strip().title()

# 5. Total character count of the full name (excluding spaces)
# .replace(" ", "") ensures spaces are not counted as letters
name_char_count = len(full_name.replace(" ", ""))

# Displaying Required Formatted Outputs
print("\n========================================")
print("     STANDARDIZED STUDENT REPORT        ")
print("========================================")
print(f"Full Name (Title Case): {full_name_title}")
print(f"Full Name (Uppercase):  {full_name_upper}")
print(f"Section (Uppercase):    {section_upper}")
print(f"Favorite Subject:       {subject_title}")
print(f"Total Character Count:  {name_char_count} (letters only)")
print("========================================")
