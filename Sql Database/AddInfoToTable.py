import pyodbc

# Set up connection parameters
server = 'TEACH2C-93918Z8'
database = 'master'
trusted_connection = 'yes'

# Establish a connection
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection};'
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Define the INSERT INTO statement
insert_query = '''
    INSERT INTO StatsInfo (UserID, Name, StrengthInfo)
    VALUES (?, ?, ?)
'''

# Define the values to insert
values = (2, 'Sid', 'Strength level 15')

# Execute the INSERT INTO statement
cursor.execute(insert_query, *values)

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()