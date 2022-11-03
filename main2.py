import sqlite3 as sql

boglash = sql.connect("Baza_institut.db")

inform = boglash.cursor()

inform.execute("""
CREATE TABLE IF NOT EXISTS Institut(
    nomi TEXT,
    fakultet_soni INTEGER
)
""")

inform.execute("""
CREATE TABLE IF NOT EXISTS Fakultet(
    fakultet_nomi TEXT,
    talabalar_soni INTEGER
)
""")