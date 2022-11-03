import sqlite3 as sql

boglash = sql.connect("Baza_kurs.db")

malumot = boglash.cursor()

malumot.execute("""
CREATE TABLE IF NOT EXISTS Kurs(
    kurs_nomi TEXT,
    kurs_oy INTEGER
)
""")

malumot.execute("""
CREATE TABLE IF NOT EXISTS Yunalish(
    yunalish_nomi TEXT,
    oylik_tulov INTEGER
)
""")