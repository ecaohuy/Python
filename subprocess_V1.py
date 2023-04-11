import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True, shell=True)
        print("Command output:")
        print(result.stdout)
    except subprocess.CalledProcessError as error:
        print("An error occurred:")
        print(error.stderr)

def main():
    command = "ls -l"
    run_command(command)

if __name__ == '__main__':
    main()


import os
