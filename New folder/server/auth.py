import bcrypt
from database import cursor, conn


def register_user(username, email, password):

    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    try:
        cursor.execute(
            """
            INSERT INTO users
            (username,email,password)
            VALUES(?,?,?)
            """,
            (username, email, hashed)
        )

        conn.commit()
        return True

    except Exception:
        return False


def login_user(username, password):

    cursor.execute(
        """
        SELECT * FROM users
        WHERE username=?
        """,
        (username,)
    )

    user = cursor.fetchone()

    if not user:
        return False

    return bcrypt.checkpw(
        password.encode(),
        user[3]
    )