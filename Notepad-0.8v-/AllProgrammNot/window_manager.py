import tkinter as tk
from tkinter import messagebox

def close_all_windows(main_window, is_modified):
    """
    Handle closing of the main window and all child windows
    """
    def confirm_close():
        if is_modified:
            response = messagebox.askyesnocancel(
                "Save Changes?",
                "Do you want to save changes before closing?",
                icon='warning'
            )
            if response is None:  # Cancel was clicked
                return False
            if response:  # Yes was clicked
                # Here you can call your SaveFile function
                pass
        
        # Close all toplevel windows
        for window in main_window.winfo_children():
            if isinstance(window, tk.Toplevel):
                window.destroy()
        
        # Close main window
        main_window.destroy()
        return True

    return confirm_close

def setup_window_closing(main_window, is_modified):
    """
    Set up the window closing protocol
    """
    close_handler = close_all_windows(main_window, is_modified)
    main_window.protocol("WM_DELETE_WINDOW", close_handler)