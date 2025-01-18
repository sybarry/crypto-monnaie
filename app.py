from tkinter import Tk
from ui.ui_manager import CryptoNotifierUI

if __name__ == "__main__":
    root = Tk()
    app = CryptoNotifierUI(root)
    app.set_event_handlers()  # Configure les actions des boutons
    root.mainloop()
