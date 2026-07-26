print("START OF MAIN")
import customtkinter as ctk

from database.db import db
print("MAIN STARTED")
# Import pages later
# from pages.login import LoginPage
# from pages.signup import SignupPage
# from pages.dashboard import DashboardPage
# from pages.profile import ProfilePage


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class ChatHubApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("ChatHub")
        self.geometry("1200x700")
        self.minsize(1000, 600)

        self.current_user = None

        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        self.show_welcome_screen()

    # -----------------------------------
    # Frame Management
    # -----------------------------------

    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_welcome_screen(self):
        self.clear_container()

        frame = ctk.CTkFrame(self.container)
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        title = ctk.CTkLabel(
            frame,
            text="ChatHub",
            font=("Arial", 42, "bold")
        )
        title.pack(pady=(80, 20))

        subtitle = ctk.CTkLabel(
            frame,
            text="Connect • Share • Chat",
            font=("Arial", 18)
        )
        subtitle.pack(pady=10)

        login_btn = ctk.CTkButton(
            frame,
            text="Login",
            width=250,
            height=45,
            command=self.open_login
        )
        login_btn.pack(pady=15)

        signup_btn = ctk.CTkButton(
            frame,
            text="Create Account",
            width=250,
            height=45,
            command=self.open_signup
        )
        signup_btn.pack(pady=10)

    # -----------------------------------
    # Navigation
    # -----------------------------------

    def open_login(self):
        try:
            from pages.login import LoginPage

            self.clear_container()

            LoginPage(
                parent=self.container,
                app=self
            ).pack(fill="both", expand=True)

        except ModuleNotFoundError:
            self.show_placeholder(
                "Login Page not created yet."
            )

    def open_signup(self):
        try:
            from pages.signup import SignupPage

            self.clear_container()

            SignupPage(
                parent=self.container,
                app=self
            ).pack(fill="both", expand=True)

        except ModuleNotFoundError:
            self.show_placeholder(
                "Signup Page not created yet."
            )

    def open_dashboard(self):
        try:
            from pages.dashboard import DashboardPage

            self.clear_container()

            DashboardPage(
                parent=self.container,
                app=self
            ).pack(fill="both", expand=True)

        except ModuleNotFoundError:
            self.show_placeholder(
                "Dashboard Page not created yet."
            )

    def open_profile(self):
        try:
            from pages.profile import ProfilePage

            self.clear_container()

            ProfilePage(
                parent=self.container,
                app=self
            ).pack(fill="both", expand=True)

        except ModuleNotFoundError:
            self.show_placeholder(
                "Profile Page not created yet."
            )

    def logout(self):
        self.current_user = None
        self.show_welcome_screen()

    # -----------------------------------
    # Helper
    # -----------------------------------

    def show_placeholder(self, message):
        self.clear_container()

        frame = ctk.CTkFrame(self.container)
        frame.pack(fill="both", expand=True)

        ctk.CTkLabel(
            frame,
            text=message,
            font=("Arial", 22)
        ).pack(expand=True)

    # -----------------------------------
    # Session
    # -----------------------------------

    def login_success(self, user):
        self.current_user = user
        self.open_dashboard()

if __name__ == "__main__":
    print("CREATING APP")
    app = ChatHubApp()
    app.mainloop()