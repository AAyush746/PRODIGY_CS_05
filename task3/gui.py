import customtkinter
from customtkinter import CTkButton,CTkFont,CTkFrame
from password_complexity import passchecker

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def check_password():
    username=user_entry1.get()
    password=user_entry2.get()
    result=passchecker(password,username)
    message_label.configure(text=result)
    

root=customtkinter.CTk()
root.geometry("500x300")

frame=customtkinter.CTkFrame(master=root)
frame.pack(pady=12,padx=10,fill="both",expand=True)

label=customtkinter.CTkLabel(master=frame,text="Password Strength Checker",font=CTkFont(family="Cabernet",size=20,weight="bold"))
label.grid(row=0,column=0,columnspan=2,pady=12,padx=10)

username_label=customtkinter.CTkLabel(master=frame,text="Username:",font=CTkFont(family="Cabernet",size=15,weight="bold"))
username_label.grid(row=1,column=0,pady=12,padx=10,sticky="e")

user_entry1=customtkinter.CTkEntry(master=frame,placeholder_text="Enter Username")
user_entry1.grid(row=1, column=1, pady=12, padx=10, sticky="w")

password_label = customtkinter.CTkLabel(master=frame, text="Password:", font=CTkFont(family="Cabernet", size=15, weight="bold"))
password_label.grid(row=2, column=0, pady=12, padx=10, sticky="e")

user_entry2=customtkinter.CTkEntry(master=frame,placeholder_text="Enter Password")
user_entry2.grid(row=2, column=1, pady=12, padx=10, sticky="w")

button=customtkinter.CTkButton(master=frame,text="Check strength",font=CTkFont(family="Cabernet",size=15,weight="bold"),command=check_password)
button.grid(row=3, column=0, columnspan=2, pady=12, padx=10)

message_label=customtkinter.CTkLabel(master=frame,text="",font=CTkFont(family="Cabernet",size=12,weight="bold"))
message_label.grid(row=4, column=0, columnspan=2, pady=12, padx=10)

root.mainloop()
