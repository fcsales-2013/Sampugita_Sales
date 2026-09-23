# More code!
import re
pattern = r"\d{4}-\d{4}"
while True:
    print("Format should be [4 digits]-[4 digits] (e.g., 2026-1234)")
    studentid = input("Enter your student id: ").strip()

    if re.fullmatch(pattern, studentid):
        print("Your student id is valid!")
        break
    else:
        print("That is invalid boiiiii...\n")
