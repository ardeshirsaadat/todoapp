import psycopg2
connection = psycopg2.connect('dbname=ardeshir user=postgres password=16760')
cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS table1;')
cursor.execute('''
  CREATE TABLE table1(
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT FALSE
  );
''')
cursor.execute('''
  INSERT INTO table1 (id,completed) VALUES (1,true);
''')
cursor.execute('INSERT INTO table1 (id,completed) VALUES (%s,%s);', (2, False))
cursor.execute('INSERT INTO table1 (id,completed) VALUES (%s,%s);', (3, False))
cursor.execute('SELECT * FROM table1')
results = cursor.fetchall()
connection.commit()
cursor.close()
connection.close()
for result in results:
    print(result)
# import psycopg2

# conn = psycopg2.connect('dbname=todoapp_development user=amy')

# cursor = conn.cursor()

# # Open a cursor to perform database operations
# cur = conn.cursor()

# # drop any existing todos table
# cur.execute("DROP TABLE IF EXISTS todos;")

# # (re)create the todos table
# # (note: triple quotes allow multiline text in python)
# cur.execute("""
#   CREATE TABLE todos (
#     id serial PRIMARY KEY,
#     description VARCHAR NOT NULL
#   );
# """)

# # commit, so it does the executions on the db and persists in the db
# conn.commit()

# cur.close()
# conn.close()

# using string interpolation to pass in values into cursor.execute


# cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))

# SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'

# data = {
#   'id': 2,
#   'completed': False
# }
# cursor.execute(SQL, data)
