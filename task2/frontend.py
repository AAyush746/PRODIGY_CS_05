import customtkinter
from customtkinter import CTkFont
from tkinter import Label
from backend import open_file_explorer  

customtkinter.set_appearance_mode("blue")
customtkinter.set_default_color_theme("dark-blue")

root=customtkinter.CTk()
root.geometry("500x350")

frame=customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both",expand=True)

label=customtkinter.CTkLabel(master=frame,text="Image Encryption",font=CTkFont(family="Cabernet",size=24))
label.pack(pady=12,padx=10)

label=customtkinter.CTkLabel(master=frame,text="Pick an image",font=CTkFont(family="Cabernet",size=18))
label.pack(pady=12,padx=10)

button=customtkinter.CTkButton(master=frame,text="choose a file",command=lambda:open_file_explorer(frame))
button.pack(pady=12,padx=10)
 

root.mainloop()
