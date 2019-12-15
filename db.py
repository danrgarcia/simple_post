import sqlite3

print("\nOpening DB")
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

print("Reading Script...")
scriptFile = open('schema.sql', 'r')
script = scriptFile.read()
scriptFile.close()

print("Running Script...")
cursor.executescript(script)