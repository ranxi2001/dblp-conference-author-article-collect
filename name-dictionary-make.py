common_surnames = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez","Ibrahim","Chris","Ozan","Croitoru","Melton","Fabbri",
    "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore","Singh","Manolis","Karimi","Dimosthenis","Roberto",
    "Jackson", "Martin", "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez","Kim","Enrico","Doruk","Sudhakaran",
    "Lewis", "Robinson", "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen","Niccolo","Prune","Fabio","Jake","Andrew",
    "Hill", "Flores", "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell","Felix","Brian","Yannick","Sidharth",
    "Carter", "Roberts"
]
# Function to extract names (4th content) from given lines
def extract_names(lines):
    return [line.split(',')[3] for line in lines]

# Read the uploaded files and extract names
with open("./PR.txt", 'r', encoding='utf-8') as file_pr, open("./TR.txt", 'r', encoding='utf-8') as file_tr:
    names_pr = file_pr.readlines()
    names_tr = file_tr.readlines()
# Strip any trailing whitespace and merge the names
all_lines = [name.strip() for name in names_pr + names_tr]
all_names = extract_names(all_lines)


# Extend the common_surnames list with the new names
common_surnames_extended = common_surnames + all_names

# Remove any duplicates
common_surnames_extended = list(set(common_surnames_extended))

# Sort the list
common_surnames_extended.sort()

# # Display the extended list in the original format
# formatted_list = "common_surnames = [\n" + ",\n".join(f'    "{name}"' for name in common_surnames_extended) + "\n]"
# print(formatted_list)

# Function to format names into chunks per line
def format_names(names, per_line=400):
    lines = []
    for i in range(0, len(names), per_line):
        chunk = ', '.join(f'"{name}"' for name in names[i:i+per_line])
        lines.append(f'    {chunk}')
    return "[\n" + ",\n".join(lines) + "\n]"

# Sample surnames for demonstration (assuming you've already defined `common_surnames_extended`)
# common_surnames_extended = ["Name1", "Name2", "Name3", "Name4", "Name5", "Name6", "Name7", "Name8", "Name9", "Name10"]

formatted_list = f'common_surnames = {format_names(common_surnames_extended)}'
print(formatted_list)
