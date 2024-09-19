import tkinter as tk
from tkinter import PhotoImage, messagebox



def save_text_to_file(text):
    file_name = my_entry.get() + ".txt"
    with open(file_name, 'w') as file:
        file.write(text)
    print(f"Metin {file_name} dosyasına kaydedildi.")


def encrypt_text():
    result = ""
    text = my_text.get("1.0", tk.END).strip()
    try:
        shift = int(my_entry2.get())
    except ValueError:
        print("Geçersiz Master Key. Lütfen geçerli bir sayı girin.")
        return ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result


def decrypt_text():
    result = ""
    text = my_text.get("1.0", tk.END).strip()
    try:
        shift = int(my_entry2.get())
    except ValueError:
        print("Geçersiz Master Key. Lütfen geçerli bir sayı girin.")
        return

    for char in text:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char

    print(f"Şifre çözülmüş metin: {result}")
    messagebox.showinfo("Şifre Çözülmüş Metin", result)


def combined_func():
    encrypted_text = encrypt_text()
    if encrypted_text:
        save_text_to_file(encrypted_text)


window = tk.Tk()
window.title("Secret Notes")
window.minsize(width=300, height=700)

image = PhotoImage(file="topsecret.png")
image_label = tk.Label(window, image=image)
image_label.place(x=95, y=50)

my_label = tk.Label(window, text="Enter your title", font=('Arial', 10, "italic"))
my_label.place(x=100, y=250)

my_entry = tk.Entry(window, width=20)
my_entry.place(x=80, y=275)

my_label2 = tk.Label(window, text="Enter your secret", font=('Arial', 10, "italic"))
my_label2.place(x=90, y=300)

my_text = tk.Text(window, height=15, width=25)
my_text.place(x=40, y=325)

my_label = tk.Label(window, text="Enter Master Key", font=('Arial', 10, "italic"))
my_label.place(x=90, y=570)

my_entry2 = tk.Entry(window, width=20)
my_entry2.place(x=80, y=595)

my_button = tk.Button(window, text="Save & Encrypt", command=combined_func)
my_button2 = tk.Button(window, text="Decrypt", command=decrypt_text)
my_button.place(x=95, y=625)
my_button2.place(x=115, y=655)

window.mainloop()
