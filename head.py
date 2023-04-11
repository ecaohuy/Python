import sys

def head(file_path, num_lines):
    with open(file_path, 'r') as f:
        for i in range(num_lines):
            line = f.readline()
            if not line:
                break
            sys.stdout.write(line)

# Example usage: print the first 10 lines of a file
head('File/H01033__LN.log', 10)
