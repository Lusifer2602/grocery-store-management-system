import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font

# Utility functions for styling
def style_fonts():
    heading_font = Font(family='Helvetica', size=24, weight='bold')
    button_font = Font(family='Helvetica', size=16, weight='bold')
    label_font = Font(family='Helvetica', size=12)
    return heading_font, button_font, label_font

# Main Application Class
class GroceryManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Grocery Management System")
        self.geometry("800x600")
        self.resizable(False, False)

        # Styles
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.bg_color = "#f0f4f8"
        self.primary_color = "#4a90e2"
        self.accent_color = "#50e3c2"
        self.bold_font, self.btn_font, self.lbl_font = style_fonts()

        self.configure(bg=self.bg_color)

        # Container for frames
        self.container = ttk.Frame(self)
        self.container.pack(fill='both', expand=True)

        # Dictionary for frames
        self.frames = {}

        # Initialize all frames
        for F in (MainMenu, AdminLoginPage, AdminDashboard, SignInPage, SignInConfirmPage, LoginPage):
            frame = F(parent=self.container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(MainMenu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# Main Menu Frame
class MainMenu(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(style='My.TFrame')

        # Banner
        banner = ttk.Label(self, text="Grocery Management System", anchor='center', style='Banner.TLabel')
        banner['font'] = (controller.bold_font, 26)
        banner.pack(pady=20)

        # Welcome Text
        welcome = ttk.Label(self, text="Welcome! Please select an option below.", style='SubTitle.TLabel')
        welcome['font'] = (controller.lbl_font, 14)
        welcome.pack(pady=10)

        # Buttons
        btn_style = ttk.Style()
        btn_style.configure('Large.TButton', font=controller.btn_font, padding=15, background=controller.primary_color)
        buttons_info = [
            ("Admin Login", lambda: controller.show_frame(AdminLoginPage)),
            ("Sign In", lambda: controller.show_frame(SignInPage)),
            ("Log In", lambda: controller.show_frame(LoginPage)),
            ("Exit", self.exit_app)
        ]

        for text, command in buttons_info:
            btn = ttk.Button(self, text=text, style='Large.TButton', command=command)
            btn.pack(pady=10, fill='x', padx=100)

    def exit_app(self):
        self.controller.destroy()

# Admin Login Page
class AdminLoginPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(style='My.TFrame')

        # Title
        title = ttk.Label(self, text="Admin Login", style='Banner.TLabel')
        title['font'] = (controller.bold_font, 22)
        title.pack(pady=20)

        # ID
        id_label = ttk.Label(self, text="Admin ID:", style='SubTitle.TLabel')
        id_label.pack(pady=5)
        self.id_entry = ttk.Entry(self, width=30)
        self.id_entry.pack(pady=5)

        # Password
        pwd_label = ttk.Label(self, text="Password:", style='SubTitle.TLabel')
        pwd_label.pack(pady=5)
        self.pwd_entry = ttk.Entry(self, width=30, show='*')
        self.pwd_entry.pack(pady=5)

        # Buttons
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=20)

        login_btn = ttk.Button(btn_frame, text="Login", command=self.check_admin_credentials)
        back_btn = ttk.Button(btn_frame, text="Back", command=lambda: controller.show_frame(MainMenu))
        login_btn.grid(row=0, column=0, padx=10)
        back_btn.grid(row=0, column=1, padx=10)

    def check_admin_credentials(self):
        admin_id = self.id_entry.get().strip()
        password = self.pwd_entry.get().strip()
        if admin_id == "abc" and password == "2345":
            self.controller.show_frame(AdminDashboard)
        else:
            messagebox.showerror("Error", "Invalid ID or Password!")

# Admin Dashboard
class AdminDashboard(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(style='My.TFrame')

        # Heading
        heading = ttk.Label(self, text="Admin Panel", style='Banner.TLabel')
        heading['font'] = (controller.bold_font, 24)
        heading.pack(pady=20)

        # Buttons
        btn_style = ttk.Style()
        btn_style.configure('Large.TButton', font=controller.btn_font, padding=15)
        btns = [
            ("View Users list", self.view_users),
            ("Remove User", self.remove_user),
            ("Items List", self.items_list),
            ("View Bills history", self.view_bills),
            ("Back to Main Menu", lambda: controller.show_frame(MainMenu))
        ]

        for text, cmd in btns:
            btn = ttk.Button(self, text=text, style='Large.TButton', command=cmd)
            btn.pack(pady=10, fill='x', padx=150)

    def view_users(self):
        messagebox.showinfo("Users List", "Feature coming soon!")

    def remove_user(self):
        messagebox.showinfo("Remove User", "Feature coming soon!")

    def items_list(self):
        messagebox.showinfo("Items List", "Feature coming soon!")

    def view_bills(self):
        messagebox.showinfo("Bills History", "Feature coming soon!")

# Sign In (Registration) Page
class SignInPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(style='My.TFrame')

        # Title
        title = ttk.Label(self, text="Sign In - New User Registration", style='Banner.TLabel')
        title['font'] = (controller.bold_font, 20)
        title.pack(pady=20)

        # Form Fields
        form_frame = ttk.Frame(self)
        form_frame.pack(pady=10, padx=50, fill='x')

        ttk.Label(form_frame, text="Name:", style='SubTitle.TLabel').grid(row=0, column=0, sticky='w', pady=5)
        self.name_entry = ttk.Entry(form_frame, width=40)
        self.name_entry.grid(row=0, column=1, pady=5, sticky='w')

        ttk.Label(form_frame, text="Email:", style='SubTitle.TLabel').grid(row=1, column=0, sticky='w', pady=5)
        self.email_entry = ttk.Entry(form_frame, width=40)
        self.email_entry.grid(row=1, column=1, pady=5, sticky='w')

        ttk.Label(form_frame, text="Password:", style='SubTitle.TLabel').grid(row=2, column=0, sticky='w', pady=5)
        self.pwd_entry = ttk.Entry(form_frame, width=40, show='*')
        self.pwd_entry.grid(row=2, column=1, pady=5, sticky='w')

        # Buttons
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=20)

        submit_btn = ttk.Button(btn_frame, text="Register", command=self.validate_registration)
        back_btn = ttk.Button(btn_frame, text="Back", command=lambda: controller.show_frame(MainMenu))
        submit_btn.grid(row=0, column=0, padx=10)
        back_btn.grid(row=0, column=1, padx=10)

    def validate_registration(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        pwd = self.pwd_entry.get().strip()
        if not name:
            messagebox.showwarning("Input Error", "Please enter your name.")
            return
        if not email.endswith("@gmail.com") or email == "@gmail.com":
            messagebox.showwarning("Input Error", "Please enter a valid Gmail address.")
            return
        if len(pwd) < 8:
            messagebox.showwarning("Input Error", "Password must be at least 8 characters.")
            return
        # Show confirmation page
        self.controller.frames[SignInConfirmPage].set_info(name, email, pwd)
        self.controller.show_frame(SignInConfirmPage)

# Sign In Confirmation Page
class SignInConfirmPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(style='My.TFrame')

        self.info_vars = {}
        self.info_vars['Name'] = tk.StringVar()
        self.info_vars['Email'] = tk.StringVar()
        self.info_vars['Password'] = tk.StringVar()

        title = ttk.Label(self, text="Confirm Your Details", style='Banner.TLabel')
        title['font'] = (controller.bold_font, 20)
        title.pack(pady=20)

        info_frame = ttk.Frame(self)
        info_frame.pack(pady=10)

        ttk.Label(info_frame, text="Name:", style='SubTitle.TLabel').grid(row=0, column=0, sticky='e', pady=5)
        ttk.Label(info_frame, textvariable=self.info_vars['Name'], style='SubTitle.TLabel').grid(row=0, column=1, sticky='w', pady=5)

        ttk.Label(info_frame, text="Email:", style='SubTitle.TLabel').grid(row=1, column=0, sticky='e', pady=5)
        ttk.Label(info_frame, textvariable=self.info_vars['Email'], style='SubTitle.TLabel').grid(row=1, column=1, sticky='w', pady=5)

        ttk.Label(info_frame, text="Password:", style='SubTitle.TLabel').grid(row=2, column=0, sticky='e', pady=5)
        ttk.Label(info_frame, textvariable=self.info_vars['Password'], style='SubTitle.TLabel').grid(row=2, column=1, sticky='w', pady=5)

        # Buttons
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=20)
        confirm_btn = ttk.Button(btn_frame, text="✅ Confirm", command=self.confirm_registration)
        edit_btn = ttk.Button(btn_frame, text="🔄 Edit", command=lambda: self.controller.show_frame(SignInPage))
        confirm_btn.grid(row=0, column=0, padx=10)
        edit_btn.grid(row=0, column=1, padx=10)

    def set_info(self, name, email, pwd):
        self.info_vars['Name'].set(name)
        self.info_vars['Email'].set(email)
        self.info_vars['Password'].set(pwd)

    def confirm_registration(self):
        # Ideally, save user info here
        messagebox.showinfo("Success", "Registration successful!")
        self.controller.show_frame(MainMenu)

# Log In Page
class LoginPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(style='My.TFrame')

        # Title
        title = ttk.Label(self, text="User Login", style='Banner.TLabel')
        title['font'] = (controller.bold_font, 22)
        title.pack(pady=20)

        # Form
        form_frame = ttk.Frame(self)
        form_frame.pack(pady=10, padx=50, fill='x')

        ttk.Label(form_frame, text="Email:", style='SubTitle.TLabel').grid(row=0, column=0, sticky='w', pady=5)
        self.email_entry = ttk.Entry(form_frame, width=40)
        self.email_entry.grid(row=0, column=1, pady=5)

        ttk.Label(form_frame, text="Password:", style='SubTitle.TLabel').grid(row=1, column=0, sticky='w', pady=5)
        self.pwd_entry = ttk.Entry(form_frame, width=40, show='*')
        self.pwd_entry.grid(row=1, column=1, pady=5)

        # Buttons
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=20)
        login_btn = ttk.Button(btn_frame, text="Log In", command=self.login_user)
        back_btn = ttk.Button(btn_frame, text="Back", command=lambda: controller.show_frame(MainMenu))
        login_btn.grid(row=0, column=0, padx=10)
        back_btn.grid(row=0, column=1, padx=10)

    def login_user(self):
        email = self.email_entry.get().strip()
        password = self.pwd_entry.get().strip()
        # For demo: Always success, in real app, validate against stored users.
        if email and password:
            messagebox.showinfo("Welcome", "Welcome Back!")
            # Proceed to user dashboard or main app
        else:
            messagebox.showwarning("Error", "Please enter email and password.")

# Initialize style for banner and subtitles
def setup_styles(app):
    style = app.style
    style.configure('TFrame', background=app.bg_color)
    style.configure('Banner.TLabel', background=app.bg_color, foreground=app.primary_color)
    style.configure('SubTitle.TLabel', background=app.bg_color, foreground='black')
    style.map('Large.TButton', background=[('active', app.accent_color)])

# Run the app
if __name__ == "__main__":
    app = GroceryManagementApp()
    setup_styles(app)
    app.mainloop()
