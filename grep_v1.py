import os

input_folder = r'C:\Coding\Python\Codes\Log'
output_file_path = 'output.txt'
search_parameters = ['CXC4040014']

def search_files(input_folder, search_parameters):
    matching_lines = []
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if any(param in line for param in search_parameters):
                        matching_lines.append(line)
    return matching_lines

def save_to_file(output_file_path, matching_lines):
    with open(output_file_path, 'w') as output_file:
        output_file.writelines(matching_lines)

def main():
    matching_lines = search_files(input_folder, search_parameters)
    save_to_file(output_file_path, matching_lines)
    print(f'Saved matching lines to {output_file_path}')

if __name__ == '__main__':
    main()
