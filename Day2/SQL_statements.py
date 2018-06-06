import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

#create tables
cursor.execute('''
CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)
''')

cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
connection.commit()

symbol = 'RHAT'
cursor.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

stocks_row = cursor.fetchone()
print(type(stocks_row))
print(stocks_row)

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
connection.close()