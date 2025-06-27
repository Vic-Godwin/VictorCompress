from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
import re
import sys,time
import base64, zlib
from compress_module import compress as com, decompress as de


def read():
    file = open(entry.get(),'r')
    text_output.delete("1.0","end")
    text_output.insert("end",file.read())

def search():
    text_output.delete("1.0","end")
    file = open(entry.get())
    word = entry1.get().capitalize()
    count = 0
    for line in file:
        count +=1
        line = line.rstrip()
        if line.startswith(word):
            text_output.insert("end", line + "\n\n")

def convert():
    filepath = entry.get()
    if not filepath:
        text_output.insert("end", "No file path provided.\n")
        return

    try:
        if option2.get().upper() == "COMPRESS":
            # Compress and write to new file
            compressed_data = com(filepath)
            output_path = "compressed_output.txt"
            with open(output_path, "w") as f:
                f.write(compressed_data.decode("utf-8"))
            entry.delete(0, "end")
            entry.insert(0, output_path)
            text_output.insert("end", f"Compressed and saved to {output_path}\n")

        elif option2.get().upper() == "DECOMPRESS":
            # Decompress and write to new file
            decompressed_data = de(filepath)
            output_path = "decompressed_output.txt"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(decompressed_data.decode("utf-8"))
            entry.delete(0, "end")
            entry.insert(0, output_path)
            text_output.insert("end", f"Decompressed and saved to {output_path}\n")
    except Exception as e:
        text_output.insert("end", f"Error: {str(e)}\n")

        
    
            
def extract():
    text_output.delete("1.0","end")
    file = open(entry.get())
    options = option.get()
    count = 0
    for line in file:
        line = line.rstrip()

        if options == "file details".upper():
            word = entry1.get().capitalize()
            read_file = file.read()
            char_in_file = len(read_file)
            filewords = read_file.split()

            count = 0
            counting = 0
            
            for search in filewords:
                count += 1
                if search.lower() == word.lower():
                    counting += 1
                    continue
            words = count
            text_output.insert("end",f"""
    Number of words in file =  {words}\n
    The word '{word}' appeared {counting} times\n
    Number of characters in file =  {char_in_file}""".upper())
           

        if options == "email".upper():
            e_mail = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}",line)
            for email in e_mail:
                count +=1
                text_output.insert("end",  f"Email {count}:    {''.join(email)}" + "\n\n")
        
        if options == "phone number".upper():
            phone = re.findall(r"\b\+?[-.\s]?\d{1,}[-.\s]?\d{1,}[-.\s]?\d{2,}\b",line)
            for number in phone:
                if len(number) < 11:
                    continue
                count += 1
                text_output.insert("end",  f"Phone Number {count}:     {''.join(number)}" + "\n\n")
        
        if options == "date".upper():

            dates = re.findall(
                r"\b\d{2}/\d{2}/\d{4}\b|"       # Matches 12/03/2025
                r"\b\d{2} [A-Za-z]{3} \d{4}\b|" # Matches 12 Mar 2025
                r"\b\d{4}-\d{2}-\d{2}\b|"       # Matches 2025-05-19
                r"\b\d{2}-\d{2}-\d{4}",         # Matches 19-05-2025
                line
            )
            for date in dates:
                count += 1
                text_output.insert("end",f"Date  {count}:    {''.join(date)}" + "\n\n")


        if options == "address".upper():
            count = 0
            addresses = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}",line)
            for address in addresses:
                count +=1
                text_output.insert("end",  f"Address {count}: {''.join(address)}" + "\n\n")


root = Tk()
root.title('Read Your Text File')
root.geometry("700x500")
root.minsize(600,400)
root.state("zoom")
root.iconbitmap("victor_logo_64x64.ico")
root.configure(bg="lightgray")
root.resizable(False, False)

frame = Frame(root,bg="gray")
frame.pack(fill="both",side="top")

frame1 = Frame(frame,bg="white")
frame1.pack(fill="x",expand=True,side="left",padx=20,pady=10)

frame2 = Frame(frame,bg="white")
frame2.pack(fill="x",expand=True,side="left",padx=20,pady=10)

frame3 = Frame(frame,bg="white")
frame3.pack(fill="x",expand=True,side="left",padx=20,pady=10)

frame4 = Frame(frame,bg="white")
frame4.pack(fill="x",expand=True,side="left",padx=20,pady=10)

entry = Entry(frame1,font=("Segoe UI", 14),width=30)
entry.pack(fill="both",side="left",ipadx=10,pady=1)
Button(frame1,text="ReadFile",relief="flat",bg="gray",fg="white",font=("Segoe UI", 10),command=read).pack(fill="both",side="left",ipadx=10,pady=1)

entry1 = Entry(frame2,font=("Segoe UI", 14),width=15)
entry1.pack(fill="both",side="left",ipadx=10,pady=1)
Button(frame2,text="Search",relief="flat",bg="gray",fg="white",font=("Segoe UI", 10),command=search).pack(fill="both",side="left",ipadx=15,pady=1)

option2 = StringVar()
ttk.Combobox(frame4,textvariable=option2,
    values=["COMPRESS","DECOMPRESS"], state="readonly",
    font=("Segoe UI", 10)).pack(fill="both",side="left",ipadx=5,pady=1)

Button(frame4,text="convert",relief="flat",bg="gray",fg="white",font=("Segoe UI", 10),command=convert).pack(fill="both",side="left",ipadx=15,pady=1)

option = StringVar()
ttk.Combobox(frame3,textvariable=option,
    values=["EMAIL","PHONE NUMBER","DATE","ADDRESS","FILE DETAILS"], state="readonly",
    font=("Segoe UI", 10)).pack(fill="both",side="left",ipadx=20,pady=1)

Button(frame3,text="Extract",relief="flat",bg="gray",fg="white",font=("Segoe UI", 10),command=extract).pack(fill="both",side="left",ipadx=30,pady=1)

text_output = scrolledtext.ScrolledText(root, font=("Arial", 14), height=5)
text_output.pack(fill="both",expand=True, padx=20, pady=5)

root.mainloop()
