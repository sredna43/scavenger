import sqlite3

def db_setup(c):
    sql_create_clues = """CREATE TABLE IF NOT EXISTS clues (
        id integer PRIMARY KEY,
        passphrase text NOT NULL,
        next_clue text NOT NULL,
        hint1 text,
        hint2 text
    ); """
    sql_create_users = """CREATE TABLE IF NOT EXISTS users (
        id integer PRIMARY KEY,
        name text NOT NULL,
        username text NOT NULL,
        passhash text,
        last_clue_id integer
    );
    """
    c.execute(sql_create_clues)
    c.execute(sql_create_users)

def search_clue_by_passphrase(c, query):
    query = "%"+query+"%"
    print(query)
    c.execute("SELECT * FROM clues WHERE passphrase LIKE ?;", (query,))
    rows = c.fetchall()
    print("Rows: ", rows)
    try:
        return rows[0]
    except:
        return None

def get_clue_by_id(c, s_id):
    c.execute("SELECT * FROM clues WHERE id IS ?;", (s_id,))
    rows = c.fetchall()
    c.close()
    return rows

def add_user(c, name, username, passhash, last_clue_id):
    sql = "INSERT INTO users(name, username, passhash, last_clue_id) VALUES(?,?,?,?);"
    users = c.execute("select username from users;").fetchall()
    for user in users:
        if user[0] == username:
            return "Duplicate username detected"
    c.execute(sql, (name, username, passhash, last_clue_id))
    c.close()
    return "Added user " + username + " with id: " + str(c.lastrowid)

def add_clue(c, passphrase, next_clue, hint1, hint2):
    sql = "INSERT INTO clues(passphrase, next_clue, hint1, hint2) VALUES(?,?,?,?);"
    clues = c.execute("select passphrase from clues;").fetchall()
    for clue in clues:
        if clue[0] == passphrase:
            return "Duplicate passphrase detected"
    c.execute(sql, (passphrase, next_clue, hint1, hint2))
    c.close()
    return "Added clue " + next_clue + " with id: " + str(c.lastrowid)

def get_all_users(c):
    users = []
    c.execute("SELECT username FROM users;")
    rows = c.fetchall()
    for username in rows:
        users.append(username[0])
    return users

def get_passhash_by_username(c, username):
    c.execute("SELECT passhash FROM users WHERE username is ?;", (username,))
    return c.fetchall()