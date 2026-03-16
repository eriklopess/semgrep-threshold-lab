import sqlite3
import subprocess
import os

SECRET_KEY = "minha-chave-super-secreta-123"

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # VULNERABILIDADE: SQL injection — concatenação direta de input
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()

def run_command(user_input):
    # VULNERABILIDADE: subprocess com shell=True e input do usuário
    result = subprocess.run(
        "echo " + user_input,
        shell=True,
        capture_output=True,
        text=True
    )
    return result.stdout

def hash_password(password):
    import hashlib
    # VULNERABILIDADE: uso de MD5 para hash de senha
    return hashlib.md5(password.encode()).hexdigest()

if __name__ == "__main__":
    print(get_user("admin"))
    print(run_command("hello world"))
