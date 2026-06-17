import tkinter as tk


class StatusBar:

    def __init__(self, parent):

        # ============================================
        # MAIN FRAME
        # ============================================

        self.frame = tk.Frame(
            parent,
            bg="#252526",
            height=28
        )

        self.frame.pack(
            side="bottom",
            fill="x"
        )

        # ============================================
        # LEFT STATUS
        # ============================================

        self.left_label = tk.Label(

            self.frame,

            text="Ready",

            bg="#252526",

            fg="#cccccc",

            font=("Segoe UI", 9),

            anchor="w"
        )

        self.left_label.pack(
            side="left",
            padx=10
        )

        # ============================================
        # RIGHT STATUS
        # ============================================

        self.right_label = tk.Label(

            self.frame,

            text="0 items",

            bg="#252526",

            fg="#cccccc",

            font=("Segoe UI", 9),

            anchor="e"
        )

        self.right_label.pack(
            side="right",
            padx=10
        )

    # ================================================
    # SET LEFT TEXT
    # ================================================

    def set_left(self, text):

        self.left_label.config(
            text=text
        )

    # ================================================
    # SET RIGHT TEXT
    # ================================================

    def set_right(self, text):

        self.right_label.config(
            text=text
        )