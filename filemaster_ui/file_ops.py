import os
from send2trash import send2trash


def rename_item(selected_folder, old_name, new_name):

    old_path = os.path.join(selected_folder, old_name)

    new_path = os.path.join(selected_folder, new_name)

    os.rename(old_path, new_path)


def delete_item(full_path):

    send2trash(full_path)


def open_item(full_path):

    os.startfile(full_path)