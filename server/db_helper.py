def db_setup(c):
    sql_create_clues = """CREATE TABLE IF NOT EXISTS clues (
        id integer PRIMARY KEY,
        passphrase text NOT NULL,
        next_clue text NOT NULL,
        hint1 text,
        hint2 text
    ); """
    try:
        c.execute(sql_create_clues)
    except Error as e:
        print(e)

def search_db(c, query):
    query = "%"+query+"%"
    print(query)
    c.execute("SELECT * FROM clues WHERE passphrase LIKE ?;", (query,))
    rows = c.fetchall()
    print("Rows: ", rows)
    try:
        return rows[0]
    except:
        return None