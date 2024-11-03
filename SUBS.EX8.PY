def find_substring_locations(s, t):
    positions = []
    # Iterate over all possible starting positions in s
    for i in range(len(s) - len(t) + 1):
        # Check if substring of s from i to i+len(t) matches t
        if s[i:i+len(t)] == t:
            # Add the position (1-based index) to the list
            positions.append(i + 1)
    return positions

# Function to read s and t from a text file
def read_strings_from_file(file_path):
    with open(file_path, 'r') as file:
        s = file.readline().strip()  # First line for s
        t = file.readline().strip()  # Second line for t
    return s, t

# Main part of the code to use the file input
file_path = 'input.txt'  # Replace with the path to your file
s, t = read_strings_from_file(file_path)
positions = find_substring_locations(s, t)

# Output the positions as a space-separated string
print(" ".join(map(str, positions)))
