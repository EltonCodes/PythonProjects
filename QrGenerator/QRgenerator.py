from tkinter import *
import os
import qrcode

#import qrcode

root = Tk()
root.title('QR generator')
root.geometry('1000x550')
root.config(bg='#0F997D')
root.resizable(False, False)

#icon image
#image_icon = PhotoImage(file='QRcodes/Hello.png')

def generate():
    try:
        name = title.get()
        text = entry.get()
        qr = qrcode.make(text)
        qr.save('QRcodes/'+ str(name) + '.png')
    except FileNotFoundError:
        new_folder = os.makedirs('QrCodes')
        name = title.get()
        text = entry.get()
        qr = qrcode.make(text)
        qr.save('QrCodes/' + str(name) + '.png')

    Label(root, text='Your QR code generated! \n Thanks for choosing us!', fg='black', bg='#0F997D', font=('Open Sans', 12, 'bold')).place(x=50, y=400)

    global image
    image=PhotoImage(file='QRcodes/' + str(name) + '.png')
    image_view.config(image=image)

image_view=Label(root, bg='#0F997D')
image_view.pack(padx=50,pady=10,side=RIGHT)

Label(root, text='Welcome to QrGenerator!', fg='white', bg='#0F997D', font=('Open Sans', 25, 'bold')).place(x=40, y=40)
Label(root, text='Title for QR:', fg='white', bg='#0F997D', font=('Open Sans', 12, 'bold')).place(x=50, y=170)
Label(root, text='Content to display:', fg='white', bg='#0F997D', font=('Open Sans', 12, 'bold')).place(x=50, y=230)
Label(root, text='QrGenerator v1.0 \n Developed by Rustamov Elbek', fg='white', bg='#0F997D',
      font=('Open Sans', 11)).place(x=770,y=500)

title=Entry(root, width=13, font=('Open Sans', 12, 'italic'))
title.place(x=50,y=200)
entry=Entry(root, width=28, font=('Open Sans', 12, 'italic'))
entry.place(x=50, y=260)

Button(root,text='Generate',font=('Open Sans', 9, 'bold'), width=20, height=2, bg='#6AF5D8', fg='black',command=generate).place(x=50, y=310)

root.mainloop()