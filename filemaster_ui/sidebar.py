import tkinter as tk

from filemaster_ui.theme import *

# =====================================================
# SIDEBAR
# =====================================================

class Sidebar:

    def __init__(self, parent):

        self.frame = tk.Frame(
            parent,
            bg=SIDEBAR_COLOR,
            width=240
        )

        self.frame.pack(
            side="left",
            fill="y"
        )

        self.frame.pack_propagate(False)

        # =============================================
        # TITLE
        # =============================================

        title = tk.Label(
            self.frame,
            text="FileMaster",
            bg=SIDEBAR_COLOR,
            fg=TEXT_COLOR,
            font=TITLE_FONT
        )

        title.pack(pady=20)

        # =============================================
        # QUICK ACCESS TITLE
        # =============================================

        quick_title = tk.Label(
            self.frame,
            text="Quick Access",
            bg=SIDEBAR_COLOR,
            fg=TEXT_COLOR,
            font=("Segoe UI", 11, "bold")
        )

        quick_title.pack(
            anchor="w",
            padx=15,
            pady=(10, 5)
        )

        # =============================================
        # QUICK ACCESS FRAME
        # =============================================

        self.quick_frame = tk.Frame(
            self.frame,
            bg=SIDEBAR_COLOR
        )

        self.quick_frame.pack(
            fill="x"
        )

        # =============================================
        # DRIVES TITLE
        # =============================================

        drive_title = tk.Label(
            self.frame,
            text="Drives",
            bg=SIDEBAR_COLOR,
            fg=TEXT_COLOR,
            font=("Segoe UI", 11, "bold")
        )

        drive_title.pack(
            anchor="w",
            padx=15,
            pady=(20, 5)
        )

        # =============================================
        # DRIVES FRAME
        # =============================================

        self.drive_frame = tk.Frame(
            self.frame,
            bg=SIDEBAR_COLOR
        )

        self.drive_frame.pack(
            fill="x"
        )



    # =================================================
    # CREATE NAV BUTTON
    # =====================================================

    def create_nav_button(
        self,
        parent,
        text,
        command
    ):

        btn = tk.Button(
            parent,
            text=text,
            bg=SIDEBAR_COLOR,
            fg=TEXT_COLOR,
            activebackground=BUTTON_HOVER,
            relief="flat",
            anchor="w",
            cursor="hand2",
            font=("Segoe UI", 10),
            command=command
        )

        btn.pack(
            fill="x",
            padx=15,
            pady=2
        )

        return btn