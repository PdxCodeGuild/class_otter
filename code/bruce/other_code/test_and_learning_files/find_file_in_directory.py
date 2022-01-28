

# import OS module
import os

# Get the list of all files and directories
path = "./"
list_of_files = os.listdir(path)

print("Files and directories in '", path, "' :")

# prints all files
for file in list_of_files:
    print(file)
