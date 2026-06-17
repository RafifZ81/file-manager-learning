import tkinter as tk

from filemaster_ui.pathbar import PathBar
from filemaster_ui.searchbar import SearchBar
from filemaster_ui.filetree import FileTree
from filemaster_ui.file_loader import FileLoader

from filemaster_ui.icon_handler import get_file_icon


class FileView:

    def __init__(self, parent):

        # =============================================
        # MAIN FRAME
        # =============================================

        self.frame = tk.Frame(
            parent,
            bg="#1e1e1e"
        )

        self.frame.pack(
            fill="both",
            expand=True
        )

        # =============================================
        # TOP BAR
        # =============================================

        self.top_bar = tk.Frame(
            self.frame,
            bg="#252526"
        )

        self.top_bar.pack(
            fill="x",
            padx=10,
            pady=(10, 5)
        )

        # =============================================
        # PATH BAR
        # =============================================

        self.pathbar = PathBar(
            self.top_bar
        )

        self.pathbar.frame.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 10)
        )

        # =============================================
        # SEARCH BAR
        # =============================================

        self.searchbar = SearchBar(
            self.top_bar
        )

        self.searchbar.frame.pack(
            side="right"
        )

        # =============================================
        # FILE TREE
        # =============================================

        self.filetree = FileTree(
            self.frame
        )

        # =============================================
        # FILE LOADER
        # =============================================

        self.loader = FileLoader()

        # =============================================
        # DATA
        # =============================================

        self.current_folder = ""
        self.current_files = []

        # =============================================
        # SEARCH EVENT
        # =============================================

        self.searchbar.bind_keyrelease(
            self.search_files
        )

    # =================================================
    # LOAD FILES
    # =================================================

    def load_files(self, folder):

        self.current_folder = folder

        self.pathbar.set_path(
            folder
        )

        self.filetree.clear()

        self.current_files = (
            self.loader.load_folder(
                folder
            )
        )

        for file_data in self.current_files:

            self.insert_file(
                file_data
            )

    # =================================================
    # INSERT FILE
    # =================================================

    def insert_file(self, file_data):

        icon = get_file_icon(
            file_data["path"]
        )

        self.filetree.insert_item(

            path=file_data["path"],

            name=file_data['name'],

            file_type=file_data["type"],

            size=file_data["size"],

            modified=file_data["modified"],

            icon=icon
        )

    # =================================================
    # SEARCH FILES
    # =================================================

    def search_files(self, event=None):

        search_text = (
            self.searchbar.get_text()
            .lower()
        )

        self.filetree.clear()

        for file_data in self.current_files:

            if search_text in (
                file_data["name"]
                .lower()
            ):

                self.insert_file(
                    file_data
                )

    # =================================================
    # GET SELECTED FILE NAME
    # =================================================

    def get_selected_file(self):

        item = (
            self.filetree.get_selected()
        )

        if not item:
            return None

        return (
            self.filetree.get_item_name(
                item
            )
        )

    # =================================================
    # GET SELECTED PATH
    # =================================================

    def get_selected_path(self):

        return (
            self.filetree.get_selected_path()
        )

    # =================================================
    # REFRESH
    # =================================================

    def refresh(self):

        if self.current_folder:

            self.load_files(
                self.current_folder
            )