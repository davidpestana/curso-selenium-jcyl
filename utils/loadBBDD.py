import mysql.connector

def load_bbdd_data():
    conn = mysql.connector.connect(
        host='localhost',   # Cambia esto si tu base de datos está en otro host    
        user='root',        # Cambia esto por tu usuario
        password='example',# Cambia esto por tu contraseña
        database='testdb'   # Cambia esto por el nombre de tu base de datos
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT num1, num2, res FROM productos")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows