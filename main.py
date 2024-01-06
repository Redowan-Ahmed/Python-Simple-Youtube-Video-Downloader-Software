from customtkinter import set_appearance_mode , set_default_color_theme, CTk, CTkLabel, CTkEntry, CTkButton, CTkOptionMenu, CTkProgressBar
from tkinter import filedialog, StringVar
from pytube import YouTube

from threading import Thread

set_appearance_mode('System')
set_default_color_theme('blue')

window = CTk()
window.geometry('800x500')
window.title('Redowan- Youtube Video Downloader')

title = CTkLabel(window, text='Insert The youtube link')
title.pack(padx=20, pady=20)

input = CTkEntry(window, border_color='white', corner_radius=50, placeholder_text='Youtube video url', width=500, height=50)
input.pack(padx=20, pady=10)
values = ["High Resulation","Low Resilation"]

input_option = CTkOptionMenu(window,width=500, height=50,dynamic_resizing=True, corner_radius=50, values=values)
input_option.pack(padx=20, pady=10)


def browse_button():
    filename = filedialog.askdirectory()
    file_path.set(filename)


def ErrorHandle(text: str):
    error = CTkLabel(window, text=text, bg_color='red')
    error.pack(padx=20, pady=20)
    return error

def completed( data, fileLocation, *args, **kwargs):
    print(data)
    print('location', fileLocation)
    download_completed = CTkButton(window, text=f"Download Completed and located = {fileLocation}")
    download_completed.pack()

def Progress(stream, chunk, bytes_remaining , *args, **kwargs):
    print(bytes_remaining)
    print('data', stream)
    print('size', stream.filesize)

def downloadExecute():
    try:
        if input.get() and input_option.get() and file_path.get():
            yt = YouTube(url=str(input.get()), on_complete_callback=completed, on_progress_callback=Progress)
            if input_option.get() == 'High Resulation':
                video = yt.streams.get_highest_resolution()
            else:
                video = yt.streams.get_lowest_resolution()
            video.download(output_path=file_path.get())
        else:
            error = ErrorHandle('Please input Something')
    except Exception as e:
        error = CTkLabel(window, text=f'Error : {str(e)}', bg_color='red')
        error.pack(padx=20, pady=20)

def runOnThread():
    Thread(target=downloadExecute).start()



file_path = StringVar()
fileBrowserButton = CTkButton(window, width=500, height=50, corner_radius=50, command=browse_button, text='Select Download Folder', fg_color='red', hover_color='#ff7b72')
fileBrowserButton.pack()
downloadButton = CTkButton(window, width=500, height=50, corner_radius=50, command=runOnThread, text='Start Download', fg_color='red', hover_color='#ff7b72')
downloadButton.pack(padx=20, pady=20)

# progressBar = CTkProgressBar(window, width=500, height=50, corner_radius=50)
# progressBar.set(10)
# progressBar.pack(padx=10, pady=10)

window.mainloop()