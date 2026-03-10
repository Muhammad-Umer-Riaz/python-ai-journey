# Chapter 12: Designing and Deploying Command Line Programs

Programs created while working through *Automate the Boring Stuff with Python* (3rd Edition). This chapter covers designing and deploying Python scripts as real CLI tools.

---

## Programs

### 🌨️ Snowstorm Animation
A terminal-based snowstorm animation using Unicode block characters. Loops continuously, clearing and redrawing the screen to simulate falling snow. Snow density can be controlled via a command-line argument (default is 4%).

```bash
python "Snowstorm - A simple snowstorm animation.py"        # Default density (4%)
python "Snowstorm - A simple snowstorm animation.py" 8      # Custom density
```

---

### 📇 Extract Contact Information from Large Documents
Reads text from the clipboard and scans it for Finnish phone numbers and email addresses using regular expressions. Supports international format (`+358...`), mobile numbers (`040...`, `050...`), and other local formats. Any matches found are copied back to the clipboard and printed to the terminal.

```bash
# Copy text to clipboard first, then run:
python "Extract Contact Information from Large Documents.py"
```

---

### 🎮 Guess the Number with PyMsgBox
A GUI version of the classic Guess the Number game from Chapter 3. The program picks a random number between 1 and 20 and gives the player 6 attempts to guess it. All interaction happens through native dialog boxes via PyMsgBox — no terminal input or output.

```bash
python "Guess the Number with PyMsgBox.py"
```

---

### ⏱️ Timer with PyMsgBox
A simple countdown timer that asks the user how many seconds to wait via a PyMsgBox prompt, pauses silently in the background, then displays a "Time's up!" alert when the countdown finishes. No terminal output at all.

```bash
python "Timer with PyMsgBox.py"
```

---

### 📦 Compiled Executables (`/dist`)
Standalone `.exe` versions of the Timer and Guess the Number programs, compiled with PyInstaller using the `--onefile` flag. These can be run on any Windows machine without Python installed.

```bash
pyinstaller --onefile "Guess the Number with PyMsgBox.py"
pyinstaller --onefile "Timer with PyMsgBox.py"
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