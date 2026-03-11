import os
import shutil
import logging

file_location_path = input("enter the folder path to organize files: ").strip()
# Your folder path
source_folder = r"c:\Users\ASUS\Desktop\FILE ORGANIZER\FILE-ORGANIZER\proj1 FILE O"

# Log file setup
log_file = os.path.join(source_folder, "organizer_log.txt")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)

# File type mapping
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.m4a'],
    'Videos': ['.mp4', '.mkv', '.flv', '.avi'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.java', '.cpp']
}

# Create folder if it doesn't exist
def create_folder(folder_path):
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            logging.info(f"Created folder: {folder_path}")
    except Exception as e:
        logging.error(f"Failed to create folder {folder_path}: {e}")

# Organize files with exception handling
def organize_files():
    try:
        for filename in os.listdir(source_folder):
            if filename == "organizer_log.txt":
                continue  # Don't touch the log file!

            file_path = os.path.join(source_folder, filename)

            if os.path.isfile(file_path):
                file_ext = os.path.splitext(filename)[1].lower()
                moved = False

                for folder_name, extensions in file_types.items():
                    if file_ext in extensions:
                        destination_folder = os.path.join(source_folder, folder_name)
                        create_folder(destination_folder)
                        try:
                            shutil.move(file_path, os.path.join(destination_folder, filename))
                            logging.info(f"Moved {filename} to {folder_name}")
                        except Exception as e:
                            logging.error(f"Error moving {filename} to {folder_name}: {e}")
                        moved = True
                        break

                if not moved:
                    other_folder = os.path.join(source_folder, 'Others')
                    create_folder(other_folder)
                    try:
                        shutil.move(file_path, os.path.join(other_folder, filename))
                        logging.info(f"Moved {filename} to Others")
                    except Exception as e:
                        logging.error(f"Error moving {filename} to Others: {e}")

        print(" All files have been organized. Check log for details.")
    except Exception as e:
        logging.critical(f"Unexpected error in organize_files(): {e}")
        print(" Something went wrong! Check the log file.")


# Run it
organize_files()
