import tkinter as tk
from database_manager import DatabaseManager

class Application(tk.Frame):
    def __init__(self, master=None, db_path: str = "zelda.sqlite"):
        super().__init__(master)
        self.master = master
        # Make the application frame expand with the window
        self.pack(fill="both", expand=True)
        self.db = DatabaseManager(db_path)

    def home_window(self):
        """Create and display the home window with navigation buttons."""
        self.destroy()
        self.__init__(self.master, self.db.db_path)

        btn_all_games = tk.Button(self, text="All Games", command=self.all_games_window)
        btn_releases = tk.Button(self, text="Game Releases", command=self.release_window)
        btn_enemies = tk.Button(self, text="Game Bosses", command=self.enemy_window)
        btn_npcs = tk.Button(self, text="NPCs", command=self.npc_window)

        lbl_all_games = tk.Label(self, text="View all games on the database")
        lbl_releases = tk.Label(self, text="View individual games and consoles they were released on")
        lbl_enemies = tk.Label(self, text="View Bosses from a game")
        lbl_npcs = tk.Label(self, text="View NPCs from a game")
        lbl_header = tk.Label(self, text="This is my python Program to help display data from my zelda database! Click a button to continue!")

        lbl_header.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        btn_all_games.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        lbl_all_games.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        btn_releases.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        lbl_releases.grid(row=2, column=1, sticky="w", padx=5, pady=5)
        btn_enemies.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        lbl_enemies.grid(row=3, column=1, sticky="w", padx=5, pady=5)
        btn_npcs.grid(row=4, column=0, sticky="w", padx=5, pady=5)
        lbl_npcs.grid(row=4, column=1, sticky="w", padx=5, pady=5)

    def _make_canvas_area(self):
        """
        Helper to create a canvas + scrollbars + scrollable_frame.
        Returns (canvas, v_scrollbar, h_scrollbar, scrollable_frame).
        The returned scrollable_frame gets attributes referencing the canvas and scrollbars
        so display_data can show/hide them based on content.
        """
        canvas = tk.Canvas(self)
        v_scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        h_scrollbar = tk.Scrollbar(self, orient="horizontal", command=canvas.xview)
        scrollable_frame = tk.Frame(canvas)

        # Ensure the inner frame resizes to the canvas width to avoid unwanted horizontal scrollbar
        canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # update scrollregion when inner frame changes
        scrollable_frame.bind(
            "<Configure>",
            lambda e, c=canvas: c.configure(scrollregion=c.bbox("all"))
        )
        # resize the window item whenever the canvas size changes
        canvas.bind(
            "<Configure>",
            lambda e, win=canvas_window, c=canvas: c.itemconfig(win, width=e.width)
        )

        canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        # store references so display_data can access them
        scrollable_frame._canvas = canvas
        scrollable_frame._v_scrollbar = v_scrollbar
        scrollable_frame._h_scrollbar = h_scrollbar

        # place them in the application's grid so they expand
        canvas.grid(row=0, column=0, sticky="nsew")
        v_scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar.grid(row=1, column=0, sticky="ew")

        # ensure the application frame gives space to the canvas
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        return canvas, v_scrollbar, h_scrollbar, scrollable_frame

    def all_games_window(self):
        """Display a window showing all games in the database."""
        self.destroy()
        self.__init__(self.master, self.db.db_path)

        canvas, v_scrollbar, h_scrollbar, scrollable_frame = self._make_canvas_area()

        lbl_name = tk.Label(scrollable_frame, text="Name")
        lbl_copies_sold = tk.Label(scrollable_frame, text="Copies Sold")
        lbl_release = tk.Label(scrollable_frame, text="Original Console Release")
        btn_home = tk.Button(scrollable_frame, text="Home", command=self.home_window)

        btn_home.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        lbl_name.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        lbl_copies_sold.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        lbl_release.grid(row=1, column=2, sticky="w", padx=5, pady=5)
        
        self.display_data(self.db.all_games, 2, scrollable_frame)

    def enemy_window(self):
        """Select and view enemies from a specific game."""
        self.destroy()
        self.__init__(self.master, self.db.db_path)

        canvas, v_scrollbar, h_scrollbar, scrollable_frame = self._make_canvas_area()

        lbl_name = tk.Label(scrollable_frame, text="Boss Name")
        btn_home = tk.Button(scrollable_frame, text="Home", command=self.home_window)

        options = [name[0] for name in self.db.game_names()] or ["(no games)"]
        selected_option = tk.StringVar(scrollable_frame)
        selected_option.set(options[0])

        dropdown = tk.OptionMenu(scrollable_frame, selected_option, *options)
        btn_confirm = tk.Button(scrollable_frame, text="Search", command=lambda: self.display_data(self.db.game_enemies, 3, scrollable_frame, selected_option))

        btn_home.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        dropdown.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        btn_confirm.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        lbl_name.grid(row=2, column=0, padx=5, pady=5)

    def release_window(self):
        """View game releases on different consoles."""
        self.destroy()
        self.__init__(self.master, self.db.db_path)

        canvas, v_scrollbar, h_scrollbar, scrollable_frame = self._make_canvas_area()

        lbl_name = tk.Label(scrollable_frame, text="Name")
        lbl_console = tk.Label(scrollable_frame, text="Console")
        btn_home = tk.Button(scrollable_frame, text="Home", command=self.home_window)

        options = [name[0] for name in self.db.game_names()] or ["(no games)"]
        selected_option = tk.StringVar(scrollable_frame)
        selected_option.set(options[0])

        dropdown = tk.OptionMenu(scrollable_frame, selected_option, *options)
        btn_confirm = tk.Button(scrollable_frame, text="Search", command=lambda: self.display_data(self.db.game_release, 3, scrollable_frame, selected_option))

        btn_home.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        dropdown.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        btn_confirm.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        lbl_name.grid(row=2, column=0, padx=5, pady=5)
        lbl_console.grid(row=2, column=1, padx=5, pady=5)

    def npc_window(self):
        """Select and view NPCs from a specific game."""
        self.destroy()
        self.__init__(self.master, self.db.db_path)

        canvas, v_scrollbar, h_scrollbar, scrollable_frame = self._make_canvas_area()

        lbl_name = tk.Label(scrollable_frame, text="NPC Name")
        btn_home = tk.Button(scrollable_frame, text="Home", command=self.home_window)

        options = [name[0] for name in self.db.game_names()] or ["(no games)"]
        selected_option = tk.StringVar(scrollable_frame)
        selected_option.set(options[0])

        dropdown = tk.OptionMenu(scrollable_frame, selected_option, *options)
        btn_confirm = tk.Button(scrollable_frame, text="Search", command=lambda: self.display_data(self.db.game_npcs, 3, scrollable_frame, selected_option))

        btn_home.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        dropdown.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        btn_confirm.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        lbl_name.grid(row=2, column=0, padx=5, pady=5)

    def display_data(self, desired_query, starting_row, frm_current, filter_var=None):
        """
        desired_query: callable that accepts either no args or a single string arg (filter).
        filter_var: tk.StringVar or None
        """
        # clear existing data rows
        for widget in frm_current.grid_slaves():
            try:
                if int(widget.grid_info().get("row", 0)) >= starting_row:
                    widget.grid_forget()
            except Exception:
                pass

        filter_value = filter_var.get() if filter_var else None
        data = desired_query(filter_value) if filter_var else desired_query()

        display_row = starting_row
        for row in data:
            display_column = 0
            for val in row:
                lbl = tk.Label(frm_current, text=str(val))
                lbl.grid(row=display_row, column=display_column, sticky="w", padx=5, pady=5)
                display_column += 1
            display_row += 1

        # ensure canvas scrollregion is up to date
        frm_current.update_idletasks()

        # show/hide scrollbars based on content vs canvas size
        canvas = getattr(frm_current, "_canvas", None)
        v_scrollbar = getattr(frm_current, "_v_scrollbar", None)
        h_scrollbar = getattr(frm_current, "_h_scrollbar", None)
        if canvas:
            bbox = canvas.bbox("all")
            canvas.update_idletasks()
            # vertical
            if v_scrollbar:
                if bbox and bbox[3] > canvas.winfo_height():
                    # show
                    v_scrollbar.grid(row=0, column=1, sticky="ns")
                else:
                    v_scrollbar.grid_remove()
            # horizontal
            if h_scrollbar:
                if bbox and bbox[2] > canvas.winfo_width():
                    h_scrollbar.grid(row=1, column=0, sticky="ew")
                else:
                    h_scrollbar.grid_remove()

def main():
    root = tk.Tk()
    root.title("Zelda Search")
    app = Application(master=root)
    app.home_window()
    root.mainloop()

if __name__ == "__main__":
    main()
