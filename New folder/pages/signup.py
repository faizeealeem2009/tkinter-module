import customtkinter as ctk
from tkinter import messagebox

from database.db import db


class SignupPage(ctk.CTkFrame):

    def __init__(self, parent, app):
        super().__init__(parent)

        self.app = app

        self.build_ui()

    def build_ui(self):

        title = ctk.CTkLabel(
            self,
            text="Create ChatHub Account",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=(40, 20))

        self.username_entry = ctk.CTkEntry(
            self,
            width=350,
            placeholder_text="Username"
        )
        self.username_entry.pack(pady=10)

        self.email_entry = ctk.CTkEntry(
            self,
            width=350,
            placeholder_text="Email"
        )
        self.email_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(
            self,
            width=350,
            placeholder_text="Password",
            show="*"
        )
        self.password_entry.pack(pady=10)

        self.confirm_entry = ctk.CTkEntry(
            self,
            width=350,
            placeholder_text="Confirm Password",
            show="*"
        )
        self.confirm_entry.pack(pady=10)

        create_btn = ctk.CTkButton(
            self,
            text="Create Account",
            width=350,
            command=self.create_account
        )
        create_btn.pack(pady=15)

        login_btn = ctk.CTkButton(
            self,
            text="Already have an account?",
            width=350,
            fg_color="gray30",
            command=self.app.open_login
        )
        login_btn.pack(pady=10)

        back_btn = ctk.CTkButton(
            self,
            text="Back",
            width=350,
            fg_color="gray25",
            command=self.app.show_welcome_screen
        )
        back_btn.pack(pady=10)

    def create_account(self):

        username = self.username_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        confirm = self.confirm_entry.get().strip()

        if not all([username, email, password, confirm]):
            messagebox.showerror(
                "Error",
                "Please fill all fields."
            )
            return

        if password != confirm:
            messagebox.showerror(
                "Error",
                "Passwords do not match."
            )
            return

        if len(password) < 6:
            messagebox.showerror(
                "Error",
                "Password must be at least 6 characters."
            )
            return

        created = db.create_user(
            username,
            email,
            password
        )

        if created:

            messagebox.showinfo(
                "Success",
                "Account created successfully."
            )

            self.app.open_login()

        else:

            messagebox.showerror(
                "Error",
                "Username or email already exists."
            )