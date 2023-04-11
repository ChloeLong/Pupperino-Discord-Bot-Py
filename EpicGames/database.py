import sqlite3
import os
from EpicGames.game import Game

class Database:
    def retrieveActive():
        game_list = []

        conn = sqlite3.connect(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')), 'GameDeals.db'))
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Epic_GameDeals WHERE active='1'")
        results = cursor.fetchall()
        for item in results:
            game_list.append(Game(item[1].decode("utf-8"),item[2].decode("utf-8"),item[3], item[4], item[5], item[6]))

        return game_list

    def retrieveUpcoming():
        game_list = []

        conn = sqlite3.connect(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')), 'GameDeals.db'))
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Epic_GameDeals WHERE active='0'")
        results = cursor.fetchall()
        for item in results:
            game_list.append(Game(item[1].decode("utf-8"),item[2].decode("utf-8"),item[3], item[4], item[5], item[6]))

        return game_list
