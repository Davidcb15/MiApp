import sqlite3

def crear_db():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        dieta BOOLEAN DEFAULT 0,
        vegano BOOLEAN DEFAULT 0,
        vegetariano BOOLEAN DEFAULT 0
    )
    """)

    # Agregar columnas si no existen (para migración)
    try:
        cursor.execute("ALTER TABLE usuarios ADD COLUMN dieta BOOLEAN DEFAULT 0")
    except sqlite3.OperationalError:
        pass  # Columna ya existe
    try:
        cursor.execute("ALTER TABLE usuarios ADD COLUMN vegano BOOLEAN DEFAULT 0")
    except sqlite3.OperationalError:
        pass
    try:
        cursor.execute("ALTER TABLE usuarios ADD COLUMN vegetariano BOOLEAN DEFAULT 0")
    except sqlite3.OperationalError:
        pass

    conn.commit()
    conn.close()

if __name__ == "__main__":
    crear_db()
