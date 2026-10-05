# ============================================================
#   Rule-Based Chatbot — CodeAlpha Internship Project
#   GUI Version using Tkinter (Python Standard Library)
#   Author : Siraj
#   Date   : October 2026
#   Python : 3.x  |  No external libraries required
# ============================================================

import datetime                        # for live date & time
import tkinter as tk                   # GUI toolkit (stdlib)
from tkinter import scrolledtext       # auto-scrolling text widget


# ════════════════════════════════════════════════════════════
#  SECTION 1 — RESPONSE ENGINE  (pure logic, no GUI code)
# ════════════════════════════════════════════════════════════

def get_current_time():
    """Return a formatted date-and-time string."""
    now = datetime.datetime.now()
    return (
        "Right now it is "
        + now.strftime("%A, %d %B %Y")
        + " at "
        + now.strftime("%I:%M %p") + "."
    )


def get_response(user_input):
    """
    Match user_input against keyword groups and return a reply string.
    Returns the special sentinel 'EXIT' for bye/quit commands.
    """
    msg = user_input.lower().strip()   # normalise: lowercase + trim spaces

    # ── Greeting ──────────────────────────────────────────
    if any(w in msg for w in ("hello", "hi", "hey", "howdy", "hiya",
                               "greetings")):
        return "Hello there! 👋 Great to meet you. How can I help you today?"

    # ── Wellbeing ─────────────────────────────────────────
    elif any(p in msg for p in ("how are you", "how are you doing",
                                 "how do you do", "how's it going",
                                 "what's up", "whats up")):
        return ("I'm doing fantastic, thanks for asking! 😊 "
                "I'm just a bot, but every chat makes my day. How about you?")

    # ── Identity ──────────────────────────────────────────
    elif any(p in msg for p in ("your name", "who are you", "what are you")):
        return ("My name is CodeBot 🤖 — your friendly Python assistant! "
                "Built with pure Python and lots of enthusiasm.")

    # ── Help menu ─────────────────────────────────────────
    elif any(w in msg for w in ("help", "assist", "commands",
                                 "what can you do")):
        return (
            "Here is what you can ask me:\n\n"
            "  • hello / hi          — say hello\n"
            "  • how are you         — check my mood\n"
            "  • what is your name   — learn who I am\n"
            "  • help                — show this menu\n"
            "  • thanks / thank you  — show some love\n"
            "  • joke                — hear a quick joke\n"
            "  • time                — get the current date & time\n"
            "  • bye / exit          — end the conversation"
        )

    # ── Gratitude ─────────────────────────────────────────
    elif any(w in msg for w in ("thanks", "thank you", "thank u",
                                 "thx", "ty", "cheers")):
        return "You're very welcome! 😄 Happy to help anytime."

    # ── Joke ──────────────────────────────────────────────
    elif any(w in msg for w in ("joke", "funny", "laugh", "humour")):
        return "Why do programmers prefer dark mode? 😄\nBecause light attracts bugs!"

    # ── Date / time ───────────────────────────────────────
    elif any(w in msg for w in ("time", "date", "today")):
        return "🕐 " + get_current_time()

    # ── Exit ──────────────────────────────────────────────
    elif any(w in msg for w in ("bye", "goodbye", "exit", "quit",
                                 "see you", "cya")):
        return "EXIT"   # sentinel — GUI will intercept this

    # ── Unknown ───────────────────────────────────────────
    else:
        return ("Hmm, I'm not sure I understand that. 🤔 "
                "Type 'help' to see what I can do!")


# ════════════════════════════════════════════════════════════
#  SECTION 2 — COLOUR PALETTE  (centralised for easy tweaking)
# ════════════════════════════════════════════════════════════

# Dark theme colours
BG_DARK       = "#0f0f1a"   # window / outer background
BG_CHAT       = "#1a1a2e"   # chat area background
BG_INPUT      = "#16213e"   # input bar background
BG_ENTRY      = "#0f3460"   # text-entry field background
ACCENT        = "#e94560"   # primary accent (red-pink)
ACCENT2       = "#533483"   # secondary accent (purple)
BOT_BUBBLE    = "#1e2a45"   # bot message bubble colour
USER_BUBBLE   = "#2d1b4e"   # user message bubble colour
TEXT_PRIMARY  = "#e0e0f0"   # main text colour
TEXT_MUTED    = "#8888aa"   # muted / label text colour
TEXT_BOT      = "#a8d8ea"   # bot text colour (light blue)
TEXT_USER     = "#f8c8d4"   # user text colour (light pink)
TEXT_TIME     = "#666688"   # timestamp colour
BTN_HOVER     = "#c73652"   # send button hover colour
SCROLLBAR_BG  = "#1a1a2e"   # scrollbar background


# ════════════════════════════════════════════════════════════
#  SECTION 3 — ChatbotApp CLASS  (all GUI code lives here)
# ════════════════════════════════════════════════════════════

