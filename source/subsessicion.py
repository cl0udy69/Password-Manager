import os
import subprocess

# Specify the main directory where all the Python files are located
main_directory = os.path.join(os.path.expanduser("~"), "Desktop")

# List of file paths relative to the main directory
file_paths = [
    'folder1/address_function.py',
    'folder2/banking_function.py',
    'folder3/ssn_function.py',
    # Add more file paths as needed
]

# Iterate over each file path and run the Python file
for file_path in file_paths:
    full_path = os.path.join(main_directory, file_path)
    subprocess.run(['python', full_path])
