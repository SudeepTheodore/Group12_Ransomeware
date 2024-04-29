import os
import shutil
from datetime import datetime

def backup_files(source_dir, backup_dir):
    # Get the current time to create a unique backup folder each time
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_subdir = os.path.join(backup_dir, f'backup_{now}')

    # Create a backup directory if it doesn't exist
    os.makedirs(backup_subdir, exist_ok=True)

    # Walk through all files and directories in the source directory
    for root, dirs, files in os.walk(source_dir):
        # Determine the path to the destination directory
        dest_dir = os.path.join(backup_subdir, os.path.relpath(root, source_dir))
        os.makedirs(dest_dir, exist_ok=True)

        # Copy each file in this directory to the destination directory
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)
            shutil.copy2(src_file, dest_file)
            print(f'Copied {src_file} to {dest_file}')

    print(f'Backup completed successfully to {backup_subdir}')

# Set the source and backup directories
source_directory = 'C:\\Users\\nsude\\OneDrive\\Desktop\\ransom'
backup_directory = 'C:\\Users\\nsude\\OneDrive\\Desktop\\backup'

backup_files(source_directory, backup_directory)
