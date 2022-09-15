from tkinter import *
from tkinter import ttk, messagebox, filedialog
from pytube import YouTube
import _thread

storagePath = r"E:\Tutorials\sudoku solver project advanced\ytlectures"
#this 'r' is converting the normal string to raw string

#main window
root = Tk();
root.title("Youtube Video Downloader");
root.geometry("500x420");

#to remove the resizeable(maximizing the window) feature
root.resizable(0, 0);

#download function
def show_progress_bar(stream, chunks, bytes_remaining):
    progress = int(((stream.filesize - bytes_remaining) / stream.filesize) * 100)
    bar["value"] = progress

def download():
    quality = ytbchoices.get();
    url = link.get();
    if len(url) > 0:
        msg["text"] = "Extracting video from youtube..."
        ytb_url = YouTube(url, on_progress_callback=show_progress_bar) #extracting the video informationn
        video = ytb_url.streams.filter(progressive=True, file_extension='mp4').order_by("resolution").desc()
        msg["text"] = "Downloading\n" + ytb_url.title
        if quality == choices[0]:
            video.last().download(storagePath)
        else :
            video.first().download(storagePath)
    else :
        urlErr["text"] = "Please Enter the URL"

    msg["text"] = "Downloaded succesfully"
    messagebox.showinfo("Download info", "Downloaded successfully and saved to\n" + storagePath)

#heading
Label(root, text = "Youtube Video Downloader", font = 'arial 20 bold').pack();

#url entry
Label(root, text = "Paste the link here", font = 'arial 15 bold').pack();
link = StringVar();
link_enter = Entry(root, textvariable = link, width = 70).pack();

#url error message
urlErr = Label(root, font = 'arial 12', fg = 'red');
urlErr.pack()


#quality of the video
Label(root, text="Select the quality of the video", font = 'arial 12 bold').pack(pady=10);
choices = ["low", "high"];
ytbchoices = ttk.Combobox(root, values = choices);
ytbchoices.pack();


#progress bar
bar = ttk.Progressbar(root, length = 300);
bar.pack(pady = 10);

#msg
msg = Label(root, font = 'arial 12', fg='green');
msg.pack();

#download button
Button(root, text="DOWNLOAD", fg = 'white', bg = '#E21717', width = 17, height=2, command = lambda: _thread.start_new_thread(download, ())).pack(pady = 10);
#this whole lambda thing will solve the freezing problem of the download button (previously it was showing window not responding)

root.mainloop();