import os
import tkinter as tk
from tkinter import filedialog
import eyed3

def select_folder():
    folder_path = filedialog.askdirectory(title="Select Folder")
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, folder_path)

def process_audio_files(folder_path, start_number):
    for i, filename in enumerate(os.listdir(folder_path)):
        if filename.lower().endswith('.mp3'):
            new_filename = f"audio{start_number + i:03}.mp3"
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            audio_file = eyed3.load(os.path.join(folder_path, new_filename))
            # Set properties here using audio_file.tag
            audio_file.tag.title = "Title"
            audio_file.tag.artist = "Artist"
            audio_file.tag.album = "Album"
            audio_file.tag.save()

def process_button_clicked():
    folder_path = folder_path_entry.get()
    start_number = int(start_number_entry.get())
    process_audio_files(folder_path, start_number)

# Create the UI
root = tk.Tk()
root.title("MP3 File Fixer")

start_number_label = tk.Label(root, text="Enter the starting number:")
start_number_label.pack()

start_number_entry = tk.Entry(root)
start_number_entry.pack()

folder_path_label = tk.Label(root, text="Selected Folder:")
folder_path_label.pack()

folder_path_entry = tk.Entry(root)
folder_path_entry.pack()

select_folder_button = tk.Button(root, text="Select Folder", command=select_folder)
select_folder_button.pack()

process_button = tk.Button(root, text="Process", command=process_button_clicked)
process_button.pack()

root.mainloop()
