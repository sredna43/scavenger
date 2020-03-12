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
        username test NOT NULL,
        passhash 
    )
    """
    try:
        c.execute(sql_create_clues)
    except Error as e:
        print(e)

def search_by_passphrase(c, query):
    query = "%"+query+"%"
    print(query)
    c.execute("SELECT * FROM clues WHERE passphrase LIKE ?;", (query,))
    rows = c.fetchall()
    print("Rows: ", rows)
    try:
        return rows[0]
    except:
        return None

def add_user(c, name, username, passhash, last_clue):
    sql = "INSERT INTO users(name, username, passhash, last_clue) VALUES(?,?,?,?);"
    c.execute(sql, (name, username, passhash, last_clue))
    return c.lastrowid