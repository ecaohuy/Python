import re

def grep(file_path, pattern):
    with open(file_path, 'r') as f:
        for line in f:
            if re.search(pattern, line):
                print(line.strip())

# Example usage: search for lines containing the word "apple" in a file
grep('H01033__LN.log', ' ENodeBFunction=')