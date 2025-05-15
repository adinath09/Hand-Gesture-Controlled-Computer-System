



## Hand Gesture Controlled Computer System

This project implements a computer control system using real-time hand gesture recognition. It uses a webcam to detect hand gestures and maps them to specific system control commands like opening applications, controlling volume, or navigating the system.

---

### 📁 Project Structure

```
project/
├── compute_operate/
│   ├── app/
│   │   ├── mainapp.py
│   │   ├── static 
│   │   └── Templates
│   └── raw/
│       ├── dataset/
│       └── config/
└── README.md
    Requirement.txt        
```

### 🚀 Features

* Real-time hand tracking using webcam
* Map gestures to system operations
* User-configurable gestures and actions
* Lightweight and fast processing
* Extendable for new gestures and commands

---

### 🛠️ Technologies Used

* Python
* OpenCV
* Mediapipe
* PyAutoGUI (for controlling the system)
* NumPy
* OS/System libraries

---

### 📦 Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/adinath09/Hand-Gesture-Controlled-Computer-System.git
cd Hand-Gesture-Controlled-Computer-System
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```


4. **Run the application:**

```bash
python compute_operate/app/main.py
```

---

### ✋ Supported Gestures (Examples)

| Gesture        | Action            |
| -------------- | ----------------- |
| Open Palm      | Open Notepad      |
| Thumbs Up      | Volume Up         |
| Thumbs Down    | Volume Down       |


### 🤝 Contributing

Contributions are welcome! Please fork the repo and submit a pull request.

---

### 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

### 👨‍💻 Author

Adinath  Nage 


Feel free to connect on [GitHub](https://github.com/adinath09)

---

