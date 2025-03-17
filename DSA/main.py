# data = [
#     ["S.No", "Question", "Link", "Company"],
#     [1, "Equilibrium Point", "https://www.geeksforgeeks.org/problems/equilibrium-point-1587115620/1?page=1&category=Arrays&sortBy=submissions", 
#      "Amazon, Adobe, Google, Facebook, Microsoft, Uber"]
# ]

# # Define column widths dynamically based on content
# col_widths = [max(len(str(row[i])) for row in data) for i in range(len(data[0]))]

# # Function to create a horizontal boundary
# def create_boundary():
#     return "+".join(["-" * (w + 2) for w in col_widths])

# # Writing the table to a file
# with open("DSA/Arrays/Prefix_sum/Questions.txt", "w", encoding="utf-8") as file:
#     top_border = "+" + create_boundary() + "+"
#     file.write(top_border + "\n")

#     # Writing data
#     for i, row in enumerate(data):
#         file.write("| " + " | ".join(f"{str(item):<{col_widths[j]}}" for j, item in enumerate(row)) + " |\n")
#         if i == 0:  # Header separator
#             file.write("|" + create_boundary() + "|\n")
    
#     bottom_border = "+" + create_boundary() + "+"
#     file.write(bottom_border + "\n")

# print("Table written to table.txt successfully!")


import os


# File path where the table will be saved
file_path = "C:/DSA_sheet/DSA/Arrays/Simple_iterations/Questions.txt"



# New row to be added
new_row = [2, "Maximum number of zeroes", "https://www.geeksforgeeks.org/problems/maximum-number-of-zeroes4048/1", "Oracle"]

# Read the existing table
data = []

if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Extract existing rows, ignoring the first and last border lines
    for line in lines[1:-1]:  
        row = line.strip("| \n").split(" | ")
        if len(row) >= 4:  # Ensure row has enough columns
            data.append(row)

# If file is empty or has invalid content, initialize with header
if not data or len(data[0]) < 4:
    data = [["S.No", "Question", "Link", "Company"]]

# Append the new row (ensuring all elements are strings)
data.append([str(item) for item in new_row])

# Ensure there is at least one row before calculating column widths
if not data or len(data[0]) < 4:
    raise ValueError("Data structure is invalid. Check the file content.")

# Define column widths dynamically
col_widths = [max(len(row[i]) for row in data) for i in range(len(data[0]))]

# Function to create a horizontal boundary
def create_boundary():
    return "+".join(["-" * (w + 2) for w in col_widths])

# Writing the updated table
with open(file_path, "w", encoding="utf-8") as file:
    top_border = "+" + create_boundary() + "+"
    file.write(top_border + "\n")

    # Writing data with separators between rows
    for row in data:
        file.write("| " + " | ".join(f"{item:<{col_widths[j]}}" for j, item in enumerate(row)) + " |\n")
        file.write("|" + create_boundary() + "|\n")  # Separator after every row

print(f"New row added to {file_path} successfully!")
