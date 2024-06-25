import zipfile
import os

def backup_folder(folder_path, zip_path):
    # Create a ZIP file object
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        # Iterate over all the files and subdirectories in the folder
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # Get the full path of the file
                file_path = os.path.join(root, file)
                # Ensure the ZIP file is not added to itself
                if file_path != zip_path:
                    # Add the file to the ZIP file
                    zip_file.write(file_path, os.path.relpath(file_path, folder_path))

# Specify the folder path and the ZIP file path
folder_path = '/home/himanshu/Desktop/python_lab'
zip_path = '/home/himanshu/Desktop/python_lab/backup.zip'

# Call the backup_folder function
try:
    backup_folder(folder_path, zip_path)
    print(f"Backup completed successfully. ZIP file created at: {zip_path}")
except Exception as e:
    print(f"An error occurred: {e}")
