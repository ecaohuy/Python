def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()
def read_file_into_list(file_name):
    with open(file_name, 'r') as file:
        content_list = file.readlines()
    return content_list
print(read_file_into_list('test.log'))