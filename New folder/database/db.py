import sqlite3
import bcrypt

DB_NAME = "database.db"


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Users table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password BLOB NOT NULL,
            bio TEXT DEFAULT '',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Posts table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
        """)

        self.conn.commit()

    # ---------- USER FUNCTIONS ----------

    def create_user(self, username, email, password):
        try:
            hashed_password = bcrypt.hashpw(
                password.encode("utf-8"),
                bcrypt.gensalt()
            )

            self.cursor.execute("""
            INSERT INTO users(username, email, password)
            VALUES (?, ?, ?)
            """, (username, email, hashed_password))

            self.conn.commit()
            return True

        except sqlite3.IntegrityError:
            return False

    def login_user(self, username, password):
        self.cursor.execute("""
        SELECT * FROM users
        WHERE username = ?
        """, (username,))

        user = self.cursor.fetchone()

        if not user:
            return None

        stored_password = user[3]

        if bcrypt.checkpw(
            password.encode("utf-8"),
            stored_password
        ):
            return user

        return None

    def get_user(self, user_id):
        self.cursor.execute("""
        SELECT * FROM users
        WHERE id = ?
        """, (user_id,))

        return self.cursor.fetchone()

    # ---------- POST FUNCTIONS ----------

    def create_post(self, user_id, content):
        self.cursor.execute("""
        INSERT INTO posts(user_id, content)
        VALUES (?, ?)
        """, (user_id, content))

        self.conn.commit()

    def get_posts(self):
        self.cursor.execute("""
        SELECT
            posts.id,
            users.username,
            posts.content,
            posts.created_at
        FROM posts
        JOIN users
        ON posts.user_id = users.id
        ORDER BY posts.id DESC
        """)

        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
    def update_bio(self, user_id, bio):
        self.cursor.execute(
            """
            UPDATE users
            SET bio = ?
            WHERE id = ?
            """,
            (bio, user_id)
        )

        self.conn.commit()


db = Database()
