import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

    def home_window(self):
        """
        Create and display the home window with navigation buttons.
        """
        self.destroy()
        self.__init__(self.master)

        # Create buttons
        btn_all_games = tk.Button(self, text="All Games", command=self.all_games_window)
        btn_releases = tk.Button(self, text="Game Releases", command=self.release_window)
        btn_enemies = tk.Button(self, text="Game Bosses", command=self.enemy_window)
        btn_npcs = tk.Button(self, text="NPCs", command=self.npc_window)

        # Create explanation labels
        lbl_all_games = tk.Label(self, text="View all games on the database")
        lbl_releases = tk.Label(self, text="View individual games and consoles they were released on")
        lbl_enemies = tk.Label(self, text="View Bosses from a game")
        lbl_npcs = tk.Label(self, text="View NPCs from a game")
        lbl_header = tk.Label(self, text="This is my python Program to help display data from my zelda database! Click a button to continue!")

        # Place buttons and labels in grid
        lbl_header.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        btn_all_games.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        lbl_all_games.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        btn_releases.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        lbl_releases.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        btn_enemies.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        lbl_enemies.grid(row=3, column=1, sticky="w", padx=5, pady=5)

        btn_npcs.grid(row=4, column=0, sticky="w", padx=5, pady=5)
        lbl_npcs.grid(row=4, column=1, sticky="w", padx=5, pady=5)

    def all_games_window(self):
        """
        Display a window showing all games in the database.
        """
        self.destroy()
        self.__init__(self.master)

        # Create a canvas and scrollbars
        canvas = tk.Canvas(self)
        v_scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        h_scrollbar = tk.Scrollbar(self, orient="horizontal", command=canvas.xview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        # Pack the canvas and scrollbars
        canvas.grid(row=0, column=0, sticky="nsew")
        v_scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar.grid(row=1, column=0, sticky="ew")

        # Make the frame expandable
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Making the Column names
        lbl_name = tk.Label(scrollable_frame, text="Name")
        lbl_copies_sold = tk.Label(scrollable_frame, text="Copies Sold")
        lbl_release = tk.Label(scrollable_frame, text="Original Console Release")

        # Making the home button
        btn_home = tk.Button(scrollable_frame, text="Home", command=self.home_window)

        # Placing the widgets
        btn_home.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        lbl_name.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        lbl_copies_sold.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        lbl_release.grid(row=1, column=2, sticky="w", padx=5, pady=5)
        
        # Call display_data() for all games
        self.display_data(query.all_games, 2, scrollable_frame)

    def enemy_window(self):
        """
        Display a window for selecting and viewing enemies from a specific game.
        """
        self.destroy()
        self.__init__(self.master)

        # Create a canvas and scrollbars
        canvas = tk.Canvas(self)
        v_scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        h_scrollbar = tk.Scrollbar(self, orient="horizontal", command=canvas.xview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        # Pack the canvas and scrollbars
        canvas.grid(row=0, column=0, sticky="nsew")
        v_scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar.grid(row=1, column=0, sticky="ew")

        # Make the frame expandable
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Making column name
        lbl_name = tk.Label(scrollable_frame, text="Boss Name")

        # Making the home button
        btn_home = tk.Button(scrollable_frame, text="Home", command=self.home_window)

        # Define the options for the dropdown menu
        options = []
        names = query.game_names()
        for name in names:
            options.append(name[0])
        
        # Create a StringVar to hold the selected option
        selected_option = tk.StringVar(scrollable_frame)
        selected_option.set(options[0])  # Set the default value

        # Create the OptionMenu (dropdown menu)
        dropdown = tk.OptionMenu(scrollable_frame, selected_option, *options)
        btn_confirm = tk.Button(scrollable_frame, text="Search", command=lambda: self.display_data(query.game_enemies, 3, scrollable_frame, selected_option))

        # Placing widgets
        btn_home.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        dropdown.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        btn_confirm.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        lbl_name.grid(row=2, column=0, padx=5, pady=5)

    def release_window(self):
        """
        Display a window for viewing game releases on different consoles.
        """
        self.destroy()
        self.__init__(self.master)

        # Create a canvas and scrollbars
        canvas = tk.Canvas(self)
        v_scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        h_scrollbar = tk.Scrollbar(self, orient="horizontal", command=canvas.xview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        # Pack the canvas and scrollbars
        canvas.grid(row=0, column=0, sticky="nsew")
        v_scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar.grid(row=1, column=0, sticky="ew")

        # Make the frame expandable
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Making column name
        lbl_name = tk.Label(scrollable_frame, text="Name")
        lbl_console = tk.Label(scrollable_frame, text="Console")

        # Making the home button
        btn_home = tk.Button(scrollable_frame, text="Home", command=self.home_window)

        # Define the options for the dropdown menu
        options = []
        names = query.game_names()
        for name in names:
            options.append(name[0])
        
        # Create a StringVar to hold the selected option
        selected_option = tk.StringVar(scrollable_frame)
        selected_option.set(options[0])  # Set the default value

        # Create the OptionMenu (dropdown menu)
        dropdown = tk.OptionMenu(scrollable_frame, selected_option, *options)
        btn_confirm = tk.Button(scrollable_frame, text="Search", command=lambda: self.display_data(query.game_release, 3, scrollable_frame, selected_option))

        # Placing widgets
        btn_home.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        dropdown.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        btn_confirm.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        lbl_name.grid(row=2, column=0, padx=5, pady=5)
        lbl_console.grid(row=2, column=1, padx=5, pady=5)

    def npc_window(self):
        """
        Display a window for selecting and viewing NPCs from a specific game.
        """
        self.destroy()
        self.__init__(self.master)

        # Create a canvas and scrollbars
        canvas = tk.Canvas(self)
        v_scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        h_scrollbar = tk.Scrollbar(self, orient="horizontal", command=canvas.xview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        # Pack the canvas and scrollbars
        canvas.grid(row=0, column=0, sticky="nsew")
        v_scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar.grid(row=1, column=0, sticky="ew")

        # Make the frame expandable
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Making column name
        lbl_name = tk.Label(scrollable_frame, text="NPC Name")

        # Making the home button
        btn_home = tk.Button(scrollable_frame, text="Home", command=self.home_window)

        # Define the options for the dropdown menu
        options = []
        names = query.game_names()
        for name in names:
            options.append(name[0])
        
        # Create a StringVar to hold the selected option
        selected_option = tk.StringVar(scrollable_frame)
        selected_option.set(options[0]) # Set the default value

        # Create the OptionMenu (dropdown menu)
        dropdown = tk.OptionMenu(scrollable_frame, selected_option, *options)
        btn_confirm = tk.Button(scrollable_frame, text="Search", command=lambda: self.display_data(query.game_npcs, 3, scrollable_frame, selected_option))

        # Placing widgets
        btn_home.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        dropdown.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        btn_confirm.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        lbl_name.grid(row=2, column=0, padx=5, pady=5)

    def display_data(self, desired_query, starting_row, frm_current, filter_var=None):
        """
        Display data retrieved from a query in the current frame.

        Args:
            desired_query (function): The query function to retrieve data.
            starting_row (int): The row number to start displaying data.
            frm_current (tk.Frame): The current frame to display data in.
            filter_var (tk.StringVar): The selected filter option.
        """

        # Clear existing data
        for widget in frm_current.grid_slaves():
            if int(widget.grid_info()["row"]) >= starting_row:
                widget.grid_forget()
        
        filter_value = filter_var.get() if filter_var else None
        data = desired_query(filter_value) if filter_var else desired_query()

        display_row = starting_row
        for row in data:
            display_column = 0
            for string in row:
                lbl_data = tk.Label(frm_current, text=string)
                lbl_data.grid(row=display_row, column=display_column, sticky="w", padx=5, pady=5)
                display_column += 1
            display_row += 1

        # Update scrollregion to include new data
        frm_current.update_idletasks()
        frm_current.master.configure(scrollregion=frm_current.master.bbox("all"))
