from pytube import YouTube
import customtkinter
from tkinter import Listbox
import os
import moviepy.editor
from pygame import mixer
import subprocess

# Default download folder

music_folder = os.path.expanduser('~\\Music')

# Initialize Variables

mixer.init()

# Defining Functions
def Download():
    print(music_folder)
    l = entry.get()
    print(l)
    yt = YouTube(l)
    file = yt.streams.get_lowest_resolution()
    path = file.download(music_folder) # Assigning path to variable because using the video title to get filename might not work if it has special characters.
    mp4 = moviepy.editor.VideoFileClip(os.path.join(music_folder, path))
    try:
        mp4.audio.write_audiofile(os.path.join(music_folder, os.path.splitext(os.path.basename(path))[0] + ".mp3"))
    except Exception as e:
        print(f"Error: {e} \n", "Error creating file, maybe the file already exists?")
    mp4.close()
    os.remove(os.path.join(music_folder, os.path.basename(path)))

def show_in_folder(path):
    subprocess.call(f"explorer {path}")

def play_selected(file:str):
    if mixer.music.get_busy():
        mixer.music.stop()
    if file.endswith('.mp3'):
        print("Now Playing: ", file)
        x = os.path.join(music_folder, file)
        mixer.music.load(x)
        mixer.music.play()


def display_folder_contents(path):
    try:
        folder_contents = os.listdir(path)
        
        for item in folder_contents:
            if item.endswith('.mp3'):
                play_list.insert(customtkinter.END, item)
    except:
        pass
        

# GUI Setup

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

root = customtkinter.CTk()
root.geometry("500x370")
root.title("AudYT")

tab_control = customtkinter.CTkTabview(master=root)


download_frame = customtkinter.CTkFrame(tab_control)
play_frame = customtkinter.CTkFrame(tab_control)


tab_control.add("Download")
tab_control.add("Play") 
tab_control.pack()
# Tabs - Download

label = customtkinter.CTkLabel(master=tab_control.tab("Download"), text="AudYT", font=("Arial", 24))
label.pack(pady=5, padx=10)

label = customtkinter.CTkLabel(master=tab_control.tab("Download"), text="Download", font=("Arial", 12))
label.pack(pady=0, padx=10)


entry = customtkinter.CTkEntry(master=tab_control.tab("Download"), placeholder_text="Enter Link")
entry.pack(pady=20, padx=10)


submit = customtkinter.CTkButton(master=tab_control.tab("Download"), text="Download", command=Download)
submit.pack(pady=20, padx=10)

showinfolder = customtkinter.CTkButton(master=tab_control.tab("Download"), text="Show in folder", command=lambda:[show_in_folder(music_folder)])
showinfolder.pack(pady=0, padx=15)

# Tabs - Play

label = customtkinter.CTkLabel(master=tab_control.tab("Play"), text="AudYT", font=("Arial", 24))
label.pack(pady=5, padx=10)

label = customtkinter.CTkLabel(master=tab_control.tab("Play"), text="Play", font=("Arial", 12))
label.pack(pady=0, padx=10)


play_list = Listbox(master=tab_control.tab("Play"), width=35)
display_folder_contents(music_folder)
play_list.pack()

play_button = customtkinter.CTkButton(master=tab_control.tab("Play"), text="Play Selected", command=lambda:[play_selected(play_list.get(customtkinter.ANCHOR))])
play_button.pack(pady=20)
root.mainloop()
