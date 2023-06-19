import pyodbc

# Set up connection parameters
server = 'TEACH2C-93918Z8'
database = 'master'
trusted_connection = 'yes'

# Establish a connection
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection};'
conn = pyodbc.connect(conn_str)

# Perform database operations
# ...
# Example: Execute a query
cursor = conn.cursor()
cursor.execute("SELECT * FROM StatsInfo")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()