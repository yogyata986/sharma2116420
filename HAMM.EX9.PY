def hamming_distance(s, t):
    # Initialize the distance
    distance = 0
    
    # Iterate over both strings simultaneously
    for a, b in zip(s, t):
        # Increment the distance for each differing pair
        if a != b:
            distance += 1
            
    return distance 

# Function to read s and t from a text file 
def read_strings_from_file(file_path):
    with open(file_path, "r") as file:
        s = file.readline().strip()  # First line for s
        t = file.readline().strip()  # Second line for t 
    return s, t 

# Main code execution
file_path = "input.txt"  # Ensure the file name is correct
s, t = read_strings_from_file(file_path)

# Check if the lengths of s and t are equal
if len(s) != len(t):
    print("Error: The two strings must be of equal length.")
else:
    distance = hamming_distance(s, t)
    # Output the Hamming distance
    print(distance)

