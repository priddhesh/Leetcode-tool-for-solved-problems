import pymysql
from bs4 import BeautifulSoup

html_doc = """
<tbody><tr><td>1&nbsp;year ago</td><td> Longest Common Subsequence </td><td><a class="text-danger" href="/submissions/detail/906529097/"><strong>Wrong Answer</strong></a></td><td>N/A</td><td>cpp</td></tr><tr><td>1&nbsp;year ago</td><td> Longest Common Subsequence </td><td><a class="text-danger" href="/submissions/detail/906526919/"><strong>Wrong Answer</strong></a></td><td>N/A</td><td>cpp</td></tr><tr><td>1&nbsp;year ago</td><td> Longest Common Subsequence </td><td><a class="text-danger" href="/submissions/detail/906525851/"><strong>Time Limit Exceeded</strong></a></td><td>N/A</td><td>cpp</td></tr><tr><td>1&nbsp;year ago</td><td> Shortest Distance to a Character </td><td><a class="text-success" href="/submissions/detail/906419665/"><strong>Accepted</strong></a></td><td>0 ms</td><td>cpp</td></tr><tr><td>1&nbsp;year ago</td><td> Shortest Distance to a Character </td><td><a class="text-danger" href="/submissions/detail/906418803/"><strong>Runtime Error</strong></a></td><td>N/A</td><td>cpp</td></tr><tr><td>1&nbsp;year ago</td><td> Leaf-Similar Trees </td><td><a class="text-success" href="/submissions/detail/906290560/"><strong>Accepted</strong></a></td><td>11 ms</td><td>cpp</td></tr><tr><td>1&nbsp;year ago</td><td> Symmetric Tree </td><td><a class="text-success" href="/submissions/detail/906287427/"><strong>Accepted</strong></a></td><td>0 ms</td><td>cpp</td></tr><tr><td>1&nbsp;year ago</td><td> Validate Binary Search Tree </td><td><a class="text-success" href="/submissions/detail/906252117/"><strong>Accepted</strong></a></td><td>8 ms</td><td>cpp</td></tr><tr><td>1&nbsp;year ago</td><td> Validate Binary Search Tree </td><td><a class="text-danger" href="/submissions/detail/906250670/"><strong>Wrong Answer</strong></a></td><td>N/A</td><td>cpp</td></tr><tr><td>1&nbsp;year ago</td><td> Validate Binary Search Tree </td><td><a class="text-danger" href="/submissions/detail/906250445/"><strong>Wrong Answer</strong></a></td><td>N/A</td><td>cpp</td></tr><tr><td>1&nbsp;year ago</td><td> Binary Tree Level Order Traversal </td><td><a class="text-success" href="/submissions/detail/906233284/"><strong>Accepted</strong></a></td><td>0 ms</td><td>cpp</td></tr><tr><td>1&nbsp;year ago</td><td> Binary Tree Zigzag Level Order Traversal </td><td><a class="text-success" href="/submissions/detail/906231291/"><strong>Accepted</strong></a></td><td>7 ms</td><td>cpp</td></tr><tr><td>1&nbsp;year ago</td><td> Generate Parentheses </td><td><a class="text-success" href="/submissions/detail/905988462/"><strong>Accepted</strong></a></td><td>0 ms</td><td>cpp</td></tr><tr><td>1&nbsp;year ago</td><td> Container With Most Water </td><td><a class="text-success" href="/submissions/detail/905905317/"><strong>Accepted</strong></a></td><td>98 ms</td><td>cpp</td></tr><tr><td>1&nbsp;year ago</td><td> Lowest Common Ancestor of a Binary Tree </td><td><a class="text-success" href="/submissions/detail/905871529/"><strong>Accepted</strong></a></td><td>20 ms</td><td>cpp</td></tr><tr><td>1&nbsp;year ago</td><td> Next Greater Element I </td><td><a class="text-success" href="/submissions/detail/905867750/"><strong>Accepted</strong></a></td><td>7 ms</td><td>cpp</td></tr><tr><td>1&nbsp;year ago</td><td> Next Greater Element III </td><td><a class="text-success" href="/submissions/detail/905831844/"><strong>Accepted</strong></a></td><td>0 ms</td><td>cpp</td></tr><tr><td>1&nbsp;year ago</td><td> Next Greater Element III </td><td><a class="text-danger" href="/submissions/detail/905831396/"><strong>Wrong Answer</strong></a></td><td>N/A</td><td>cpp</td></tr><tr><td>1&nbsp;year ago</td><td> Next Greater Element II </td><td><a class="text-success" href="/submissions/detail/905468898/"><strong>Accepted</strong></a></td><td>42 ms</td><td>cpp</td></tr><tr><td>1&nbsp;year ago</td><td> Next Greater Element II </td><td><a class="text-success" href="/submissions/detail/904639328/"><strong>Accepted</strong></a></td><td>35 ms</td><td>cpp</td></tr></tbody>
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
