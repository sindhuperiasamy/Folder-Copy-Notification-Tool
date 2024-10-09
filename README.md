# Folder-Copy-Notification-Tool
This Python project is a simple GUI application that allows users to select a folder and copy its contents to a fixed destination folder
After copying, the app sends a desktop notification displaying the folder that was selected and processed. The tool uses tkinter for the graphical user interface (GUI) and plyer for desktop notifications.

**Features**
 - Deletes all existing files from a pre-defined folder (Folder1).
 - Copies files from a user-selected folder (Folder2) to Folder1.
 - Sends a desktop notification with details about the copied folder.
 - Simple, user-friendly graphical interface for folder selection.

**Requirements:**
Before running the program, ensure that you have the following dependencies installed:
 - Python 3.x

**Required libraries:**
 - os.
 - shutil
 - tkinter
 - plyer

**Configure Folder Paths:**

 - Folder1: Update the folder1_path variable in the script to set the destination folder (Folder1) where files will be copied.
 - Initial Directory for Folder2: Optionally, you can set the initial directory for Folder2 browsing by modifying initial_folder2_dir.

**Run the Application: Run the Python script using the command below:**
Open the command Prompt from the project directory and execute the below
**python software_selection.py**

**Using the GUI:**
 - The GUI will open, displaying the static path for Folder1.
 - Use the Browse Folder button to select Folder2 (the source folder).
 - Click the Start Process button to delete existing files in Folder1, copy new files from Folder2 to Folder1, and send a notification.

**Notifications:**
The application sends a desktop notification using the plyer library. 
The notification displays the content of a specific file (currentfolder.txt), which contains the name of the folder that was copied.

**Screenshots**
Refer screenshot.jpg


