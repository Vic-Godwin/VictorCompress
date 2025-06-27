
# VictorCompress
A modern Python app for compressing and decompressing .txt files using zlib and Base64 — features dark mode, clipboard tools, and a built-in file reader.

# 🗜️ VictorCompress

**Lighten Your Load — Compress, Decompress, and Explore Files with Ease**

VictorCompress is a modern, user-friendly Python desktop app that allows you to compress and decompress `.txt` files using `zlib` and Base64. Designed with a beautiful dark theme using `ttkbootstrap`, it features intuitive clipboard integration, file browsing, and a custom file reader.

---

## 📸 how it looks

![image](https://github.com/user-attachments/assets/05d1d282-3241-4b53-94f2-1c8554f5cb34)
## the VicReader
![image](https://github.com/user-attachments/assets/0c8005f0-e21d-4220-bcc5-c44f2c4541db)


## ✨ Features

- 📂 Browse and select text files
- 🗜️ Compress and decompress via zlib + Base64
- 📋 Copy file paths to clipboard
- 📖 Open decompressed files in a custom reader (`readfile.py`)
- 🌑 Dark-themed UI (ttkbootstrap)
- ✅ Progress bar and error handling

---

## 🚀 Getting Started

### 1. Clone the Repo

bash
git clone https://github.com/Vic-Godwin/VictorCompress.git
cd VictorCompress


## Install required dependencies:
```pip install -r requirements.txt```

## Run The App
```python main.py```



## 📁 Project Structure
VictorCompress/

├── main.py               # Main GUI app

├── compress_module.py    # Compression logic (zlib + base64)

├── readfile.py           # File reader launched from main app

├── assets/               # Logos/icons (optional)

│   └── victor_logo_64x64.png

├── docs/

│   └── user_guide.md     # Optional detailed guide

├── requirements.txt

├── .gitignore

├── LICENSE

└── README.md


# 🧪 How It Works
### 🔹 Compression
```python```

```compressed = base64.b64encode(zlib.compress(data.encode('utf-8'), 9))```

### 🔹 Decompression
```python```

```original = zlib.decompress(base64.b64decode(encoded_data)).decode('utf-8')```

#### Compressed file is saved in .txt format using Base64 encoding.

#### Decompressed output restores the original plain text.



# 🔑 Usage Flow
 **1.** **Browse** to select a .txt file.
 
 **2.** **Click Compress** to reduce its size.
 
 **3.** **Click Decompress** to **restore** a file.
 
 **4.** Use the **📋 Clipboard** button to copy file path.
 
 **5.** **Click Open Reader** to launch **readfile.py** and view file contents(though readfile.py isn't fully ready.



# 📦 Dependencies
#### List in requirements.txt:
```ttkbootstrap>=1.10.1```

```pyperclip>=1.8.2(optional). I used the built in clipbboard```

```pip install -r requirements.txt```




## 📝 .gitignore
```__pycache__/```

```*.pyc```

```*.pyo```

```*.log```

```.DS_Store```

```*.bak```

```*.swp```

```env/```

```venv/```



# 📘 License
#### This project is licensed under the MIT License.
#### See the [LICENSE](LICENSE) file for full details.



# 🙌 Author
### Victor Godwin
#### 🎯 Passionate about clean interfaces, smart compression, and intuitive file utilities.
#### 📬 GitHub: Vic-Godwin



# 🌟 Support This Project
If you find VictorCompress helpful, consider starring ⭐ the repo and sharing it.

```git clone https://github.com/Vic-Godwin/VictorCompress.git```

Feel free to fork, contribute, or improve!



# 🙌 About the Author
## Victor Godwin
### 🛠️ Developer | 📚 Teacher | 💡 Innovator

### Passionate about user-friendly tools that solve real-world problems.
## #This project is part of my professional developer portfolio.

📬 GitHub: https://github.com/Vic-Godwin

🌍 Portfolio: https://vic-godwin.github.io/victorgodwinchinonso/

