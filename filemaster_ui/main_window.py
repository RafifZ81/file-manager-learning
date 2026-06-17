# filemaster_ui/main_window.py

import tkinter as tk
import os

from tkinter import filedialog
from tkinter import messagebox

from filemaster_ui.sidebar import Sidebar
from filemaster_ui.file_view import FileView
from filemaster_ui.context_menu import ContextMenu
from filemaster_ui.navigation import (
    get_drives,
    get_quick_access
)
from filemaster_ui.toolbar import Toolbar
from filemaster_ui.statusbar import StatusBar
from filemaster_ui.sorting import sort_files


class MainWindow:

    def __init__(self, root):

        self.root = root

        self.root.title("Filemaster")
        self.root.geometry("1400x800")
        self.root.configure(bg="#1e1e1e")

        # =========================================
        # CURRENT FOLDER
        # =========================================

        self.selected_folder = ""

        # =========================================
        # NAVIGATION HISTORY
        # =========================================

        self.history = []
        self.history_index = -1

        # =========================================
        # TOOLBAR
        # =========================================

        self.toolbar = Toolbar(
            self.root
        )

        # =========================================
        # MAIN CONTENT
        # =========================================

        self.content_frame = tk.Frame(
            self.root,
            bg="#1e1e1e"
        )

        self.content_frame.pack(
            fill="both",
            expand=True
        )

        # =========================================
        # SIDEBAR
        # =========================================

        self.sidebar = Sidebar(
            self.content_frame
        )

        self.sidebar.frame.pack(
            side="left",
            fill="y"
        )

        # =========================================
        # FILE VIEW
        # =========================================

        self.file_view = FileView(
            self.content_frame
        )

        # =========================================
        # STATUSBAR
        # =========================================

        self.statusbar = StatusBar(
            self.root
        )

        # =========================================
        # CONTEXT MENU
        # =========================================

        self.context_menu = ContextMenu(
            self.root,
            self
        )

        # =========================================
        # SETUP
        # =========================================

        self.setup_navigation()
        self.setup_toolbar()
        self.setup_bindings()

    # =================================================
    # TOOLBAR SETUP
    # =================================================

    def setup_toolbar(self):

        self.toolbar.open_button.config(
            command=self.select_folder
        )

        self.toolbar.refresh_button.config(
            command=self.refresh_files
        )

        self.toolbar.back_button.config(
            command=self.go_back
        )

        self.toolbar.forward_button.config(
            command=self.go_forward
        )

        self.toolbar.up_button.config(
            command=self.go_up
        )

        self.toolbar.organize_button.config(
            command=self.show_organize_menu
        )

        self.toolbar.name_sort.config(
            command=lambda:
            self.sort_view("name")
        )

        self.toolbar.date_sort.config(
            command=lambda:
            self.sort_view("date")
        )

        self.toolbar.type_sort.config(
            command=lambda:
            self.sort_view("type")
        )

    # =================================================
    # NAVIGATION SETUP
    # =================================================

    def setup_navigation(self):

        for name, path in get_quick_access().items():

            self.sidebar.create_nav_button(

                self.sidebar.quick_frame,

                f"📁 {name}",

                lambda p=path:
                self.open_folder(p)
            )

        for drive in get_drives():

            self.sidebar.create_nav_button(

                self.sidebar.drive_frame,

                f"💽 {drive}",

                lambda d=drive:
                self.open_folder(d)
            )

    # =================================================
    # BINDINGS
    # =================================================

    def setup_bindings(self):

        self.file_view.filetree.bind_double_click(
            lambda e:
            self.open_selected()
        )

        self.file_view.filetree.bind_right_click(
            self.context_menu.show
        )

        self.file_view.pathbar.bind_enter(
            self.navigate_from_pathbar
        )

    # =================================================
    # SELECT FOLDER
    # =================================================

    def select_folder(self):

        folder = filedialog.askdirectory()

        if folder:

            self.open_folder(folder)

    # =================================================
    # OPEN FOLDER
    # =================================================

    def open_folder(self, folder):

        if not os.path.exists(folder):
            return

        self.selected_folder = folder

        self.file_view.load_files(folder)

        self.update_statusbar()

        # =========================================
        # SAVE HISTORY
        # =========================================

        if (
            self.history_index == -1
            or
            self.history[self.history_index] != folder
        ):

            self.history = (
                self.history[:self.history_index + 1]
            )

            self.history.append(folder)

            self.history_index += 1

    # =================================================
    # REFRESH
    # =================================================

    def refresh_files(self):

        if self.selected_folder:

            self.file_view.refresh()

            self.update_statusbar()

    # =================================================
    # STATUSBAR
    # =================================================

    def update_statusbar(self):

        count = len(
            self.file_view.filetree.tree.get_children()
        )

        self.statusbar.set_left(
            self.selected_folder
        )

        self.statusbar.set_right(
            f"{count} items"
        )

    # =================================================
    # GET SELECTED PATH
    # =================================================

    def get_selected_path(self):

        file_name = (
            self.file_view.get_selected_file()
        )

        if not file_name:
            return None

        return os.path.join(
            self.selected_folder,
            file_name
        )

    # =================================================
    # OPEN SELECTED
    # =================================================

    def open_selected(self):

        full_path = self.get_selected_path()

        if not full_path:
            return

        if os.path.isdir(full_path):

            self.open_folder(full_path)

        else:

            os.startfile(full_path)

    # =================================================
    # SORT VIEW
    # =================================================

    def sort_view(self, mode):

        if not self.selected_folder:
            return

        try:

            files = [

                os.path.join(
                    self.selected_folder,
                    item
                )

                for item in os.listdir(
                    self.selected_folder
                )
            ]

            # =========================================
            # FOLDERS FIRST
            # =========================================

            folders = [
                f for f in files
                if os.path.isdir(f)
            ]

            normal_files = [
                f for f in files
                if not os.path.isdir(f)
            ]

            # =========================================
            # SORTING
            # =========================================

            if mode == "name":

                folders.sort(
                    key=lambda x:
                    os.path.basename(x).lower()
                )

                normal_files.sort(
                    key=lambda x:
                    os.path.basename(x).lower()
                )

            elif mode == "date":

                folders.sort(
                    key=os.path.getmtime,
                    reverse=True
                )

                normal_files.sort(
                    key=os.path.getmtime,
                    reverse=True
                )

            elif mode == "type":

                normal_files.sort(
                    key=lambda x:
                    os.path.splitext(x)[1]
                )

            files = folders + normal_files

            # =========================================
            # REFRESH TREE
            # =========================================

            self.file_view.filetree.clear()

            for path in files:

                file_data = (
                    self.file_view.loader
                    .get_file_info(path)
                )

                self.file_view.insert_file(
                    file_data
                )

        except Exception as e:

            print(e)

    # =================================================
    # ORGANIZE MENU
    # =================================================

    def show_organize_menu(self):

        if not self.selected_folder:
            return

        menu = tk.Menu(
            self.root,
            tearoff=0
        )

        menu.add_command(
            label="By Extension",
            command=lambda:
            self.organize_files("extension")
        )

        menu.add_command(
            label="By Type",
            command=lambda:
            self.organize_files("type")
        )

        menu.add_command(
            label="By Date",
            command=lambda:
            self.organize_files("date")
        )

        x = (
            self.toolbar.organize_button
            .winfo_rootx()
        )

        y = (
            self.toolbar.organize_button
            .winfo_rooty()
            +
            self.toolbar.organize_button
            .winfo_height()
        )

        menu.tk_popup(x, y)

    # =================================================
    # ORGANIZE FILES
    # =================================================

    def organize_files(self, mode):

        if not self.selected_folder:
            return

        confirm = messagebox.askyesno(

            "Organize Files",

            "This will move files into new folders.\n\n"
            "Current file locations will change.\n\n"
            "Continue?"
        )

        if not confirm:
            return

        try:

            moved = sort_files(
                self.selected_folder,
                mode
            )

            self.refresh_files()

            messagebox.showinfo(

                "Organize Complete",

                f"{moved} files organized."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # =================================================
    # BACK
    # =================================================

    def go_back(self):

        if self.history_index > 0:

            self.history_index -= 1

            folder = (
                self.history[self.history_index]
            )

            self.selected_folder = folder

            self.file_view.load_files(folder)

            self.update_statusbar()

    # =================================================
    # FORWARD
    # =================================================

    def go_forward(self):

        if self.history_index < len(self.history) - 1:

            self.history_index += 1

            folder = (
                self.history[self.history_index]
            )

            self.selected_folder = folder

            self.file_view.load_files(folder)

            self.update_statusbar()

    # =================================================
    # GO UP
    # =================================================

    def go_up(self):

        if not self.selected_folder:
            return

        parent = os.path.dirname(
            self.selected_folder
        )

        if parent and parent != self.selected_folder:

            self.open_folder(parent)

    # =================================================
    # PATHBAR NAVIGATION
    # =================================================

    def navigate_from_pathbar(
        self,
        event=None
    ):

        path = (
            self.file_view.pathbar.get_path()
        )

        if os.path.exists(path):

            self.open_folder(path)

        else:

            messagebox.showerror(
                "Error",
                "Path not found"
            )


# =====================================================
# START APP
# =====================================================

def start_app():

    root = tk.Tk()

    MainWindow(root)

    root.mainloop()