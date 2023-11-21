from pytube import YouTube
import customtkinter
import os

# Default download folder

music_folder = os.path.expanduser('~\\Music')



# GUI Setup

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()
root.geometry("500x300")
root.title("AudYT")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="AudYT", font=("Arial", 24))
label.pack(pady=20, padx=10)

entry = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Link")
entry.pack(pady=20, padx=10)





# Defining Functions
def Download():
    print(music_folder)
    l = entry.get()
    print(l)
    yt = YouTube(l)
    audio = yt.streams.filter(only_audio=True)
    audio[0].download(output_path=music_folder)


submit = customtkinter.CTkButton(master=frame, text="Download", command=Download)
submit.pack(pady=20, padx=10)
root.mainloop()