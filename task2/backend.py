from PIL import Image, ImageTk
from tkinter import filedialog, Label, simpledialog
import customtkinter
from customtkinter import CTkFont, CTkButton
import os

def open_file_explorer(frame):
    print("opening...")
    file_path = filedialog.askopenfilename(
        title="select an image",
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")]
    )
    if file_path:
        print(f"selected file: {file_path}")
        display_image(file_path, frame)
        button_encrypt = customtkinter.CTkButton(
            master=frame, text="Encrypt the Image", font=CTkFont(family="Cabernet", size=15),
            command=lambda: encrypt_image(file_path)
        )
        button_encrypt.pack(pady=12, padx=10)
        
        button_decrypt = customtkinter.CTkButton(
            master=frame, text="Decrypt the Image", font=CTkFont(family="Cabernet", size=15),
            command=lambda: decrypt_image(file_path)
        )
        button_decrypt.pack(pady=12, padx=10)
                        
def display_image(file_path, frame):
    try:
        image = Image.open(file_path) 
        resized_image = image.resize((300, 200), Image.LANCZOS)
        photo = ImageTk.PhotoImage(resized_image)

        image_label = Label(master=frame, image=photo)
        image_label.image = photo
        image_label.pack(pady=12, padx=10)
    except Exception as e:
        print(f"Error displaying the image: {e}")

def encrypt_image(file_path):
    try:
        key = simpledialog.askinteger("Input", "Enter the key to encrypt the image:")
        print("The path of the file:", file_path)
        print("Key for encryption:", key)
        
        with open(file_path, 'rb') as fin:
            image = fin.read()
        
        encrypted_image = bytearray([byte ^ key for byte in image])
        
        with open(file_path, 'wb') as fout:
            fout.write(encrypted_image)
        
        print("Encryption Done.")
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

def decrypt_image(file_path):
    try:
        key = simpledialog.askinteger("Input", "Enter the key to decrypt the image:")
        with open(file_path, 'rb') as fin:
            encrypted_data = fin.read()

        decrypted_data = bytearray([byte ^ key for byte in encrypted_data])

        decrypted_file_path = file_path.replace(".encrypted", ".decrypted")
        with open(decrypted_file_path, 'wb') as fout:
            fout.write(decrypted_data)

        print(f"Decryption successful! Decrypted file saved as {decrypted_file_path}")
    except Exception as e:
        print(f"An error occurred during decryption: {e}")

