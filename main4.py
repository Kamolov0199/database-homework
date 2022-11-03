import sqlite3 as sql

boglash = sql.connect("Baza_Maktab.db")

inform = boglash.cursor()

inform.execute("""
CREATE TABLE IF NOT EXISTS Sinfraxbar(
    ismi TEXT,
    sinf INTEGER
)
""")

inform.execute("""
CREATE TABLE IF NOT EXISTS Sinf(
    sinf_nomi TEXT,
    uquvchilar_soni INTEGER
)
""")