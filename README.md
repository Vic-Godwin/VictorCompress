# VictorCompress
A modern Python app for compressing and decompressing .txt files using zlib and Base64 — features dark mode, clipboard tools, and a built-in file reader.

# 🗜️ VictorCompress

**Lighten Your Load — Compress, Decompress, and Explore Files with Ease**

VictorCompress is a modern, user-friendly Python desktop app that allows you to compress and decompress `.txt` files using `zlib` and Base64. Designed with a beautiful dark theme using `ttkbootstrap`, it features intuitive clipboard integration, file browsing, and a custom file reader.

---

## 📸 Screenshot

![image](https://github.com/user-attachments/assets/05d1d282-3241-4b53-94f2-1c8554f5cb34)


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


### 🧪 How It Works
## 🔹 Compression
```python```

```compressed = base64.b64encode(zlib.compress(data.encode('utf-8'), 9))```

## 🔹 Decompression
```python
original = zlib.decompress(base64.b64decode(encoded_data)).decode('utf-8')```