class ChatbotApp:
    """
    Main GUI application class.
    Builds the window, lays out all widgets, and wires up events.
    """

    def __init__(self, root):
        """
        Constructor — receives the Tk root window and builds everything.

        Parameters
        ----------
        root : tk.Tk  — the top-level Tkinter window
        """
        self.root = root
        self._configure_window()      # window title, size, icon colour
        self._build_header()          # top banner
        self._build_input_bar()       # ← MUST be packed before chat area
        self._build_chat_area()       # fills all remaining space
        self._bind_keys()             # keyboard shortcuts
        self._show_welcome()          # initial greeting message

    # ── Window setup ──────────────────────────────────────
    def _configure_window(self):
        """Set window title, size, minimum size, and background."""
        self.root.title("CodeBot — CodeAlpha Internship")
        self.root.geometry("700x600")
        self.root.minsize(500, 450)
        self.root.configure(bg=BG_DARK)
        # Centre the window on the screen
        self.root.update_idletasks()
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        x = (self.root.winfo_screenwidth()  - w) // 2
        y = (self.root.winfo_screenheight() - h) // 2
        self.root.geometry(f"{w}x{h}+{x}+{y}")

    # ── Header banner ─────────────────────────────────────
    def _build_header(self):
        """Create the top gradient-style header with title and subtitle."""
        header_frame = tk.Frame(self.root, bg=ACCENT2, height=70)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        header_frame.pack_propagate(False)   # keep fixed height

        # Avatar circle label
        avatar = tk.Label(
            header_frame, text="🤖",
            font=("Segoe UI Emoji", 22),
            bg=ACCENT2, fg=TEXT_PRIMARY
        )
        avatar.pack(side=tk.LEFT, padx=(18, 6), pady=10)

        # Title + subtitle stack
        title_stack = tk.Frame(header_frame, bg=ACCENT2)
        title_stack.pack(side=tk.LEFT, pady=10)

        tk.Label(
            title_stack, text="CodeBot",
            font=("Segoe UI", 16, "bold"),
            bg=ACCENT2, fg=TEXT_PRIMARY
        ).pack(anchor=tk.W)

        tk.Label(
            title_stack, text="CodeAlpha Internship  •  Python Rule-Based AI",
            font=("Segoe UI", 8),
            bg=ACCENT2, fg=TEXT_MUTED
        ).pack(anchor=tk.W)

        # Online status badge (right-aligned)
        tk.Label(
            header_frame, text="● Online",
            font=("Segoe UI", 9),
            bg=ACCENT2, fg="#44ff88"
        ).pack(side=tk.RIGHT, padx=18)

    # ── Chat display area ─────────────────────────────────
    def _build_chat_area(self):
        """
        Build the main chat display using a Text widget.
        We use a Text widget (not a Label) so we can colour
        individual lines differently.
        """
        # Outer frame that holds the Text widget + scrollbar
        chat_frame = tk.Frame(self.root, bg=BG_CHAT)
        chat_frame.pack(fill=tk.BOTH, expand=True,
                        padx=10, pady=(8, 0))

        # Scrollbar
        scrollbar = tk.Scrollbar(chat_frame, bg=SCROLLBAR_BG,
                                  troughcolor=BG_CHAT,
                                  activebackground=ACCENT)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Main text display widget
        self.chat_display = tk.Text(
            chat_frame,
            bg=BG_CHAT,
            fg=TEXT_PRIMARY,
            font=("Segoe UI", 11),
            wrap=tk.WORD,              # word-wrap long lines
            state=tk.DISABLED,         # read-only — we insert via code
            cursor="arrow",            # no text cursor visible
            selectbackground=ACCENT2,
            borderwidth=0,
            padx=12,
            pady=10,
            yscrollcommand=scrollbar.set
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.chat_display.yview)

        # Define named text tags for coloured/styled segments
        self.chat_display.tag_configure(
            "bot_name",
            foreground=ACCENT, font=("Segoe UI", 10, "bold"))
        self.chat_display.tag_configure(
            "bot_text",
            foreground=TEXT_BOT, font=("Segoe UI", 11),
            lmargin1=20, lmargin2=20)
        self.chat_display.tag_configure(
            "user_name",
            foreground=ACCENT2, font=("Segoe UI", 10, "bold"),
            justify=tk.RIGHT)
        self.chat_display.tag_configure(
            "user_text",
            foreground=TEXT_USER, font=("Segoe UI", 11),
            justify=tk.RIGHT, lmargin1=20, lmargin2=20)
        self.chat_display.tag_configure(
            "timestamp",
            foreground=TEXT_TIME, font=("Segoe UI", 8),
            justify=tk.RIGHT)
        self.chat_display.tag_configure(
            "divider",
            foreground=BG_DARK)
        self.chat_display.tag_configure(
            "welcome",
            foreground=TEXT_MUTED, font=("Segoe UI", 10, "italic"),
            justify=tk.CENTER)

    # ── Input bar ─────────────────────────────────────────
    def _build_input_bar(self):
        """Create the bottom input area: hint label, entry field, send button."""
        # Outer bar frame — side=BOTTOM pins it to the bottom;
        # must be packed BEFORE the expanding chat area (Tkinter rule).
        bar_frame = tk.Frame(self.root, bg=BG_INPUT, height=70)
        bar_frame.pack(fill=tk.X, side=tk.BOTTOM, padx=10, pady=(0, 8))
        bar_frame.pack_propagate(False)  # keep fixed height

        # Inner padding frame
        inner = tk.Frame(bar_frame, bg=BG_INPUT)
        inner.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)

        # Prompt prefix icon/label
        prompt_icon = tk.Label(
            inner,
            text="💬",
            font=("Segoe UI Emoji", 14),
            bg=BG_INPUT,
            fg=TEXT_MUTED
        )
        prompt_icon.pack(side=tk.LEFT, padx=(4, 8))

        # Text entry field
        self.user_entry = tk.Entry(
            inner,
            font=("Segoe UI", 12),
            bg=BG_ENTRY,
            fg=TEXT_PRIMARY,
            insertbackground=ACCENT,       # cursor colour
            relief=tk.FLAT,
            borderwidth=0
        )
        self.user_entry.pack(side=tk.LEFT, fill=tk.BOTH,
                              expand=True, ipady=8, padx=(0, 10))

        # Send button
        self.send_btn = tk.Button(
            inner,
            text="Send  ➤",
            font=("Segoe UI", 11, "bold"),
            bg=ACCENT,
            fg="white",
            activebackground=BTN_HOVER,
            activeforeground="white",
            relief=tk.FLAT,
            cursor="hand2",              # pointer cursor on hover
            padx=16,
            pady=6,
            command=self._on_send        # click handler
        )
        self.send_btn.pack(side=tk.RIGHT)

        # Hover effect for send button
        self.send_btn.bind("<Enter>",
            lambda e: self.send_btn.config(bg=BTN_HOVER))
        self.send_btn.bind("<Leave>",
            lambda e: self.send_btn.config(bg=ACCENT))

    # ── Key bindings ──────────────────────────────────────
    def _bind_keys(self):
        """Wire up keyboard events."""
        # Enter key sends the message
        self.root.bind("<Return>", lambda e: self._on_send())
        # Automatically focus the entry box on launch
        self.user_entry.focus_set()

    # ── Welcome message ───────────────────────────────────
    def _show_welcome(self):
        """Display an introductory message when the app first opens."""
        self._insert_text(
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n",
            "welcome"
        )
        self._insert_text(
            "  Welcome! I'm CodeBot 🤖\n"
            "  Type 'help' to see what I can do.\n"
            "  Type 'bye' or 'exit' to close the chat.\n",
            "welcome"
        )
        self._insert_text(
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n",
            "welcome"
        )

    # ── Core send handler ─────────────────────────────────
    def _on_send(self):
        """Called when the user clicks Send or presses Enter."""
        # Read and validate the entry field
        raw = self.user_entry.get().strip()
        if not raw:
            return   # ignore empty sends

        # Clear the input field immediately and keep focus active
        self.user_entry.delete(0, tk.END)
        self.user_entry.focus_set()

        # Display the user's message in the chat window
        self._display_user_message(raw)

        # Get the bot's response
        response = get_response(raw)

        if response == "EXIT":
            # Show goodbye then close the window after a short delay
            self._display_bot_message(
                "Goodbye! It was great chatting with you. 👋\n"
                "The window will close in 2 seconds..."
            )
            self.root.after(2000, self.root.destroy)
        else:
            self._display_bot_message(response)

    # ── Message display helpers ───────────────────────────
    def _display_user_message(self, text):
        """Append a right-aligned user bubble to the chat display."""
        ts = datetime.datetime.now().strftime("%I:%M %p")
        self._insert_text("You\n",          "user_name")
        self._insert_text(text + "\n",      "user_text")
        self._insert_text(ts + "\n\n",      "timestamp")

    def _display_bot_message(self, text):
        """Append a left-aligned bot bubble to the chat display."""
        ts = datetime.datetime.now().strftime("%I:%M %p")
        self._insert_text("CodeBot\n",      "bot_name")
        self._insert_text(text + "\n",      "bot_text")
        self._insert_text(ts + "\n\n",      "timestamp")

    def _insert_text(self, text, tag):
        """
        Insert styled text into the (normally read-only) chat widget.

        We temporarily enable the widget, insert text with the given
        colour/style tag, then make it read-only again.
        """
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, text, tag)
        self.chat_display.config(state=tk.DISABLED)
        # Auto-scroll to the latest message
        self.chat_display.see(tk.END)


# ════════════════════════════════════════════════════════════
#  SECTION 4 — ENTRY POINT
# ════════════════════════════════════════════════════════════

if __name__ == "__main__":
    root = tk.Tk()              # create the top-level window
    app  = ChatbotApp(root)     # build and wire up all widgets
    root.mainloop()             # hand control to the Tkinter event loop
