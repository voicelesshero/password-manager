import threading
from tkinter import simpledialog, messagebox

TIMEOUT_MINUTES = 10
TIMEOUT_SECONDS = TIMEOUT_MINUTES * 60


class SessionManager:
    def __init__(self, window, verify_func):
        self.window = window
        self.verify_func = verify_func  # function that verifies master password
        self.timer = None
        self.locked = False
        self._start_timer()
        self._bind_activity()

    def _bind_activity(self):
        # reset timer on any mouse or keyboard activity
        self.window.bind_all("<Motion>", self._reset_timer)
        self.window.bind_all("<KeyPress>", self._reset_timer)
        self.window.bind_all("<ButtonPress>", self._reset_timer)

    def _start_timer(self):
        self.timer = threading.Timer(TIMEOUT_SECONDS, self._lock)
        self.timer.daemon = True
        self.timer.start()

    def _reset_timer(self, event=None):
        if self.locked:
            return
        if self.timer:
            self.timer.cancel()
        self._start_timer()

    def _lock(self):
        self.locked = True
        self.window.after(0, self._show_lock)

    def _show_lock(self):
        self.window.withdraw()

        entered = simpledialog.askstring(
            "Session Locked",
            "Session timed out. Enter master password to unlock:",
            show="*"
        )

        if entered is None:
            self.window.destroy()
            return

        if self.verify_func(entered):
            self.locked = False
            self.window.deiconify()
            self._start_timer()
        else:
            messagebox.showerror("Access Denied", "Incorrect master password.")
            self.window.destroy()