import tkinter as tk


class SearchBar:

    def __init__(self, parent):

        # =============================================
        # VARIABLES
        # =============================================

        self.search_var = tk.StringVar()

        # =============================================
        # FRAME
        # =============================================

        self.frame = tk.Frame(
            parent,
            bg="#252526"
        )

        # =============================================
        # SEARCH ENTRY
        # =============================================

        self.search_entry = tk.Entry(

            self.frame,

            textvariable=self.search_var,

            width=25,

            font=("Segoe UI", 10),

            bg="#2d2d30",

            fg="white",

            insertbackground="white",

            relief="flat"
        )

        self.search_entry.pack(
            fill="x",
            expand=True,
            ipady=6
        )

    # =================================================
    # GET TEXT
    # =================================================

    def get_text(self):

        return self.search_var.get()

    # =================================================
    # SET TEXT
    # =================================================

    def set_text(self, text):

        self.search_var.set(text)

    # =================================================
    # CLEAR
    # =================================================

    def clear(self):

        self.search_var.set("")

    # =================================================
    # BIND KEY RELEASE
    # =================================================

    def bind_keyrelease(self, callback):

        self.search_entry.bind(
            "<KeyRelease>",
            callback
        )

    # =================================================
    # FOCUS
    # =================================================

    def focus(self):

        self.search_entry.focus_set()