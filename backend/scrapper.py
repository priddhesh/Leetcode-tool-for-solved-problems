import pymysql
from bs4 import BeautifulSoup

html_doc = """
"""

host = 'localhost'
user = 'root'
password = 'riddhesh@12345'
database = 'leetcode'

# Establish MySQL connection
conn = pymysql.connect(host=host, user=user, password=password, database=database)

# Create a cursor object
cursor = conn.cursor()

soup = BeautifulSoup(html_doc, 'html.parser')

unique_strings = set()

for tr in soup.find_all('tr'):
    second_td = tr.find_all('td')[1].get_text()
    unique_strings.add(second_td)

for string in unique_strings:
    try:
        cursor.execute("SELECT * FROM solvedques WHERE ques= %s", (string,))
        if not cursor.fetchone():
            cursor.execute("INSERT INTO solvedques(ques,status) VALUES (%s,%s)", (string,"0"))
            conn.commit()
    except pymysql.Error as e:
        print(f"Error inserting data: {e}")

cursor.close()
conn.close()
