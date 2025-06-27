# 🗜️ VictorCompress

**Lighten Your Load — Compress, Decompress, and Explore Files with Ease**

VictorCompress is a modern, user-friendly Python desktop app that allows you to compress and decompress `.txt` files using `zlib` and Base64. Designed with a beautiful dark theme using `ttkbootstrap`, it features intuitive clipboard integration, file browsing, and a custom file reader.

---

## 📸 How It Looks

![image](https://github.com/user-attachments/assets/05d1d282-3241-4b53-94f2-1c8554f5cb34)

## the VicReader
![image](https://github.com/user-attachments/assets/0c8005f0-e21d-4220-bcc5-c44f2c4541db)
---

## ✨ Features

- 📂 Browse and select text files
- 🗜️ Compress and decompress via zlib + Base64
- 📋 Copy file paths to clipboard
- 📖 Open decompressed files in a custom reader (`readfile.py` or `vic_file_reader.py`)
- 🌑 Dark-themed UI with `ttkbootstrap`
- ✅ Progress bar and robust error handling

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Vic-Godwin/VictorCompress.git
cd VictorCompress
```

### 2. Install Required Dependencies

```bash
pip install -r requirements.txt
```

> If you don't have a `requirements.txt` yet, here's what to include:

```
ttkbootstrap>=1.10.1
pyperclip>=1.8.2(optional). I used built in clipboard
```

### 3. Run the App

```bash
python VictorCompress.py
```

---

## 📁 Project Structure

```
VictorCompress/
├── VictorCompress.py         # Main GUI app
├── compress_module.py        # Compression/decompression logic
├── vic_file_reader.py               # Original file reader module
├── VicReader.py        # Alternate or enhanced file reader
├── victor_logo_64x64.png     # App logo image
├── victor_logo_64x64.ico     # App window icon
├── .gitignore                # Files ignored by Git
|--- About Reader.me
├── LICENSE                   # MIT License
└── README.md                 # Project documentation
```

---

## 🧪 How It Works

### 🔹 Compression
```python
compressed = base64.b64encode(zlib.compress(data.encode('utf-8'), 9))
```

### 🔹 Decompression
```python
original = zlib.decompress(base64.b64decode(encoded_data)).decode('utf-8')
```

> Compressed files are saved in `.txt` format using Base64 encoding. Decompressed files restore the original plain text.

---

## 🔑 Usage Flow

1. **Browse** to select a `.txt` file.
2. **Click Compress** to reduce its size.
3. **Click Decompress** to restore a compressed file.
4. **Copy Path** with 📋 button (clipboard integration).
5. **Open Reader** to view decompressed content (via `readfile.py` or `vic_file_reader.py`).

---

## 📦 Dependencies

- `ttkbootstrap` >= 1.10.1
- `pyperclip` >= 1.8.2 *(optional if using `clipboard_append()`)*
- `tkinter`, `os`, `shutil`, `zlib`, and `base64` *(built-in)*

Install everything via:
```bash
pip install -r requirements.txt
```

---

## 📘 .gitignore

```
__pycache__/
*.pyc
*.pyo
*.log
.DS_Store
*.bak
*.swp
env/
venv/
```

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). See the LICENSE file for full details.

---

## 🙌 Author

**Victor Godwin**  
🎯 Passionate about clean interfaces, smart compression, and intuitive file utilities.  
📬 GitHub: [Vic-Godwin](https://github.com/Vic-Godwin)

---

## 🌟 Support This Project

If you find VictorCompress helpful:

- ⭐ Star the repo
- 🍴 Fork and contribute
- 🔁 Share with others

```bash
git clone https://github.com/Vic-Godwin/VictorCompress.git
```

---

## 🙌 About the Author

**Victor Godwin**  
🛠️ Developer | 📚 Teacher | 💡 Innovator  
Passionate about user-friendly tools that solve real-world problems.

🌍 Portfolio: [https://vic-godwin.github.io/victorgodwinchinonso/](https://vic-godwin.github.io/victorgodwinchinonso/)
