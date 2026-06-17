import tkinter as tk
from tkinter import ttk


class FileTree:

    def __init__(self, parent):

        self.frame = tk.Frame(
            parent,
            bg="#1e1e1e"
        )

        self.frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 10)
        )

        self.scrollbar = ttk.Scrollbar(
            self.frame
        )

        self.scrollbar.pack(
            side="right",
            fill="y"
        )

        self.tree = ttk.Treeview(

            self.frame,

            columns=(
                "path",
                "type",
                "size",
                "modified"
            ),

            show="tree headings",

            yscrollcommand=self.scrollbar.set
        )

        self.scrollbar.config(
            command=self.tree.yview
        )

        style = ttk.Style()

        style.theme_use("default")

        style.configure(

            "Treeview",

            background="#1e1e1e",

            foreground="white",

            fieldbackground="#1e1e1e",

            rowheight=28,

            borderwidth=0,

            font=("Segoe UI", 10)
        )

        style.configure(

            "Treeview.Heading",

            background="#252526",

            foreground="white",

            relief="flat",

            font=("Segoe UI", 10, "bold")
        )

        style.map(

            "Treeview",

            background=[
                ("selected", "#3a3d41")
            ]
        )

        self.tree.heading(
            "#0",
            text="Name"
        )

        self.tree.heading(
            "type",
            text="Type"
        )

        self.tree.heading(
            "size",
            text="Size"
        )

        self.tree.heading(
            "modified",
            text="Date Modified"
        )

        self.tree.column(
            "#0",
            width=450,
            anchor="w"
        )

        self.tree.column(
            "path",
            width=0,
            stretch=False
        )

        self.tree.column(
            "type",
            width=180,
            anchor="center"
        )

        self.tree.column(
            "size",
            width=120,
            anchor="center"
        )

        self.tree.column(
            "modified",
            width=180,
            anchor="center"
        )

        self.tree.pack(
            fill="both",
            expand=True
        )

    # =============================================
    # CLEAR
    # =============================================

    def clear(self):

        self.tree.delete(
            *self.tree.get_children()
        )

    # =============================================
    # INSERT ITEM
    # =============================================

    def insert_item(

        self,

        path,

        name,

        file_type,

        size,

        modified,

        icon="📄"
    ):

        self.tree.insert(

            "",

            "end",

            text=f"{icon}  {name}",

            values=(

                path,

                file_type,

                size,

                modified
            )
        )

    # =============================================
    # GET SELECTED
    # =============================================

    def get_selected(self):

        selected = self.tree.selection()

        if not selected:
            return None

        return selected[0]

    # =============================================
    # GET ITEM NAME
    # =============================================

    def get_item_name(self, item_id):

        text = self.tree.item(
            item_id,
            "text"
        )

        if "  " in text:
            return text.split(
                "  ",
                1
            )[1]

        return text

    # =============================================
    # GET SELECTED PATH
    # =============================================

    def get_selected_path(self):

        item = self.get_selected()

        if not item:
            return None

        values = self.tree.item(
            item,
            "values"
        )

        if not values:
            return None

        return values[0]

    # =============================================
    # BINDINGS
    # =============================================

    def bind_double_click(
        self,
        callback
    ):

        self.tree.bind(
            "<Double-1>",
            callback
        )

    def bind_right_click(
        self,
        callback
    ):

        self.tree.bind(
            "<Button-3>",
            callback
        )

    def bind_select(
        self,
        callback
    ):

        self.tree.bind(
            "<<TreeviewSelect>>",
            callback
        )