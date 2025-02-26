import sqlite3
from flask import Flask, request

app = Flask(__name__)

# 🚨 VULNERABLE CODE: SQL Injection (GHAS will detect this)
def get_user_info(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # ❌ Bad practice: Directly injecting user input into SQL query
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)  # ⚠️ SQL Injection vulnerability
    
    result = cursor.fetchall()
    conn.close()
    return result

@app.route('/user', methods=['GET'])
def user():
    username = request.args.get('username')
    data = get_user_info(username)
    return {"data": data}

if __name__ == '__main__':
    app.run(debug=True)
