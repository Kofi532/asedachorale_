import os

def delete_all_files(directory):
    # Get the list of files in the directory
    file_list = os.listdir(directory)

    # Iterate through the files and delete each one
    for file_name in file_list:
        file_path = os.path.join(directory, file_name)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

# Replace 'your_directory_path' with the path of the directory you want to clear
directory_path = '/home/kofi532/asedachorale/media'
delete_all_files(directory_path)
