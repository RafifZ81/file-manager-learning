import os
import shutil
import datetime
from settings import FILE_TYPES


def sort_files(selected_folder, mode="extension"):

    if not selected_folder:
        return 0

    files = os.listdir(selected_folder)

    moved_count = 0

    for file in files:

        full_path = os.path.join(selected_folder, file)

        # Skip folders
        if not os.path.isfile(full_path):
            continue

        filename, ext = os.path.splitext(file)

        ext = ext.replace(".", "").lower()

        # =============================================
        # SORT BY EXTENSION
        # =============================================

        if mode == "extension":

            folder_name = ext.upper()

            if folder_name == "":
                folder_name = "OTHER"

        # =============================================
        # SORT BY TYPE
        # =============================================

        elif mode == "type":

            folder_name = "OTHER"

            for category, extensions in FILE_TYPES.items():

                if ext in extensions:

                    folder_name = category
                    break

        # =============================================
        # SORT BY DATE
        # =============================================

        elif mode == "date":

            modified_time = os.path.getmtime(full_path)

            date = datetime.datetime.fromtimestamp(modified_time)

            folder_name = f"{date.year}-{date.month}"

        else:

            folder_name = "OTHER"

        target_folder = os.path.join(selected_folder, folder_name)

        os.makedirs(target_folder, exist_ok=True)

        shutil.move(full_path, os.path.join(target_folder, file))

        moved_count += 1

    return moved_count