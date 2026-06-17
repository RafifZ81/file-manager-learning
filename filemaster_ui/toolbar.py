import tkinter as tk


class Toolbar:

    def __init__(self, parent):

        # ============================================
        # MAIN FRAME
        # ============================================

        self.frame = tk.Frame(
            parent,
            bg="#252526",
            height=45
        )

        self.frame.pack(fill="x")
        self.frame.pack_propagate(False)

        # ============================================
        # LEFT SIDE
        # ============================================

        self.left_frame = tk.Frame(
            self.frame,
            bg="#252526"
        )

        self.left_frame.pack(
            side="left",
            padx=10
        )

        # ============================================
        # BACK BUTTON
        # ============================================

        self.back_button = tk.Button(

            self.left_frame,

            text="⬅",

            bg="#2d2d30",

            fg="white",

            activebackground="#3a3d41",

            activeforeground="white",

            relief="flat",

            font=("Segoe UI", 10),

            cursor="hand2",

            width=3
        )

        self.back_button.pack(
            side="left",
            padx=(0, 2),
            pady=6
        )

        # ============================================
        # FORWARD BUTTON
        # ============================================

        self.forward_button = tk.Button(

            self.left_frame,

            text="➡",

            bg="#2d2d30",

            fg="white",

            activebackground="#3a3d41",

            activeforeground="white",

            relief="flat",

            font=("Segoe UI", 10),

            cursor="hand2",

            width=3
        )

        self.forward_button.pack(
            side="left",
            padx=2
        )

        # ============================================
        # UP BUTTON
        # ============================================

        self.up_button = tk.Button(

            self.left_frame,

            text="⬆",

            bg="#2d2d30",

            fg="white",

            activebackground="#3a3d41",

            activeforeground="white",

            relief="flat",

            font=("Segoe UI", 10),

            cursor="hand2",

            width=3
        )

        self.up_button.pack(
            side="left",
            padx=(2, 10)
        )

        # ============================================
        # OPEN BUTTON
        # ============================================

        self.open_button = tk.Button(

            self.left_frame,

            text="📂 Open",

            bg="#2d2d30",

            fg="white",

            activebackground="#3a3d41",

            activeforeground="white",

            relief="flat",

            font=("Segoe UI", 10),

            cursor="hand2"
        )

        self.open_button.pack(
            side="left",
            padx=5,
            pady=6
        )

        # ============================================
        # REFRESH BUTTON
        # ============================================

        self.refresh_button = tk.Button(

            self.left_frame,

            text="⟳ Refresh",

            bg="#2d2d30",

            fg="white",

            activebackground="#3a3d41",

            activeforeground="white",

            relief="flat",

            font=("Segoe UI", 10),

            cursor="hand2"
        )

        self.refresh_button.pack(
            side="left",
            padx=5
        )

        # ============================================
        # ORGANIZE BUTTON
        # ============================================

        self.organize_button = tk.Button(

            self.left_frame,

            text="🗂 Organize",

            bg="#2d2d30",

            fg="white",

            activebackground="#3a3d41",

            activeforeground="white",

            relief="flat",

            font=("Segoe UI", 10),

            cursor="hand2"
        )

        self.organize_button.pack(
            side="left",
            padx=(5, 12)
        )

        # ============================================
        # SORT LABEL
        # ============================================

        self.sort_label = tk.Label(

            self.left_frame,

            text="Sort:",

            bg="#252526",

            fg="#cccccc",

            font=("Segoe UI", 10)
        )

        self.sort_label.pack(
            side="left",
            padx=(0, 5)
        )

        # ============================================
        # SORT BY NAME
        # ============================================

        self.name_sort = tk.Button(

            self.left_frame,

            text="Name",

            bg="#2d2d30",

            fg="white",

            relief="flat",

            font=("Segoe UI", 9),

            cursor="hand2"
        )

        self.name_sort.pack(
            side="left",
            padx=3
        )

        # ============================================
        # SORT BY DATE
        # ============================================

        self.date_sort = tk.Button(

            self.left_frame,

            text="Date",

            bg="#2d2d30",

            fg="white",

            relief="flat",

            font=("Segoe UI", 9),

            cursor="hand2"
        )

        self.date_sort.pack(
            side="left",
            padx=3
        )

        # ============================================
        # SORT BY TYPE
        # ============================================

        self.type_sort = tk.Button(

            self.left_frame,

            text="Type",

            bg="#2d2d30",

            fg="white",

            relief="flat",

            font=("Segoe UI", 9),

            cursor="hand2"
        )

        self.type_sort.pack(
            side="left",
            padx=3
        )

        # ============================================
        # RIGHT SIDE
        # ============================================

        self.right_frame = tk.Frame(
            self.frame,
            bg="#252526"
        )

        self.right_frame.pack(
            side="right",
            padx=10
        )

        self.view_label = tk.Label(

            self.right_frame,

            text="Explorer View",

            bg="#252526",

            fg="#888888",

            font=("Segoe UI", 9)
        )

        self.view_label.pack(
            side="right"
        )