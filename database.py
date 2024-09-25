import sqlite3

def creat_table():
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()

    cursor.execute('''
                       CREATE TABLE IF NOT EXISTS Employees(
                   id TEXT PRIMARY KEY,
                   name TEXT ,
                   role TEXT ,
                   gender TEXT,
                   status TEXT ) 
                   ''')
    conn.commit()
    conn.close()    

def fetch_employees():
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Employees')
    employees = cursor.fetchall()
    conn.close()
    return employees


def insert_employees(id, name, role, gender, status):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Employees (id, name, role, gender, status) VALUES (?, ?, ?, ?, ?)',
                   (id, name, role, gender, status))
    conn.commit()
    conn.close()

    


def delete_employees(id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Employees WHERE id = ?',(id,))
    conn.commit()
    conn.close()


def update_employees(new_name, new_role, new_gender, new_status, id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE Employees SET name =?, role =?, gender =?, status =? WHERE id =?',
                   (new_name, new_role, new_gender, new_status, id))  # Notez les parenthèses autour des variables
    conn.commit()
    conn.close()


def id_exists(id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Employees WHERE id=?',(id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0

creat_table()

    