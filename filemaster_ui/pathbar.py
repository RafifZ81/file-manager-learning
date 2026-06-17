import tkinter as tk


class PathBar:

    def __init__(self, parent):

        # =============================================
        # VARIABLES
        # =============================================

        self.path_var = tk.StringVar()

        # =============================================
        # FRAME
        # =============================================

        self.frame = tk.Frame(
            parent,
            bg="#252526"
        )

        self.frame.pack(
            fill="x",
            padx=10,
            pady=(10, 5)
        )

        # =============================================
        # PATH ENTRY
        # =============================================

        self.path_entry = tk.Entry(

            self.frame,

            textvariable=self.path_var,

            font=("Segoe UI", 10),

            bg="#2d2d30",

            fg="white",

            insertbackground="white",

            relief="flat"
        )

        self.path_entry.pack(

            fill="x",

            expand=True,

            ipady=6
        )

    # =================================================
    # SET PATH
    # =================================================

    def set_path(self, path):

        self.path_var.set(path)

    # =================================================
    # GET PATH
    # =================================================

    def get_path(self):

        return self.path_var.get()

    # =================================================
    # BIND ENTER
    # =================================================

    def bind_enter(self, callback):

        self.path_entry.bind(
            "<Return>",
            callback
        )