data = [
    ["S.No", "Question", "Link", "Company"],
    [1, "Equilibrium Point", "https://www.geeksforgeeks.org/problems/equilibrium-point-1587115620/1?page=1&category=Arrays&sortBy=submissions", 
     "Amazon, Adobe, Google, Facebook, Microsoft, Uber"]
]

# Define column widths dynamically based on content
col_widths = [max(len(str(row[i])) for row in data) for i in range(len(data[0]))]

# Function to create a horizontal boundary
def create_boundary():
    return "+".join(["-" * (w + 2) for w in col_widths])

# Writing the table to a file
with open("DSA/Arrays/Prefix_sum/Questions.txt", "w", encoding="utf-8") as file:
    top_border = "+" + create_boundary() + "+"
    file.write(top_border + "\n")

    # Writing data
    for i, row in enumerate(data):
        file.write("| " + " | ".join(f"{str(item):<{col_widths[j]}}" for j, item in enumerate(row)) + " |\n")
        if i == 0:  # Header separator
            file.write("|" + create_boundary() + "|\n")
    
    bottom_border = "+" + create_boundary() + "+"
    file.write(bottom_border + "\n")

print("Table written to table.txt successfully!")
