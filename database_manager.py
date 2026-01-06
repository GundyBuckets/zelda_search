import sqlite3
from typing import List, Tuple, Optional

class DatabaseManager:
    """
    Simple SQLite database manager that exposes the queries formerly in zelda_query.py.
    Methods return lists of tuples (rows). Uses parameterized queries to avoid injection.
    """

    def __init__(self, db_path: str = "zelda.sqlite"):
        self.db_path = db_path

    def _fetch(self, sql: str, params: Optional[tuple] = None) -> List[Tuple]:
        params = params or ()
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(sql, params)
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    def all_games(self) -> List[Tuple]:
        """Return (game_name, copies_sold, console_name) for all games."""
        sql = """
            SELECT game_name, copies_sold, console_name
            FROM game g JOIN console c
                ON g.console_id = c.console_id
        """
        return self._fetch(sql)

    def game_names(self) -> List[Tuple]:
        """Return (game_name,) for all games."""
        sql = "SELECT game_name FROM game"
        return self._fetch(sql)

    def game_release(self, game_name: str) -> List[Tuple]:
        """
        Return (name, console_name) for the given game including re-releases.
        Uses parameterized queries.
        """
        sql = """
            SELECT game_name, console_name
            FROM game g JOIN console c
                ON g.console_id = c.console_id
            WHERE game_name = ?
            UNION
            SELECT rr.re_release_name, c.console_name
            FROM re_release rr
            JOIN game g ON g.game_id = rr.game_id
            JOIN console c ON rr.console_id = c.console_id
            WHERE g.game_name = ?
        """
        return self._fetch(sql, (game_name, game_name))

    def game_enemies(self, game_name: str) -> List[Tuple]:
        """Return (enemy_name,) for enemies appearing in the specified game."""
        sql = """
            SELECT enemy_name FROM enemy
            JOIN enemy_to_game
                ON enemy.enemy_id = enemy_to_game.enemy_id
            JOIN game
                ON enemy_to_game.game_id = game.game_id
            WHERE game_name = ?
        """
        return self._fetch(sql, (game_name,))

    def game_npcs(self, game_name: str) -> List[Tuple]:
        """Return (npc_name,) for NPCs appearing in the specified game."""
        sql = """
            SELECT npc_name FROM NPCs
            JOIN NPC_to_game
                ON NPCs.npc_id = NPC_to_game.npc_id
            JOIN game
                ON NPC_to_game.game_id = game.game_id
            WHERE game_name = ?
        """
        return self._fetch(sql, (game_name,))