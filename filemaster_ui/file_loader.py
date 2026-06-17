import os
import time


class FileLoader:

    # =================================================
    # LOAD FOLDER
    # =================================================

    def load_folder(self, folder):

        files_data = []

        if not folder:
            return files_data

        try:

            entries = os.listdir(folder)

            # =========================================
            # SORT FOLDERS FIRST
            # =========================================

            entries.sort(

                key=lambda x: (

                    not os.path.isdir(
                        os.path.join(
                            folder,
                            x
                        )
                    ),

                    x.lower()
                )
            )

            for file_name in entries:

                full_path = os.path.join(
                    folder,
                    file_name
                )

                files_data.append(

                    self.get_file_info(
                        full_path
                    )
                )

        except Exception as e:

            print(
                f"Load Error: {e}"
            )

        return files_data

    # =================================================
    # GET FILE INFO
    # =================================================

    def get_file_info(self, full_path):

        file_name = os.path.basename(
            full_path
        )

        # =============================================
        # FOLDER
        # =============================================

        if os.path.isdir(full_path):

            icon = "📁"

            file_type = "Folder"

            size = "--"

        # =============================================
        # FILE
        # =============================================

        else:

            extension = os.path.splitext(
                file_name
            )[1].lower()

            icon = self.get_file_icon(
                extension
            )

            if extension:

                file_type = (
                    extension[1:].upper()
                    + " File"
                )

            else:

                file_type = "File"

            try:

                size = self.format_size(

                    os.path.getsize(
                        full_path
                    )
                )

            except:

                size = "--"

        # =============================================
        # MODIFIED DATE
        # =============================================

        try:

            modified = time.strftime(

                "%Y-%m-%d %H:%M",

                time.localtime(

                    os.path.getmtime(
                        full_path
                    )
                )
            )

        except:

            modified = "--"

        return {

            "name": file_name,

            "display_name":
                f"{icon} {file_name}",

            "path": full_path,

            "is_folder": os.path.isdir(
                full_path
            ),

            "type": file_type,

            "size": size,

            "modified": modified
        }

    # =================================================
    # FILE ICONS
    # =================================================

    def get_file_icon(self, extension):

        icon_map = {

            # Images
            ".png": "🖼",
            ".jpg": "🖼",
            ".jpeg": "🖼",
            ".gif": "🖼",
            ".bmp": "🖼",
            ".webp": "🖼",

            # Audio
            ".mp3": "🎵",
            ".wav": "🎵",
            ".ogg": "🎵",
            ".flac": "🎵",

            # Video
            ".mp4": "🎬",
            ".mkv": "🎬",
            ".avi": "🎬",
            ".mov": "🎬",

            # Archives
            ".zip": "📦",
            ".rar": "📦",
            ".7z": "📦",

            # Documents
            ".pdf": "📕",
            ".txt": "📄",
            ".doc": "📄",
            ".docx": "📄",
            ".ppt": "📊",
            ".pptx": "📊",
            ".xls": "📗",
            ".xlsx": "📗",

            # Code
            ".py": "🐍",
            ".js": "🟨",
            ".html": "🌐",
            ".css": "🎨",
            ".json": "🧩",

            # Executable
            ".exe": "⚙"
        }

        return icon_map.get(
            extension,
            "📄"
        )

    # =================================================
    # FORMAT SIZE
    # =================================================

    def format_size(self, size):

        if size < 1024:

            return f"{size} B"

        elif size < 1024 * 1024:

            return (
                f"{size / 1024:.2f} KB"
            )

        elif size < 1024 * 1024 * 1024:

            return (
                f"{size / (1024 * 1024):.2f} MB"
            )

        else:

            return (
                f"{size / (1024 * 1024 * 1024):.2f} GB"
            )