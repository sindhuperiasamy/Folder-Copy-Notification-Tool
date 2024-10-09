import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from plyer import notification

# Define Folder1 as a static (fixed) path
folder1_path = r"C:\Users\smohanku\Downloads\browse_copy2another_folder\main"  # Set your static path here

# Define the initial directory for Folder2 browsing
initial_folder2_dir = r"C:\Users\smohanku\Downloads\browse_copy2another_folder\project"

# Path to the text file for notification
file_path = r'C:\Users\smohanku\Downloads\browse_copy2another_folder\main\currentfolder.txt' 

# Function to delete all files in main folder
def delete_files_in_folder(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        print(f"Deleted all files from {folder_path}")
    except Exception as e:
        print(f"Failed to delete files in {folder_path}. Reason: {e}")

# Function to copy files from some Folder to main folder
def copy_files(src_folder, dest_folder):
    try:
        files = os.listdir(src_folder)
        for file in files:
            src_file = os.path.join(src_folder, file)
            dest_file = os.path.join(dest_folder, file)
            if os.path.isfile(src_file):
                shutil.copy(src_file, dest_file)
        print(f"Copied files from {src_folder} to {dest_folder}")
    except Exception as e:
        print(f"Failed to copy files. Reason: {e}")

# Function to send notification which folder was selected.
def send_notification():
    try:
        # Check if the file exists first
        if not os.path.exists(file_path):
            print(f"File {file_path} does not exist. Skipping notification.")
            return

        # Read text from the file
        with open(file_path, 'r') as file:
            text = file.read()

        # Display the notification
        notification.notify(
            title='Copied Folder is:',
            message=text,
            app_name='Test',
            timeout=10  # Duration in seconds
        )
        print("Notification sent successfully.")
    except Exception as e:
        print(f"Failed to send notification. Reason: {e}")

# Function to handle folder selection and process execution
def process_folders(folder2, root):
    if not os.path.exists(folder1_path):
        messagebox.showerror("Error", f"Folder1 does not exist: {folder1_path}")
        return
    if not folder2 or not os.path.exists(folder2):
        messagebox.showerror("Error", "Please select a valid software folder (Folder2).")
        return
    
    # Step 1: Delete files in Folder1
    delete_files_in_folder(folder1_path)
    
    # Step 2: Copy files from Folder2 to Folder1
    copy_files(folder2, folder1_path)
    
    # Step 3: Send notification
    send_notification()
    
    # Show success message
    messagebox.showinfo("Success", "Process completed successfully!")
    
    # Close the GUI after the process is complete
    root.destroy()

# GUI for folder selection
def select_folder():
    folder = filedialog.askdirectory(initialdir=initial_folder2_dir)
    return folder

# GUI setup using tkinter
def gui():
    root = tk.Tk()
    root.title("Choose Folder")
    root.geometry("600x350")
    
    folder2_var = tk.StringVar()
    
    # Show static path for Folder1
    tk.Label(root, text=f"Select folder to copy to main folder: {folder1_path}").pack(pady=10)
    
    # Folder 2 selection
    tk.Label(root, text="Select the folder:").pack(pady=10)
    folder2_entry = tk.Entry(root, textvariable=folder2_var, width=80)
    folder2_entry.pack(pady=5)
    tk.Button(root, text="Browse Folder", command=lambda: folder2_var.set(select_folder())).pack(pady=5)
    
    # Start process button
    tk.Button(root, text="Start Process", command=lambda: process_folders(folder2_var.get(), root)).pack(pady=10)
    
    root.mainloop()
    
# Run the GUI
if __name__ == "__main__":
    gui()
