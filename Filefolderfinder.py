import os
import tkinter as tk


def find():
    

    c = entry.get()

    found = False

    b = os.getcwd()

    a = os.walk(b)

    for dirpath , dirname , filename in a:
        for f in filename:
            if c.lower() in f.lower():
                label3.config(text=f'Your file is in the directory: {dirpath} \n You file name: {f}')
                label4.config(text=dirpath)
                found = True
        for k in dirname:
            if c.lower() in k.lower():
                label3.config(text=f'Your folder is in the directory: {dirpath} \n Your Folder name: {k}')
                label4.config(text=dirpath)
                found = True
    if not found:
        label3.config(text='File/Folder not found.')


def copy_path():
    
    path_text = label4.cget("text")
    if path_text:
        root.clipboard_clear()  
        root.clipboard_append(path_text) 
        btn2.config(text='Copied!') 

root = tk.Tk()
root.geometry('600x250')
root.title('File/Folder Finder')

label = tk.Label(root , text='This is a File/Folder finder.' , font=('Arial',18))
label.pack(pady=10)

label2 = tk.Label(root , text='Keep this application in the folder where you want to find your file/folder in , eg: In C drive ' , font = ('Arial',10))
label2.pack()

entry = tk.Entry(root , width=30)
entry.pack(pady=10)

btn = tk.Button(root, text='Find', height=1, width=15, command=find, bg='#4CAF50', fg='white')
btn.pack(pady=10)

label3 = tk.Label(root , text = '' , font=('Arial',16))
label3.pack(pady=10)

btn2 = tk.Button(root , text = 'Copy' , command=copy_path)
btn2.pack()

label4 = tk.Label(root , text='')

root.mainloop()