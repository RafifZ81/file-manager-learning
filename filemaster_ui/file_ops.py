import os

from send2trash import send2trash


# =====================================================
# RENAME ITEM
# =====================================================

def rename_item(
    selected_folder,
    old_name,
    new_name
):

    old_path = os.path.join(
        selected_folder,
        old_name
    )

    new_path = os.path.join(
        selected_folder,
        new_name
    )

    old_path = os.path.normpath(
        os.path.abspath(old_path)
    )

    new_path = os.path.normpath(
        os.path.abspath(new_path)
    )

    os.rename(
        old_path,
        new_path
    )


# =====================================================
# DELETE ITEM
# =====================================================

def delete_item(full_path):

    if not os.path.exists(full_path):

        raise FileNotFoundError(
            f"Path not found:\n{full_path}"
        )

    full_path = os.path.normpath(
        os.path.abspath(full_path)
    )

    send2trash(full_path)


# =====================================================
# OPEN ITEM
# =====================================================

def open_item(full_path):

    full_path = os.path.normpath(
        os.path.abspath(full_path)
    )

    os.startfile(full_path)