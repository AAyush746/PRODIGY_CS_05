import customtkinter
from customtkinter import CTkFont
from backend import analyzer
from scapy.all import sniff
import threading
import tkinter as tk  

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("700x500")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(
    master=frame, text="Network Packet Analyzer", font=CTkFont(family="Cabernet", size=24)
)
label.pack(pady=12, padx=10)

packet_textbox = customtkinter.CTkTextbox(master=frame, width=100, height=15)
packet_textbox.pack(pady=12, padx=10, fill="both", expand=True)

packet_list = []

def update_textbox():
    packet_textbox.delete("1.0", tk.END)  
    for packet in packet_list: 
        packet_info = (
            f"Source MAC: {packet[0]}, Destination MAC: {packet[1]}\n"
            f"Source IP: {packet[2]}, Destination IP: {packet[3]}\n"
            f"Protocol: {packet[4]}, Source Port: {packet[5]}, Destination Port: {packet[6]}\n\n"
        )
        packet_textbox.insert(tk.END, packet_info) 

def start_sniffing():
    sniff(prn=lambda x: analyzer(x, packet_list), count=10, iface="Wi-Fi")
    root.after(1000, update_textbox)

def start_sniffing_thread():
    sniff_thread = threading.Thread(target=start_sniffing)
    sniff_thread.daemon = True
    sniff_thread.start()

button = customtkinter.CTkButton(
    master=frame, text="Start Sniffing", font=CTkFont(family="Cabernet", size=18), command=start_sniffing_thread
)
button.pack(pady=12, padx=10)

root.mainloop()
