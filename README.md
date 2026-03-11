# File Organizer Project

## Overview
This project is a Python-based file organizer that helps users automatically organize files in a specified folder. It categorizes files into subfolders based on their types, such as Images, Documents, Videos, Audio, Archives, and more. The project also includes a logging feature to track file movements and errors.

## Features
- Automatically scans and organizes files into categorized folders.
- Supports various file types:
  - **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`
  - **Documents**: `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`
  - **Audio**: `.mp3`, `.wav`, `.m4a`
  - **Videos**: `.mp4`, `.mkv`, `.flv`, `.avi`
  - **Archives**: `.zip`, `.rar`, `.tar`, `.gz`
  - **Scripts**: `.py`, `.js`, `.java`, `.cpp`
  - **Others**: Files that do not match any category are moved to an "Others" folder.
- Automatically creates folders if they do not exist.
- Generates a detailed log file (`organizer_log.txt`) with timestamps.
- Handles errors gracefully with logging and exception handling.

## How to Use
1. Clone this repository to your local machine.
2. Navigate to the `Scripts` folder.
3. Run the `main.py` script using the following command:
   ```
   python main.py
   ```
4. Enter the path of the folder you want to organize when prompted.
5. The script will organize the files into categorized subfolders and generate a log file in the project directory.

## Project Structure
```
FILE-ORGANIZER/
│
├── proj1 FILE O/
│   ├── organizer_log.txt
│   ├── Audio/
│   ├── Documents/
│   │   └── sample.txt
│   ├── Images/
│   ├── Scripts/
│   │   └── main.py
│
└── README.md
```

## Requirements
- Python 3.13 or higher
- Required Python packages: None (uses built-in libraries)

## Future Enhancements
- Add support for more file types.
- Implement a graphical user interface (GUI).
- Add a feature to schedule automatic file organization.

## Author
This project was created by [Your Name].

## License
This project is licensed under the MIT License.
