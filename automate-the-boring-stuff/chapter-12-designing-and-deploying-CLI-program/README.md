# Chapter 12: Designing and Deploying Command Line Programs

Programs created while working through *Automate the Boring Stuff with Python* (3rd Edition). This chapter covers designing and deploying Python scripts as real CLI tools.

---

## Programs

### 🌨️ Snowstorm Animation
A terminal-based snowstorm animation. Snow density can be controlled via a command-line argument.

```bash
python "Snowstorm - A simple snowstorm animation.py"        # Default density (4%)
python "Snowstorm - A simple snowstorm animation.py" 8      # Custom density
```

---

### 📇 Extract Contact Information from Large Documents *(Chapter 9)*
Scans large text documents and extracts email addresses and phone numbers using regular expressions.

```bash
python "Extract Contact Information from Large Documents.py" input.txt
```

---

### 📝 Add Bullets to Wiki Markup *(Chapter 8)*
Reads text from the clipboard, adds bullet points to each line, and copies the formatted result back to the clipboard.

```bash
python "Add Bullets to Wiki Markup.py"
```

---

### ♟️ Interactive Chessboard Simulator *(Chapter 7)*
A text-based chessboard that displays piece positions using Unicode characters.

```bash
python "Interactive Chessboard Simulator.py"
```

---

### 🎮 Guess the Number with PyMsgBox
Classic "Guess the Number" game using GUI dialog boxes via PyMsgBox instead of terminal input.

```bash
python "Guess the Number with PyMsgBox.py"
```

---

### ⏱️ Timer with PyMsgBox
A countdown timer that shows a GUI popup alert when time expires.

```bash
python "Timer with PyMsgBox.py" 60     # 60-second timer
python "Timer with PyMsgBox.py" 300    # 5-minute timer
```

---

### 📦 Compiled Executables (`/dist`)
Standalone `.exe` versions of the Timer and Guess the Number programs, compiled with PyInstaller. No Python installation required.

```bash
.\dist\timer.exe 60
.\dist\guess_the_number.exe
```

---

## Setup

```bash
# Activate the virtual environment
C:\Users\muham\Scripts\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

*Part of the [python-ai-journey](https://github.com/muham/python-ai-journey) repository.*
