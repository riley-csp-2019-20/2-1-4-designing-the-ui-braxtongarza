##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk
from tkinter import*

# main window
root = tk.Tk()
root.wm_geometry("200x200")
root.wm_title("authentication")



# create empty frame
frame_login = tk.Frame(root)
frame_login.grid(row=0,column=0, sticky="news")
 

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack(padx=50)

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_password = tk.Label(frame_login, text='Password:')
lbl_password.pack(padx=50)

ent_password = tk.Label(frame_login, bd=4)
ent_password.pack(pady=5)


def callback():
    print ("click!")

b = Button(frame_login, text ="Login", command=callback)
b.pack()



root.mainloop()

frame_auth = tk.RAISED(root)
frame_auth.grid(row=0,column=0, sticky="news")
mainloop()