import os

# Set the directory containing the files
directory = 'maritime images'

# Set the base name for the files
base_name = 'image'

# Set the starting index number
start_index = 1

# Get a list of files in the directory
file_list = os.listdir(directory)

# Sort the file list in alphabetical order
file_list.sort()

# Rename files in bulk and sequence
for index, filename in enumerate(file_list, start=start_index):
    extension = os.path.splitext(filename)[1]  # Get the file extension
    new_filename = f'{base_name}_{index:03d}{extension}'  # Create the new filename
    old_path = os.path.join(directory, filename)  # Get the old file path
    new_path = os.path.join(directory, new_filename)  # Get the new file path
    os.rename(old_path, new_path)  # Rename the file
