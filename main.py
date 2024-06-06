# Import necessary modules
import streamlit as st

# Import from resources
from resources import EndProgram, Pages

# Set the title of the application
TITLE = "Python OSINT Toolbox"

button_style = """
<style>
    .stButton>button {
        color: white;
        background-color: #1E90FF;
        border-color: #1E90FF;
    }
</style>
"""


st.set_page_config(layout="wide")



st.markdown(button_style, unsafe_allow_html=True)



# Define the button clicks


def button_clicks(page_placeholder):

    pages = Pages(page_placeholder)

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        if st.button("SignUp"):
            pages.signup_page()

        if st.button("Login"):
            pages.login_page()

        if st.button("Forgot Password"):
            pages.forgot_password_page()



    with col2:
        if st.button("User Profile"):
            pages.user_profile_page()

        if st.button("Help"):
            pages.help_page()


    with col3:
        if st.button("Active OSINT"):
            pages.active_osint_page()

        if st.button("Passive OSINT"):
            pages.passive_osint_page()


    with col4:
        if st.button("Logout"):
            pages.exit_page()

        if st.button("Settings"):
            pages.settings_page()


    with col5:
        if st.button("Contact Us"):
            pages.contact_us_page()

        if st.button("Reports"):
            pages.reports_page()



    with col6:
        if st.button("Exit"):
            EndProgram()

def main():
    st.title("Python OSINT Active and Passive Toolbox")

    page_placeholder = st.empty()

    button_clicks(page_placeholder)




    # Descriptive text
    st.subheader("Welcome to the Python OSINT Toolbox")
    st.write("This is a Python OSINT toolbox that can be used for both passive and active OSINT operations. ")
    st.write("The toolbox is designed to be used by security researchers, penetration testers, and bug bounty hunters.")
    st.write("The toolbox is divided into two main sections: Passive OSINT and Active OSINT.")

    st.write("The toolbox is intended for educational and research purposes only. Use at your own risk.")
    st.write("The toolbox is provided as-is, with no warranties or guarantees of any kind.")
    st.write("The toolbox is not affiliated with any government agency or organization.")
    st.empty()
    # Display the sidebar
    st.sidebar.title(TITLE)
    st.sidebar.write("Welcome to the Python OSINT Toolbox.")
    st.sidebar.write("This toolbox is designed to help you collect information about a target.")
    st.sidebar.write("The Passive OSINT section contains tools for collecting information about a target without directly interacting with the target.")
    st.sidebar.write("The Active OSINT section contains tools for interacting with the target to collect information.")
    st.sidebar.write("Things are designed to be modular, so new tools can be easily added or removed.")
    st.sidebar.write("A work in progress, POAPT is also designed to be extensible, so new functionality can be easily added.")
    st.sidebar.write("POAPT is built using the Streamlit framework, which allows for easy creation of web-based applications in "
             "Python.")
    st.sidebar.write("The toolbox is open-source and can be freely used, modified, and distributed.")
    st.empty()
    uploaded_files = st.file_uploader("Choose Python files", type=["py"], accept_multiple_files=True)

    if uploaded_files:
        for uploaded_file in uploaded_files:
            display_file_content(uploaded_file)

            # Example operation: Check if the file contains a specific function or class
            if st.checkbox(f"Check for main() in {uploaded_file.name}"):
                if "def main(" in uploaded_file.getvalue().decode("utf-8"):
                    st.write(f"`main()` function found in {uploaded_file.name}")
                else:
                    st.write(f"`main()` function not found in {uploaded_file.name}")


if __name__ == "__main__":
    main()
