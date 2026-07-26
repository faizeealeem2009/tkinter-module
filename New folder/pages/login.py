import customtkinter as ctk
from tkinter import messagebox

from database.db import db


class LoginPage(ctk.CTkFrame):

    def __init__(self, parent, app):
        super().__init__(parent)

        self.app = app

        self.build_ui()

    def build_ui(self):

        title = ctk.CTkLabel(
            self,
            text="ChatHub Login",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=(50, 20))

        self.username_entry = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Username"
        )
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Password",
            show="*"
        )
        self.password_entry.pack(pady=10)

        login_btn = ctk.CTkButton(
            self,
            text="Login",
            width=300,
            command=self.login
        )
        login_btn.pack(pady=15)

        signup_btn = ctk.CTkButton(
            self,
            text="Create Account",
            width=300,
            fg_color="gray30",
            command=self.app.open_signup
        )
        signup_btn.pack(pady=10)

        back_btn = ctk.CTkButton(
            self,
            text="Back",
            width=300,
            fg_color="gray25",
            command=self.app.show_welcome_screen
        )
        back_btn.pack(pady=10)

    def login(self):

        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showerror(
                "Error",
                "Please fill all fields."
            )
            return

        user = db.login_user(username, password)

        if user:
            messagebox.showinfo(
                "Success",
                f"Welcome {username}"
            )

            self.app.login_success(user)

        else:
            messagebox.showerror(
                "Error",
                "Invalid username or password."
            )