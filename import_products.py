import json
import mysql.connector

# Read data from the JSON file
with open('petlebi_products.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# MySQL database connection parameters
db_config = {
    'host': 'sql11.freemysqlhosting.net',
    'user': 'sql11671400',
    'password': 'wb19LMvs9V',
    'database': 'sql11671400',
}

# Connect to the MySQL database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Read and execute SQL queries from petlebi_create.sql
with open('petlebi_create.sql', 'r', encoding='utf-8') as create_file:
    create_queries = create_file.read().split(';')
    for query in create_queries:
        if query.strip():
            cursor.execute(query)

# Commit changes to the database
connection.commit()

# Insert data into the petlebi table
insert_query = """
INSERT INTO petlebi (url, name, price, category, stock, images, brand, origin, barkod, skt, description)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

for product in data:
    values = (
        product['url'],
        product['name'],
        product['price'],
        product['category'],
        product['stock'],
        json.dumps(product['images']),  # Convert images to JSON string
        product['brand'],
        product['origin'],
        product['barkod'],
        product['skt'],
        '\n'.join(product['description']),  # Join description list to a newline-separated string
    )
    cursor.execute(insert_query, values)

connection.commit()

# Close the database connection
cursor.close()
connection.close()
