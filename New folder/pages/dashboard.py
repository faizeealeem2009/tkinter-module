import customtkinter as ctk
from tkinter import messagebox

from database.db import db


class DashboardPage(ctk.CTkFrame):

    def __init__(self, parent, app):
        super().__init__(parent)

        self.app = app

        self.build_ui()
        self.load_posts()

    def build_ui(self):

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=220)
        self.sidebar.pack(side="left", fill="y", padx=5, pady=5)

        username = self.app.current_user[1]

        ctk.CTkLabel(
            self.sidebar,
            text="ChatHub",
            font=("Arial", 28, "bold")
        ).pack(pady=20)

        ctk.CTkLabel(
            self.sidebar,
            text=f"@{username}",
            font=("Arial", 16)
        ).pack(pady=5)

        ctk.CTkButton(
            self.sidebar,
            text="Profile",
            command=self.app.open_profile
        ).pack(fill="x", padx=10, pady=10)

        ctk.CTkButton(
            self.sidebar,
            text="Refresh Feed",
            command=self.load_posts
        ).pack(fill="x", padx=10, pady=10)

        ctk.CTkButton(
            self.sidebar,
            text="Logout",
            fg_color="red",
            command=self.app.logout
        ).pack(fill="x", padx=10, pady=10)

        # Main Area
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(
            side="right",
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

        ctk.CTkLabel(
            self.main_frame,
            text="News Feed",
            font=("Arial", 24, "bold")
        ).pack(pady=10)

        self.post_box = ctk.CTkTextbox(
            self.main_frame,
            width=700,
            height=120
        )
        self.post_box.pack(pady=10)

        ctk.CTkButton(
            self.main_frame,
            text="Create Post",
            command=self.create_post
        ).pack(pady=10)

        # Scroll Feed
        self.feed_frame = ctk.CTkScrollableFrame(
            self.main_frame,
            width=800,
            height=450
        )
        self.feed_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    def create_post(self):

        content = self.post_box.get(
            "1.0",
            "end"
        ).strip()

        if not content:
            messagebox.showerror(
                "Error",
                "Post cannot be empty."
            )
            return

        user_id = self.app.current_user[0]

        db.create_post(
            user_id,
            content
        )

        self.post_box.delete(
            "1.0",
            "end"
        )

        messagebox.showinfo(
            "Success",
            "Post published."
        )

        self.load_posts()

    def load_posts(self):

        for widget in self.feed_frame.winfo_children():
            widget.destroy()

        posts = db.get_posts()

        if not posts:

            ctk.CTkLabel(
                self.feed_frame,
                text="No posts yet."
            ).pack(pady=20)

            return

        for post in posts:

            post_id, username, content, created_at = post

            card = ctk.CTkFrame(
                self.feed_frame
            )
            card.pack(
                fill="x",
                padx=10,
                pady=10
            )

            ctk.CTkLabel(
                card,
                text=f"@{username}",
                font=("Arial", 16, "bold")
            ).pack(
                anchor="w",
                padx=10,
                pady=(10, 0)
            )

            ctk.CTkLabel(
                card,
                text=created_at,
                text_color="gray"
            ).pack(
                anchor="w",
                padx=10
            )

            ctk.CTkLabel(
                card,
                text=content,
                wraplength=650,
                justify="left"
            ).pack(
                anchor="w",
                padx=10,
                pady=10
            )