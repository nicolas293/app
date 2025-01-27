import time
import threading
from tkinter import Label

class StatusBar:
    def __init__(self, win, text_widget):
        # Create status label
        self.status_label = Label(win, anchor="w", padx=5)
        self.status_label.pack(side="bottom", fill="x")
        self.text_widget = text_widget
        self.running = True
        
        # Start update thread
        self.update_thread = threading.Thread(target=self._update_status, daemon=True)
        self.update_thread.start()
    
    def _update_status(self):
        while self.running:
            
            try:
                # Get cursor position
                cursor_pos = self.text_widget.index("insert")
                line, column = map(int, cursor_pos.split('.'))
                
                # Get text statistics
                content = self.text_widget.get("1.0", "end-1c")
                char_count = len(content)
                word_count = len(content.split())
                line_count = len(content.splitlines())
                
                # Update status text
                status_text = f"Line: {line} | Column: {column} | Characters: {char_count} | Words: {word_count} | Lines: {line_count}"
                self.status_label.config(text=status_text)
                
                time.sleep(0.1)  # Update every 100ms
            except Exception:
                break
    
    def stop(self):
        self.running = False