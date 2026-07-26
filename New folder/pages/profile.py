import customtkinter as ctk
from tkinter import messagebox

from database.db import db


class ProfilePage(ctk.CTkFrame):

    def __init__(self, parent, app):
        super().__init__(parent)

        self.app = app

        self.build_ui()

    def build_ui(self):

        user = self.app.current_user

        ctk.CTkLabel(
            self,
            text="My Profile",
            font=("Arial", 30, "bold")
        ).pack(pady=30)

        ctk.CTkLabel(
            self,
            text=f"Username: {user[1]}",
            font=("Arial", 18)
        ).pack(pady=10)

        ctk.CTkLabel(
            self,
            text=f"Email: {user[2]}",
            font=("Arial", 18)
        ).pack(pady=10)

        ctk.CTkLabel(
            self,
            text="Bio"
        ).pack(pady=(20, 5))

        self.bio_box = ctk.CTkTextbox(
            self,
            width=500,
            height=120
        )
        self.bio_box.pack(pady=10)

        current_bio = user[4] if user[4] else ""
        self.bio_box.insert(
            "1.0",
            current_bio
        )

        ctk.CTkButton(
            self,
            text="Save Bio",
            command=self.save_bio
        ).pack(pady=10)

        ctk.CTkButton(
            self,
            text="Back to Dashboard",
            command=self.app.open_dashboard
        ).pack(pady=10)

    def save_bio(self):

        bio = self.bio_box.get(
            "1.0",
            "end"
        ).strip()

        user_id = self.app.current_user[0]

        db.cursor.execute(
            """
            UPDATE users
            SET bio = ?
            WHERE id = ?
            """,
            (bio, user_id)
        )

        db.conn.commit()

        updated_user = db.get_user(user_id)

        self.app.current_user = updated_user

        messagebox.showinfo(
            "Success",
            "Profile updated."
        )