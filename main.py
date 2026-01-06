import tkinter as tk
from Application import Application

def main():
    root = tk.Tk()
    root.title("Zelda Search")
    app = Application(master=root)
    app.home_window()
    root.mainloop()

if __name__ == "__main__":
    main()