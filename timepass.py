import customtkinter as ctk

# Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("My Desktop App")
        self.geometry("1000x600")

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=200)
        self.sidebar.pack(side="left", fill="y")

        self.logo = ctk.CTkLabel(
            self.sidebar,
            text="My App",
            font=("Arial", 24, "bold")
        )
        self.logo.pack(pady=20)

        ctk.CTkButton(
            self.sidebar,
            text="Home",
            command=self.show_home
        ).pack(pady=10, padx=20, fill="x")

        ctk.CTkButton(
            self.sidebar,
            text="Profile",
            command=self.show_profile
        ).pack(pady=10, padx=20, fill="x")

        ctk.CTkButton(
            self.sidebar,
            text="Settings",
            command=self.show_settings
        ).pack(pady=10, padx=20, fill="x")

        # Main content
        self.content = ctk.CTkFrame(self)
        self.content.pack(side="right", fill="both", expand=True)

        self.show_home()

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_home(self):
        self.clear_content()

        ctk.CTkLabel(
            self.content,
            text="🏠 Home Page",
            font=("Arial", 28, "bold")
        ).pack(pady=30)

        ctk.CTkLabel(
            self.content,
            text="Welcome to your desktop application!"
        ).pack()

    def show_profile(self):
        self.clear_content()

        ctk.CTkLabel(
            self.content,
            text="👤 Profile",
            font=("Arial", 28, "bold")
        ).pack(pady=30)

        ctk.CTkEntry(
            self.content,
            placeholder_text="Enter Name"
        ).pack(pady=10)

        ctk.CTkEntry(
            self.content,
            placeholder_text="Enter Email"
        ).pack(pady=10)

        ctk.CTkButton(
            self.content,
            text="Save"
        ).pack(pady=20)

    def show_settings(self):
        self.clear_content()

        ctk.CTkLabel(
            self.content,
            text="⚙ Settings",
            font=("Arial", 28, "bold")
        ).pack(pady=30)

        ctk.CTkButton(
            self.content,
            text="Dark Mode",
            command=lambda: ctk.set_appearance_mode("dark")
        ).pack(pady=10)

        ctk.CTkButton(
            self.content,
            text="Light Mode",
            command=lambda: ctk.set_appearance_mode("light")
        ).pack(pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()
ctk.mainloop()