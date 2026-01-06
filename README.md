# Zelda Search

A Python-based desktop application for browsing and searching a Zelda video game database. Built with Tkinter for the GUI and SQLite for data storage, this tool allows users to explore games, their releases across different consoles, bosses (enemies), and non-player characters (NPCs) from the iconic Zelda franchise.

## Features

- **All Games View**: Display a list of all Zelda games in the database, including copies sold and original console release.
- **Game Releases**: Select a specific game to view all its releases and re-releases across different consoles.
- **Bosses (Enemies)**: Browse bosses from a selected game.
- **NPCs**: View non-player characters from a chosen game.
- **Scrollable Interface**: The application uses a scrollable canvas to handle large datasets comfortably.
- **Simple Navigation**: Easy-to-use buttons and dropdown menus for navigation between different views.

## Prerequisites

- Python 3.6 or higher (Tkinter is included in standard Python installations)
- SQLite database file (`zelda.sqlite`) with the required schema

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/GundyBuckets/zelda_search.git
   cd zelda_search
   ```

2. Ensure you have the `zelda.sqlite` database file in the project directory. The database should contain the following tables:
   - `game`: Stores game information (game_id, game_name, copies_sold, console_id)
   - `console`: Stores console information (console_id, console_name)
   - `re_release`: Stores re-release information (re_release_name, game_id, console_id)
   - `enemy`: Stores enemy information (enemy_id, enemy_name)
   - `enemy_to_game`: Junction table linking enemies to games
   - `NPCs`: Stores NPC information (npc_id, npc_name)
   - `NPC_to_game`: Junction table linking NPCs to games

3. Run the application:
   ```
   python main.py
   ```

## Usage

1. Launch the application by running `main.py`.
2. The home screen will display navigation buttons for different views.
3. Click on a button to navigate to the desired section:
   - **All Games**: View all games with their sales figures and original consoles.
   - **Game Releases**: Select a game from the dropdown and view its releases.
   - **Game Bosses**: Choose a game and see its bosses.
   - **NPCs**: Pick a game to view its non-player characters.
4. Use the "Home" button to return to the main menu at any time.

## Project Structure

- `main.py`: Entry point of the application.
- `Application.py`: Contains the Tkinter GUI logic and window management.
- `database_manager.py`: Handles all database interactions and queries.
- `zelda.sqlite`: The SQLite database file 

## Dependencies

- `tkinter`: For the graphical user interface (built-in with Python).
- `sqlite3`: For database operations (built-in with Python).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Hunter Gundersen