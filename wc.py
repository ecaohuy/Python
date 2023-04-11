def wc_l(file_path):
    with open(file_path, 'r') as f:
        line_count = 0
        for line in f:
            line_count += 1
    print(line_count)

# Example usage: count the number of lines in a file
wc_l('H01033__LN.log')