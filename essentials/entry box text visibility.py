#date 9 feb 2025

from typing import Final
AUTHOR: Final[str] = "Satyam maddeshiya"
VERSION: Final[str] = "1.0.0"

import tkinter as tk
from tkinter import Entry , END

root=tk.Tk()
def txt_in_box(placeholder: str, padx: int, pady: int) -> str:
    entry = Entry(root, fg='grey')
    entry.insert(0, placeholder)

    # Add event bindings to handle focus in/out
    entry.bind("<FocusIn>", lambda event: entry.delete(0, END) if entry.get() == placeholder else None)
    entry.bind("<FocusOut>", lambda event: entry.insert(0, placeholder) if not entry.get() else None)

    entry.pack(padx=padx, pady=pady)
    return "done"

txt_in_box("ram",22,33)
root.mainloop()