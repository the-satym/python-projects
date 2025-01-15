#date: 15 jan 2025


import qrcode
data=input("enter the text of url:-   ").strip()
f=input("enter the filename you want to save as:-  ").strip()
qr=qrcode.QRCode(box_size=20, border= 5)
qr.add_data(data)
image=qr.make_image(fill_color="black",back_color="white")
image.save(f)
print(f'qrcode is saved as {f}')