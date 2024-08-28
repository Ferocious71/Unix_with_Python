# Implement a Python script called backup.py that takes a source directory and 
# a destination directory as command-line arguments.

import os,shutil,sys,time 
from datetime import datetime

def backup_files(source_dir, dest_dir):
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: The source directory '{source_dir}' does not exist.")
        return

    # Check if the destination directory exists, create if it does not
    if not os.path.exists(dest_dir):
        try:
            os.makedirs(dest_dir)
            print(f"The destination directory '{dest_dir}' did not exist, so it was created.")
        except OSError as e:
            print(f"Error: Unable to create the destination directory '{dest_dir}'. {e}")
            return

    # Iterate over all files in the source directory
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        
        # Ensure we only copy files, not directories
        if os.path.isfile(source_file):
            dest_file = os.path.join(dest_dir, filename)
            
            # If the file already exists in the destination, append a timestamp to the filename
            if os.path.exists(dest_file):
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename, extension = os.path.splitext(filename)
                dest_file = os.path.join(dest_dir, f"{filename}_{timestamp}{extension}")
            
            # Copy the file
            try:
                shutil.copy2(source_file, dest_file)
                print(f"Copied '{source_file}' to '{dest_file}'")
            except shutil.Error as e:
                print(f"Error copying '{source_file}' to '{dest_file}': {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
    else:
        source_dir = sys.argv[1]
        dest_dir = sys.argv[2]
        backup_files(source_dir, dest_dir)

