import os
import subprocess
import shutil
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import filedialog, Canvas, PhotoImage, StringVar
import tkinter as tk
from compress_module import compress as com, decompress as de
import sys

def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller EXE.
    """
    try:
        base_path = sys._MEIPASS  # Temporary folder used by PyInstaller(Can't Forget my The Last Error.)
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ------------------ GlowButton: Custom Button Class ------------------ #
class GlowButton(tk.Canvas):
    def __init__(self, parent, text="", command=None, fg="white", bg="#1f1f2e", glow_color="#00f0ff", **kwargs):
        super().__init__(parent, width=140, height=50, bg=bg, highlightthickness=0, bd=0)
        self.command = command
        self.bg = bg
        self.glow_color = glow_color

        # Draw background rounded rectangle
        self.rect = self.create_rounded_rect(10, 10, 130, 40, r=20, fill=bg, outline=glow_color, width=2)

        # Add glowing text
        self.label = self.create_text(70, 25, text=text, font=("Segoe UI", 11, "bold"), fill=fg)

        # Bind events
        self.bind("<Button-1>", self.on_click)
        self.bind("<Enter>", lambda e: self.itemconfig(self.rect, outline=self.glow_color))
        self.bind("<Leave>", lambda e: self.itemconfig(self.rect, outline=self.bg))

    def on_click(self, event):
        if self.command:
            self.command()

    def create_rounded_rect(self, x1, y1, x2, y2, r=25, **kwargs):
        points = [
            x1 + r, y1,
            x2 - r, y1,
            x2, y1,
            x2, y1 + r,
            x2, y2 - r,
            x2, y2,
            x2 - r, y2,
            x1 + r, y2,
            x1, y2,
            x1, y2 - r,
            x1, y1 + r,
            x1, y1
        ]
        return self.create_polygon(points, smooth=True, **kwargs)


# ------------------ Victor Compress Main App ------------------ #
class VictorCompressApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Victor Compress - Lighten Your Load")
        # Use resource_path for icon (important for .exe packaging)
        self.root.iconbitmap(resource_path("victor_logo_64x64.ico"))
        self.root.geometry("600x500")
        self.root.configure(bg="#101626")  # Simulate dark gradient background
        self.root.resizable(False, False)

        # Load custom theme for ttkbootstrap
        self.style = tb.Style("cyborg")

        # ------------------ Logo and Title ------------------ #
        self.title_frame = tk.Frame(self.root, bg="#101626")
        self.title_frame.pack(pady=20)

        # Logo (fallback to ⚡ if image not found)
        try:
            logo = resource_path("victor_logo_64x64.png")
            self.logo = PhotoImage(file=logo)
            self.logo_label = tk.Label(self.title_frame, image=self.logo, bg="#101626")
        except:
            self.logo_label = tk.Label(self.title_frame, text="⚡", font=("Segoe UI", 24), fg="white", bg="#101626")
        self.logo_label.pack(side=tk.LEFT, padx=10)

        # Title Text
        title = tk.Label(self.title_frame, text="Victor Compress", font=("Segoe UI", 22, "bold"), fg="white", bg="#101626")
        subtitle = tk.Label(self.title_frame, text="Lighten Your Load", font=("Segoe UI", 11), fg="#CCCCCC", bg="#101626")
        title.pack(anchor="w")
        subtitle.pack(anchor="w")

        # ------------------ File Input Section ------------------ #
        self.file_frame = tk.Frame(self.root, bg="#101626")
        self.file_frame.pack(pady=10)

        self.file_path = StringVar()
        self.entry = tk.Entry(self.file_frame, textvariable=self.file_path, width=40, font=("Segoe UI", 10), bg="#1e1e2f", fg="white", insertbackground='white', relief="flat")
        self.entry.pack(side=tk.LEFT, padx=(0, 10), ipady=5)

        self.browse_btn = GlowButton(self.file_frame, text="Browse...", command=self.browse_file, glow_color="#5555ff")
        self.browse_btn.pack(side=tk.LEFT)

        # ------------------ Compress / Decompress / Clear Buttons ------------------ #
        self.action_frame = tk.Frame(self.root, bg="#101626")
        self.action_frame.pack(pady=30)

        self.compress_btn = GlowButton(self.action_frame, text="Compress", glow_color="#00aaff", command=self.mock_compress)
        self.compress_btn.grid(row=0, column=0, padx=10)

        self.decompress_btn = GlowButton(self.action_frame, text="Decompress", glow_color="#00ffd5", command=self.mock_decompress)
        self.decompress_btn.grid(row=0, column=1, padx=10)

        self.clear_btn = GlowButton(self.action_frame, text="Clear", glow_color="#ff00c8", command=self.clear_all)
        self.clear_btn.grid(row=0, column=2, padx=10)

        self.read_btn = GlowButton(self.action_frame, text="Open Reader", glow_color="#00ff88", command=self.open_reader)
        self.read_btn.grid(row=1,column=0,pady=3)

        self.copy_path_btn = GlowButton(self.action_frame, text="📋clipboard", glow_color="#ffaa00", command=self.copy_file_path,cursor="hand2")
        self.copy_path_btn.grid(row=1, column=1,pady=3) 


        # ------------------ Progress Bar ------------------ #
        self.progress = tb.Progressbar(self.root, length=400, mode='determinate', bootstyle="info-striped")
        self.progress.pack(pady=10)

        # ------------------ Status Label ------------------ #
        self.status_label = tk.Label(self.root, text="No action yet", font=("Segoe UI", 10), fg="#cccccc", bg="#101626")
        self.status_label.pack()

        # ------------------ Download Button ------------------ #
        self.download_btn = GlowButton(self.root, text="Download", glow_color="#aaaaaa", command=self.mock_download)
        self.download_btn.pack(pady=20)

    # ------------------ Browse Button Function ------------------ #
    def browse_file(self):
        file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file:
            self.file_path.set(file)
            self.status_label.config(text="File selected")

    # ------------------ Mock Compress Action ------------------ #
    def mock_compress(self):
            if not self.file_path.get():
                self.status_label.config(text="Please select a file first.")
                return

            try:
                self.status_label.config(text="Compressing...")
                self.progress.start(10)

                # Calling the real compress function
                compressed_data = com(self.file_path.get())  # bytes

                # Ask user for where to save the compressed file
                dest = filedialog.asksaveasfilename(
                    defaultextension=".txt",
                    filetypes=[("Compressed Files", "*.txt"),
                               ("Compressed Files", "*.doc"),
                              ]
                )
                if dest:
                    with open(dest, "wb") as f:
                        f.write(compressed_data)

                    self.status_label.config(text="File compressed and saved")
                    self.output_file_path = dest # store path for download
                else:
                    self.status_label.config(text="Save cancelled")

            except Exception as e:
                self.status_label.config(text=f"Error: {e}")

            finally:
                self.progress.stop()

    # ------------------ Mock Decompress Action ------------------ #
    def mock_decompress(self):
            if not self.file_path.get():
                self.status_label.config(text="Please select a file first.")
                return

            try:
                self.status_label.config(text="Decompressing...")
                self.progress.start(10)

                # Call your real decompress function
                decompressed_data = de(self.file_path.get())  # bytes

                # Ask where to save the decompressed content
                dest = filedialog.asksaveasfilename(
                    defaultextension=".txt",
                    filetypes=[("Text Files", "*.txt"),
                               ("PDF Files", "*.pdf"),
                               ("Doc Files", "*.doc"),
                               ("EPUB Files", "*.epub")]
                )
                if dest:
                    with open(dest, "w", encoding="utf-8") as f:
                        f.write(decompressed_data.decode('utf-8'))
                    self.status_label.config(text="File decompressed and saved")
                    self.output_file_path = dest # store path for download

                    self.status_label.config(text="Decompressed! Copy file to clipboard. Open it in reader.")
               
                else:
                    self.status_label.config(text="Save cancelled")

            except Exception as e:
                self.status_label.config(text=f"Error: {e}")

            finally:
                self.progress.stop()

      # ------------------ Clear All Fields ------------------ #
    def clear_all(self):
        self.file_path.set("")
        self.status_label.config(text="Cleared")
        self.progress.stop()
        self.root.clipboard_clear()
        self.root.update()

    #------------------------Open Reader----------------------#
    def open_reader(self):
        if not hasattr(self, 'output_file_path') or not os.path.exists(self.output_file_path):
            self.status_label.config(text="No file to read")
            return

        try:
            # Open readfile.py and pass the decompressed file as an argument
            subprocess.Popen(["VicReader1.exe", self.output_file_path])
            self.status_label.config(text="Opening reader...")

        except Exception as e:
            self.status_label.config(text=f"Error launching reader: {e}")

    #------------------------Clip Board-----------------------------#
    def copy_file_path(self):
        if hasattr(self, 'output_file_path') and os.path.exists(self.output_file_path):
            self.root.clipboard_clear()
            self.root.clipboard_append(self.output_file_path)
            self.root.update()
            self.status_label.config(text="Path copied to clipboard.")
        else:
            self.status_label.config(text="No valid file to copy.")

    # ------------------ Mock Download Function ------------------ #
    def mock_download(self):
            if not hasattr(self, 'output_file_path') or not os.path.exists(self.output_file_path):
                self.status_label.config(text="No file to download")
                return

            try:
                # Ask user to choose a folder
                folder = filedialog.askdirectory(title="Select download folder")
                if not folder:
                    self.status_label.config(text="Download cancelled")
                    return

                # Get the filename from the compressed file path
                filename = os.path.basename(self.output_file_path)
                destination_path = os.path.join(folder, filename)

                # Copy the file to the selected folder
                shutil.copy(self.output_file_path, destination_path)

                self.status_label.config(text=f"Downloaded to: {destination_path}")

            except Exception as e:
                self.status_label.config(text=f"Error: {e}")



# ------------------ Run the App ------------------ #
if __name__ == "__main__":
    root = tk.Tk()
    app = VictorCompressApp(root)
    root.mainloop()
