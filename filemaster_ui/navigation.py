import os
import string

# =====================================================
# GET DRIVES
# =====================================================

def get_drives():

    drives = []

    for letter in string.ascii_uppercase:

        drive = f"{letter}:/"

        if os.path.exists(drive):

            drives.append(drive)

    return drives

# =====================================================
# GET QUICK ACCESS
# =====================================================

def get_quick_access():

    home = os.path.expanduser("~")

    folders = {

        "Desktop":
        os.path.join(home, "Desktop"),

        "Documents":
        os.path.join(home, "Documents"),

        "Downloads":
        os.path.join(home, "Downloads"),

        "Pictures":
        os.path.join(home, "Pictures"),

        "Music":
        os.path.join(home, "Music"),

        "Videos":
        os.path.join(home, "Videos")
    }

    valid_folders = {}

    for name, path in folders.items():

        if os.path.exists(path):

            valid_folders[name] = path

    return valid_folders