# Filemaster

A modern desktop file manager built with Python and Tkinter.

Filemaster aims to provide a lightweight Windows-style file explorer with a clean interface, file management tools, navigation shortcuts, and extensible architecture.

---

## Features

### Navigation
- Open folders
- Quick Access sidebar
- Drive navigation
- Path bar navigation
- Refresh current directory (F5)

### File Browsing
- File and folder listing
- Search files instantly
- Sort by:
  - Name
  - Date Modified
  - File Type

### Context Menu
- Open
- Copy Name
- Copy Path
- Open in Explorer
- Properties
- Delete

### Properties Window
- File information
- Folder information
- Creation date
- Modification date
- Size calculation
- Folder contents count
- Rename support

### User Interface
- Dark theme
- Emoji file icons
- Status bar
- Sidebar navigation
- Search bar
- Path bar

---

## Project Structure

```text
Filemaster/
│
├── main.py
│
├── file_ops.py
│
├── filemaster_ui/
│   │
│   ├── main_window.py
│   ├── toolbar.py
│   ├── sidebar.py
│   ├── statusbar.py
│   ├── navigation.py
│   │
│   ├── file_view.py
│   ├── filetree.py
│   ├── file_loader.py
│   │
│   ├── pathbar.py
│   ├── searchbar.py
│   │
│   ├── context_menu.py
│   ├── property_window.py
│   └── icon_handler.py
│
└── README.md
```

---

## Requirements

- Python 3.11+
- Tkinter

Tkinter comes bundled with standard Python installations.

Verify installation:

```bash
python --version
```

---

## Running Filemaster

From the project root:

```bash
python main.py
```

---

## Current Status

Implemented:

- File browsing
- Search
- Sorting
- Context menu
- Properties window
- Rename
- Delete
- Path navigation
- Sidebar navigation

Planned:

- Back button
- Forward button
- Up folder button
- Breadcrumb path bar
- Copy/Paste
- Cut/Paste
- Multi-select
- Drag & Drop
- File preview panel
- Real Windows file icons
- Tab support

---

## Screenshots

Add screenshots here as the project grows.

```text
docs/screenshots/main-window.png
```

---

## Design Goals

Filemaster is designed to be:

- Lightweight
- Fast
- Easy to understand
- Modular
- Beginner-friendly for learning desktop application development

The codebase is intentionally separated into small UI components to make maintenance and future feature additions easier.

---

## License

MIT License

Feel free to modify, learn from, and extend the project.
