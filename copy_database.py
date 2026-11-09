import sqlite3

source = sqlite3.connect("supportflow.db")
destination = sqlite3.connect("supportflow_test.db")

source.backup(destination)

destination.close()
source.close()

print("Database copied successfully!")