import tkinter as tk
import os
import subprocess

from tkinter import messagebox

from filemaster_ui.property_window import show_properties
from filemaster_ui.file_ops import delete_item


class ContextMenu:

    def __init__(self, root, app):

        self.root = root
        self.app = app

        self.menu = tk.Menu(
            root,
            tearoff=0
        )

        # =============================================
        # MENU ITEMS
        # =============================================

        self.menu.add_command(
            label="Open",
            command=self.open_selected
        )

        self.menu.add_separator()

        self.menu.add_command(
            label="Copy Name",
            command=self.copy_name
        )

        self.menu.add_command(
            label="Copy Path",
            command=self.copy_path
        )

        self.menu.add_command(
            label="Open in Explorer",
            command=self.open_in_explorer
        )

        self.menu.add_separator()

        self.menu.add_command(
            label="Properties",
            command=self.show_properties
        )

        self.menu.add_separator()

        self.menu.add_command(
            label="Delete",
            command=self.delete_selected
        )

    # =================================================
    # SHOW MENU
    # =================================================

    def show(self, event):

        tree = self.app.file_view.filetree.tree

        selected = tree.identify_row(
            event.y
        )

        if not selected:
            return

        tree.selection_set(selected)

        self.menu.tk_popup(
            event.x_root,
            event.y_root
        )

    # =================================================
    # OPEN
    # =================================================

    def open_selected(self):

        self.app.open_selected()

    # =================================================
    # COPY NAME
    # =================================================

    def copy_name(self):

        full_path = self.app.get_selected_path()

        if not full_path:
            return

        self.root.clipboard_clear()

        self.root.clipboard_append(
            os.path.basename(full_path)
        )

    # =================================================
    # COPY PATH
    # =================================================

    def copy_path(self):

        full_path = self.app.get_selected_path()

        if not full_path:
            return

        self.root.clipboard_clear()

        self.root.clipboard_append(
            full_path
        )

    # =================================================
    # OPEN IN EXPLORER
    # =================================================

    def open_in_explorer(self):

        full_path = self.app.get_selected_path()

        if not full_path:
            return

        subprocess.run([
            "explorer",
            "/select,",
            full_path
        ])

    # =================================================
    # PROPERTIES
    # =================================================

    def show_properties(self):

        full_path = self.app.get_selected_path()

        if not full_path:
            return

        show_properties(
            self.root,
            full_path
        )

    # =================================================
    # DELETE
    # =================================================

    def delete_selected(self):

        full_path = self.app.get_selected_path()

        if not full_path:
            return

        confirm = messagebox.askyesno(
            "Delete",
            f"Delete:\n\n{os.path.basename(full_path)}?"
        )

        if not confirm:
            return

        try:

            delete_item(full_path)

            self.app.refresh_files()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )