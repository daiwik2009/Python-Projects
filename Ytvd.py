import yt_dlp as yt
import subprocess as sb
import os
import tkinter as tk
import threading
from tkinter import ttk
import platform

def startd():
    link = url_entry.get()
    download_thread = threading.Thread(target=run_downloader,args=(link,))
    download_thread.start()

def my_hook(d):

    p = os.path.expanduser('~/Videos')


    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate')
        down = d.get('downloaded_bytes')
        if total:
            percent = (int(down)/int(total))*100
            progress_bar['value'] = percent
            status_label.config(text=f'Downloading..... {percent:.1f}%')
    elif d['status'] == 'finished':
        status_label.config(text='Downloading compleated.')
        open_folder(p)

def run_downloader(link):
    path = os.path.expanduser('~/Videos')
    opts = {
        'format' : 'best',
        'outtmpl' : f'{path}/%(title)s.%(ext)s',
        'progress_hooks':[my_hook]
    }
    with yt.YoutubeDL(opts) as ydl:
        ydl.download([link])

def open_folder(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin": 
        sb.run(["open", path])
    else: 
        sb.run(["xdg-open", path])


root = tk.Tk()
root.title("Youtube Video Downloader")
root.geometry("600x200")

intro_label = tk.Label(root , text = 'Paste Your Youtube URL below and click the button to start downloading:')
intro_label.pack()

url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=10)

download_btn = tk.Button(root, text="Download", command=startd)
download_btn.pack(pady=5)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)

status_label = tk.Label(root, text="Enter a URL to begin")
status_label.pack()

root.mainloop()
