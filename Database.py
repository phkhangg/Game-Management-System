import sqlite3


def add(account, name, bundle_ID, release_date, language, certificate):
    """Add all the information of the game"""
    con = sqlite3.connect('games_management.db')
    cur = con.cursor()
    cur.execute(f"""
CREATE TABLE IF NOT EXISTS gameFor_{account}(id INTEGER PRIMARY KEY,
                                    name TEXT,
                                    bundle_ID TEXT,
                                    release_date TEXT,
                                    language TEXT,
                                    certificate TEXT)""")
    cur.execute(f"""
INSERT INTO gameFor_{account}(name, bundle_ID, release_date, language, certificate)
VALUES (?, ?, ?, ?, ?);""", (str(name), str(bundle_ID), str(release_date), str(language), str(certificate)))
    con.commit()
    con.close()


def display(account):
    """Display all the data of the user"""
    con = sqlite3.connect('games_management.db')
    cur = con.cursor()
    cur.execute(f"""
SELECT * FROM gameFor_{account}""")
    data = cur.fetchall()
    con.commit()
    con.close()
    return data


def uprelease_date(account, id, name, bundle_ID, release_date, language, certificate):
    """To uprelease_date information in database

    Args:
        account: account of the users
        id: id of a game
        name: name of a game
        bundle_ID: bundle_ID of a game
        release_date: release_date the bundle_ID write for a game
        language: language of a game
        certificate: certificate of a game
    """
    con = sqlite3.connect('games_management.db')
    cur = con.cursor()
    cur.execute(f"""
UPrelease_date gameFor_{account}
SET name = ?,
    bundle_ID = ?,
    release_date = ?,
    language = ?,
    certificate = ?
WHERE id = {id};""", (name, bundle_ID, release_date, language, certificate))
    con.commit()
    con.close()


def delete(account, id):
    """Delete one release_date based on the id of games you chose"""
    con = sqlite3.connect('games_management.db')
    cur = con.cursor()
    cur.execute(f"DELETE FROM gameFor_{account} WHERE id = {id}")
    con.commit()
    con.close()


def delete_all(account):
    """Delete all the data in the database"""
    con = sqlite3.connect('games_management.db')
    cur = con.cursor()
    cur.execute(f"DROP TABLE IF EXISTS gameFor_{account}")
    cur.execute(f"""
CREATE TABLE IF NOT EXISTS gameFor_{account}(id INTEGER PRIMARY KEY,
                                    name TEXT,
                                    bundle_ID TEXT,
                                    release_date TEXT,
                                    language TEXT,
                                    certificate TEXT)""")
    con.commit()
    con.close()


def search(account, type_of_search, search):
    """To search the content you want to find in the database

    Args:
        account (_type_): account of the user
        type_of_search (_type_): choose the attribute you want to search
        search (_type_): search the content of that attribute

    Returns:
        data: return the data you want to search
    """
    con = sqlite3.connect('games_management.db')
    cur = con.cursor()
    search_command = f"SELECT * FROM gameFor_{account} WHERE {type_of_search} LIKE '%{search}%'"
    cur.execute(search_command)
    data = cur.fetchall()
    con.commit()
    con.close()
    return data
