import tkinter as tk
from tkinter import messagebox

import os
import time


# =====================================================
# SHOW PROPERTIES
# =====================================================

def show_properties(root, full_path):

    try:

        item_name = os.path.basename(full_path)

        # =================================================
        # TYPE
        # =================================================

        if os.path.isdir(full_path):
            item_type = "File Folder"
        else:
            ext = os.path.splitext(item_name)[1]

            if ext:
                item_type = f"{ext.upper()[1:]} File"
            else:
                item_type = "File"

        # =================================================
        # SIZE + CONTAINS
        # =================================================

        total_size = 0
        file_count = 0
        folder_count = 0

        if os.path.isfile(full_path):

            total_size = os.path.getsize(full_path)

        else:

            for dirpath, dirnames, filenames in os.walk(full_path):

                folder_count += len(dirnames)
                file_count += len(filenames)

                for f in filenames:

                    fp = os.path.join(dirpath, f)

                    try:
                        total_size += os.path.getsize(fp)
                    except:
                        pass

        # =================================================
        # FORMAT SIZE
        # =================================================

        def format_size(size):

            if size < 1024:
                return f"{size} B"

            elif size < 1024 * 1024:
                return f"{size / 1024:.2f} KB"

            elif size < 1024 * 1024 * 1024:
                return f"{size / (1024 * 1024):.2f} MB"

            else:
                return f"{size / (1024 * 1024 * 1024):.2f} GB"

        readable_size = format_size(total_size)

        # =================================================
        # DATES
        # =================================================

        created = time.strftime(
            "%d %B %Y %H:%M",
            time.localtime(
                os.path.getctime(full_path)
            )
        )

        modified = time.strftime(
            "%d %B %Y %H:%M",
            time.localtime(
                os.path.getmtime(full_path)
            )
        )

        # =================================================
        # WINDOW
        # =================================================

        window = tk.Toplevel(root)

        window.title(
            f"{item_name} Properties"
        )

        window.geometry("520x420")
        window.resizable(False, False)

        bg = "#1e1e1e"
        fg = "white"
        line = "#404040"

        window.configure(bg=bg)

        # =================================================
        # MAIN FRAME
        # =================================================

        main = tk.Frame(
            window,
            bg=bg
        )

        main.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        # =================================================
        # ICON + NAME
        # =================================================

        top_frame = tk.Frame(
            main,
            bg=bg
        )

        top_frame.pack(
            fill="x",
            pady=(0, 15)
        )

        icon = "📁" if os.path.isdir(full_path) else "📄"

        tk.Label(
            top_frame,
            text=icon,
            bg=bg,
            fg=fg,
            font=("Segoe UI Emoji", 24)
        ).pack(side="left")

        name_var = tk.StringVar(
            value=item_name
        )

        name_entry = tk.Entry(
            top_frame,
            textvariable=name_var,
            bg="#2d2d30",
            fg="white",
            insertbackground="white",
            relief="flat",
            font=("Segoe UI", 11)
        )

        name_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(10, 0),
            ipady=6
        )

        # =================================================
        # SEPARATOR
        # =================================================

        tk.Frame(
            main,
            bg=line,
            height=1
        ).pack(
            fill="x",
            pady=5
        )

        # =================================================
        # INFO ROW
        # =================================================

        def add_row(label, value):

            row = tk.Frame(
                main,
                bg=bg
            )

            row.pack(
                fill="x",
                pady=4
            )

            tk.Label(
                row,
                text=label,
                width=12,
                anchor="w",
                bg=bg,
                fg="#cfcfcf",
                font=("Segoe UI", 10)
            ).pack(side="left")

            tk.Label(
                row,
                text=value,
                anchor="w",
                justify="left",
                bg=bg,
                fg=fg,
                font=("Segoe UI", 10)
            ).pack(side="left")

        # =================================================
        # GENERAL INFO
        # =================================================

        add_row("Type:", item_type)

        add_row(
            "Location:",
            os.path.dirname(full_path)
        )

        add_row(
            "Size:",
            f"{readable_size} ({total_size:,} bytes)"
        )

        if os.path.isdir(full_path):

            add_row(
                "Contains:",
                f"{file_count:,} files, {folder_count:,} folders"
            )

        tk.Frame(
            main,
            bg=line,
            height=1
        ).pack(
            fill="x",
            pady=10
        )

        add_row(
            "Created:",
            created
        )

        add_row(
            "Modified:",
            modified
        )

        # =================================================
        # BUTTONS
        # =================================================

        bottom = tk.Frame(
            main,
            bg=bg
        )

        bottom.pack(
            side="bottom",
            fill="x",
            pady=(20, 0)
        )

        # =================================================
        # APPLY RENAME
        # =================================================

        def apply_changes():

            new_name = (
                name_var.get().strip()
            )

            if not new_name:
                return

            if new_name == item_name:
                window.destroy()
                return

            try:

                parent = os.path.dirname(
                    full_path
                )

                new_path = os.path.join(
                    parent,
                    new_name
                )

                os.rename(
                    full_path,
                    new_path
                )

                window.destroy()

            except Exception as e:

                messagebox.showerror(
                    "Rename Failed",
                    str(e)
                )

        # =================================================
        # OK BUTTON
        # =================================================

        tk.Button(
            bottom,
            text="OK",
            command=apply_changes,
            bg="#0e639c",
            fg="white",
            relief="flat",
            width=10
        ).pack(
            side="right",
            padx=(5, 0)
        )

        # =================================================
        # CANCEL BUTTON
        # =================================================

        tk.Button(
            bottom,
            text="Cancel",
            command=window.destroy,
            bg="#3c3c3c",
            fg="white",
            relief="flat",
            width=10
        ).pack(
            side="right"
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )