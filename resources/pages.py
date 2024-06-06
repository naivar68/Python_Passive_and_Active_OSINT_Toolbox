import streamlit as st
from resources.database_setup import User, CreateFolders



# Set the page layout to wide mode


# Rest of your code...
class Pages:
    def __init__(self, placeholder):
        self.placeholder = placeholder
        self.pages = {
            "signup": self.signup_page,
            "login": self.login_page,
            "forgot_password": self.forgot_password_page,
            "success": self.success_page,
            "failure": self.failure_page,
            "active_osint": self.active_osint_page,
            "passive_osint": self.passive_osint_page,
            "exit": self.exit_page,
            "user_profile": self.user_profile_page,
            "settings": self.settings_page,
            "help": self.help_page,
            "contact_us": self.contact_us_page,
            "reports": self.reports_page
        }
        self.active_page = None





    def home_page(self):
        main()
        # Add your home page content here
    def signup_page(self):
        self.active_page = "signup"
        st.title("SignUp Page")
        st.write("Welcome to the SignUp Page")
        st.button("Go Home", )
        with st.form("signup_form"):
            username = st.text_input("Username", max_chars=20)
            password = st.text_input("Password", type="password")
            st.empty()  # This creates a space before the submit button

            submit = st.form_submit_button("Submit")

            if submit:
                with st.spinner("Creating user..."):
                    self.DataBaseSetup()
                    self.User.signup(username, password)
                    self.DataBaseSetup.create_tables()
                    self.DataBaseSetup.CreateFolders(username)
                    self.Pages.success_page(self)



                # st.write(f"Username: {username}")
                # st.write(f"Password: {password}")
                # user = User(username, password)
                # user.signup(self)
                # CreateFolders(username)
                # st.switch_page
                # st.write("User created successfully")

            else:
                st.stop()

    def success_page(self):
        st.active_page = "success"

        st.write("User created successfully")
        st.write("Folders and database entries created successfully")
        st.empty()
        st.button("Go Home", self.home_page)

    def failure_page(self):
        st.active_page = "failure"
        st.title("Failure Page")
        st.write("User already exists")
        st.empty()
        st.button("Go Home", self.home_page)


    def login_page(self):
        st.title("Login Page")
        # Add your login page content here


    def forgot_password_page(self):
        st.title("Forgot Password Page")
        # Add your forgot password page content here


    def active_osint_page(self):
        st.title("Active OSINT Page")
        # Add your active OSINT page content here


    def passive_osint_page(self):
        st.title("Passive OSINT Page")

    # Add your passive OSINT page content here
    # Existing code...

    def user_profile_page(self):
        st.title("User Profile Page")
        # Add your user profile page content here

    def settings_page(self):
        st.title("Settings Page")
        # Add your settings page content here

    def help_page(self):
        st.title("Help Page")
        # Add your help page content here

    def contact_us_page(self):
        st.title("Contact Us Page")
        # Add your contact us page content here

    def reports_page(self):
        st.title("Reports Page")
        # Add your reports page content here

    def exit_page(self):
        st.title("Exit Page")
        # Add your exit page content here

    def __call__(self, page):
        self.active_page = self.pages.get(page)
        if self.active_page:
            self.active_page()
        else:
            st.title("404 Page Not Found")
            st.write("The page you are looking for does not exist")
            st.button("Go Home", self.home_page)
            st.stop()




