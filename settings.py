import json
import os

# =====================================================
# CONFIG FILE
# =====================================================

CONFIG_FILE = "config.json"

# =====================================================
# DEFAULT SETTINGS
# =====================================================

DEFAULT_SETTINGS = {

    "confirm_delete": True
}

# =====================================================
# LOAD SETTINGS
# =====================================================

def load_settings():

    # Create config if missing
    if not os.path.exists(CONFIG_FILE):

        save_settings(DEFAULT_SETTINGS)

        return DEFAULT_SETTINGS

    try:

        with open(CONFIG_FILE, "r") as file:

            settings = json.load(file)

            return settings

    except:

        return DEFAULT_SETTINGS

# =====================================================
# SAVE SETTINGS
# =====================================================

def save_settings(settings):

    with open(CONFIG_FILE, "w") as file:

        json.dump(settings, file, indent=4)

# =====================================================
# FILE TYPE CATEGORIES
# =====================================================

FILE_TYPES = {

    "Pictures": [
        "png", "jpg", "jpeg", "gif", "webp",
        "bmp", "svg", "ico", "tiff"
    ],

    "Documents": [
        "pdf", "doc", "docx", "txt",
        "rtf", "odt",
        "xls", "xlsx", "csv",
        "ppt", "pptx",
        "md"
    ],

    "Music": [
        "mp3", "wav", "flac",
        "aac", "ogg", "m4a"
    ],

    "Videos": [
        "mp4", "mkv", "avi",
        "mov", "wmv", "flv",
        "webm"
    ],

    "Archives": [
        "zip", "rar", "7z",
        "tar", "gz"
    ],

    "Code": [
        "py", "js", "html",
        "css", "cpp", "c",
        "java", "php", "json",
        "xml", "sql"
    ],

    "Applications": [
        "exe", "msi", "bat",
        "apk"
    ],

    "System": [
        "dll", "sys", "ini"
    ]
}