# CodeBot — Rule-Based AI Chatbot 🤖

A sleek, modern, desktop GUI chatbot built with **Python** and **Tkinter**. Developed as an internship project for **CodeAlpha**.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-blueviolet?style=for-the-badge)
![CodeAlpha](https://img.shields.io/badge/Internship-CodeAlpha-blue?style=for-the-badge)
![Dependencies](https://img.shields.io/badge/Dependencies-None%20(Standard%20Library)-success?style=for-the-badge)

---

## 📌 Project Overview

**CodeBot** is an interactive, rule-based chatbot designed to handle natural conversational flows using keyword detection and pattern matching. It features a custom **dark-mode cyberpunk-inspired interface** crafted entirely with Python's built-in `tkinter` library—meaning **no third-party dependencies or installations are required**.

---

## ✨ Features

- **🎨 Modern Dark-Theme GUI**:
  - Custom color scheme (`#0f0f1a` base, `#e94560` crimson accent, and `#533483` purple tone).
  - Styled message bubbles with distinct alignment:
    - **CodeBot**: Left-aligned with cyan text and bot avatar.
    - **User**: Right-aligned with pink text.
  - Formatted timestamps for every message.
  - Centered screen launch on startup.
- **⚡ Zero External Dependencies**:
  - Uses only Python standard library modules (`tkinter`, `datetime`).
  - Works out of the box on Windows, macOS, and Linux.
- **🧠 Rule-Based Response Engine**:
  - Handles greetings, wellbeing checks, identity, jokes, date/time queries, gratitude, and fallback responses.
  - Normalizes input (case-insensitive, trims excess whitespace).
- **⌨️ Intuitive User Experience**:
  - Press <kbd>Enter</kbd> or click the **Send ➤** button with dynamic hover effects.
  - Auto-scrolling chat history.
  - Dedicated welcome message on startup.
  - Graceful exit sequence: countdown and auto-closure when typing `bye` or `exit`.

---

## 💬 Supported Commands & Queries

CodeBot identifies keywords inside user prompts:

| Intent / Category | Sample Inputs | Bot Response / Action |
|---|---|---|
| **Greetings** | `hello`, `hi`, `hey`, `hiya`, `greetings` | Welcomes the user and asks how to help. |
| **Wellbeing** | `how are you`, `how's it going`, `what's up` | Responds with bot mood and friendly tone. |
| **Identity** | `who are you`, `what is your name` | Introduces CodeBot and project background. |
| **Help Menu** | `help`, `commands`, `what can you do` | Displays list of supported queries. |
| **Jokes** | `joke`, `tell me a joke`, `funny` | Delivers a programming-related joke. |
| **Live Time / Date**| `time`, `date`, `today` | Fetches system time and full date format. |
| **Gratitude** | `thanks`, `thank you`, `ty`, `cheers` | Acknowledges with a polite reply. |
| **Exit** | `bye`, `exit`, `quit`, `see you` | Initiates 2-second farewell and closes window. |
| **Fallback** | *(Any unrecognized input)* | Explains query wasn't understood & points to `help`. |

---

## 🚀 Getting Started

### Prerequisites

Ensure you have **Python 3.7+** installed on your system. Tkinter is included by default with standard Python installations on Windows and macOS.

> **Linux users (Ubuntu/Debian)**: If Tkinter is not pre-installed, install it via:
> ```bash
> sudo apt-get install python3-tk
> ```

### Running the Chatbot

1. Clone or download this repository to your local machine.
2. Open your terminal or command prompt in the project directory:
   ```bash
   cd Chatbot
   ```
3. Run the application:
   ```bash
   python chatbot.py
   ```

---

## 📁 Project Structure

```text
Chatbot/
├── chatbot.py        # Complete application source code (Engine + GUI)
└── README.md         # Project documentation
```

### Code Architecture in `chatbot.py`

- **Section 1: Response Engine (`get_response`, `get_current_time`)**:
  - Independent pure Python logic for text preprocessing, intent detection, and response generation.
- **Section 2: Colour Palette**:
  - Centralized color constants for fast and consistent theme adjustments.
- **Section 3: `ChatbotApp` Class**:
  - Tkinter GUI layout: header banner, status badge, message log with auto-scroll, text entry field, and event bindings.
- **Section 4: Entry Point**:
  - `tk.Tk()` initialization and event loop invocation (`mainloop()`).

---

## 🛠️ Customization

### Adding New Responses
You can easily expand CodeBot's vocabulary by adding new conditions to the `get_response()` function in [chatbot.py](file:///c:/Users/siraj/Desktop/Chatbot/chatbot.py):

```python
elif any(w in msg for w in ("weather", "forecast")):
    return "I cannot check the live weather yet, but it's always sunny in the terminal! ☀️"
```

### Changing the Theme
Modify the color variables in **Section 2** of [chatbot.py](file:///c:/Users/siraj/Desktop/Chatbot/chatbot.py#L93-L113) to create your own color scheme.

---

## 👨‍💻 Author

- **Author**: Siraj
- **Organization**: [CodeAlpha](https://www.codealpha.tech/) Internship Program
- **Date**: October 2026
