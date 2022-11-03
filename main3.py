import sqlite3 as sql

boglash = sql.connect("Baza_Shifoxona.db")

inform = boglash.cursor()

inform.execute("""
CREATE TABLE IF NOT EXISTS Bulim(
    bulim_nomi TEXT,
    bemorlar_soni INTEGER
)
""")

inform.execute("""
CREATE TABLE IF NOT EXISTS Shifokor(
    ism TEXT,
    familiya TEXT,
    staj INTEGER
)
""")