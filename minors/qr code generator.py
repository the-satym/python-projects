#date: 15 jan 2025

import qrcode
from tkinter import *
import os
from pathlib import Path


root = Tk()
root.geometry("300x300")
root.title("QR Code generator")
label1=Label(root,text="enter your URL here").grid(row=0,column=1)
label2=Label(root,text="enter file name you want to save as").grid(row=3,column=1)

e=Entry(root)
e.grid(row=1,column=1)
f=Entry(root)
f.grid(row=4,column=1)

def button_1():
    data = e.get()
    file = f.get()
    download_folder=str(Path.home()/"downloads")
    file_path=os.path.join(download_folder,file)
    qr = qrcode.QRCode(box_size=20, border=5)
    qr.add_data(data)
    image = qr.make_image(fill_color="black", back_color="white")
    image.save(file_path)
    print(f'QR Code is saved at {file_path}')


button1=Button(root,text="generate qr code",padx=15,pady=8,command=button_1)
button1.grid(row=6,column=1)

root.mainloop()