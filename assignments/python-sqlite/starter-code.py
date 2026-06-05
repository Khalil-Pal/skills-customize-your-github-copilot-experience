import os
import sqlite3
from typing import Dict, List, Optional

DB_FILE = os.getenv("DB_PATH", os.path.join(os.path.dirname(__file__), "data.db"))


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(DB_FILE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db() -> None:
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL
            )
            """
        )
        conn.commit()


def create_item(name: str, description: Optional[str], price: float) -> Dict:
    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO items (name, description, price) VALUES (?, ?, ?)",
            (name, description, price),
        )
        conn.commit()
        return get_item(cursor.lastrowid)


def list_items() -> List[Dict]:
    with get_connection() as conn:
        cursor = conn.execute("SELECT * FROM items")
        return [dict(row) for row in cursor.fetchall()]


def get_item(item_id: int) -> Optional[Dict]:
    with get_connection() as conn:
        cursor = conn.execute("SELECT * FROM items WHERE id = ?", (item_id,))
        row = cursor.fetchone()
        return dict(row) if row else None


def update_item(item_id: int, name: Optional[str] = None, description: Optional[str] = None, price: Optional[float] = None) -> Optional[Dict]:
    existing = get_item(item_id)
    if not existing:
        return None

    updated = {
        "name": name if name is not None else existing["name"],
        "description": description if description is not None else existing["description"],
        "price": price if price is not None else existing["price"],
    }

    with get_connection() as conn:
        conn.execute(
            "UPDATE items SET name = ?, description = ?, price = ? WHERE id = ?",
            (updated["name"], updated["description"], updated["price"], item_id),
        )
        conn.commit()

    return get_item(item_id)


def delete_item(item_id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.execute("DELETE FROM items WHERE id = ?", (item_id,))
        conn.commit()
        return cursor.rowcount > 0


def search_items(name: str) -> List[Dict]:
    with get_connection() as conn:
        cursor = conn.execute("SELECT * FROM items WHERE name LIKE ?", (f"%{name}%",))
        return [dict(row) for row in cursor.fetchall()]


if __name__ == "__main__":
    init_db()
    print("Database initialized.")
    print("Use the functions in this file to create, list, update, delete, and search items.")
