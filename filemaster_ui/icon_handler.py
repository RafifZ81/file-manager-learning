# filemaster_ui/icon_handler.py

import os


def get_file_icon(path):

    if os.path.isdir(path):
        return "📁"

    extension = os.path.splitext(path)[1].lower()

    icon_map = {

        # Images
        ".png": "🖼",
        ".jpg": "🖼",
        ".jpeg": "🖼",
        ".gif": "🖼",
        ".webp": "🖼",
        ".bmp": "🖼",

        # Music
        ".mp3": "🎵",
        ".wav": "🎵",
        ".flac": "🎵",
        ".ogg": "🎵",

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

        # Executables
        ".exe": "⚙",
    }

    return icon_map.get(extension, "📄")