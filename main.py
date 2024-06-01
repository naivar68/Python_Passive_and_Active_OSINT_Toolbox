# Import necessary modules
import subprocess
import pathlib
import hashlib
import binascii
from datetime import datetime
import streamlit as st
from sklearn import datasets
import numpy as np
import pandas as pd
import sys

# Import from resources
from resources import (
    DatabaseSetup,
    writeToDB,
    User,
    UserNotes,
    OpenPorts,
    runningServices,
    SubdomainFinder,
    Domain,
    EmailDiscovery,
    SocialMediaDiscovery,
    Charts,
    EndProgram
)

# Set the title of the application
TITLE = "Python OSINT Toolbox"


def display_file_content(file):
    content = file.read().decode("utf-8")
    st.subheader(f"Filename: {file.name}")
    st.code(content, language="python")


def button_clicks():
    button_style = """
    <style>
    div.stButton > button {
        width: 150px;
        height: 40px;
    }
    </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        if st.button("SignUp"):
            User()
    with col2:
        if st.button("Login"):
            User()
    with col3:
        if st.button("Forgot Password"):
            User()
    with col4:
        if st.button("Active OSINT"):
            pass
    with col5:
        if st.button("Passive OSINT"):
            pass
    with col6:
        if st.button("Exit"):
            EndProgram()


def main():
    st.title("Python OSINT Active and Passive Toolbox")

    # Display buttons horizontally
    button_clicks()

    # Descriptive text
    st.write("This is a Python OSINT toolbox that can be used for both passive and active OSINT operations. ")
    st.write("The toolbox is designed to be used by security researchers, penetration testers, and bug bounty hunters.")
    st.write("The toolbox is divided into two main sections: Passive OSINT and Active OSINT.")
    st.write(
        "The Passive OSINT section contains tools for collecting information about a target without directly interacting with the target.")
    st.write("The Active OSINT section contains tools for interacting with the target to collect information.")
    st.write("The toolbox is designed to be modular, so new tools can be easily added or removed.")
    st.write("The toolbox is also designed to be extensible, so new functionality can be easily added.")
    st.write(
        "The toolbox is built using the Streamlit framework, which allows for easy creation of web-based applications in Python.")
    st.write("The toolbox is open-source and can be freely used, modified, and distributed.")
    st.write("The toolbox is intended for educational and research purposes only. Use at your own risk.")
    st.write("The toolbox is provided as-is, with no warranties or guarantees of any kind.")
    st.write("The toolbox is not affiliated with any government agency or organization.")
    st.write("The toolbox is not intended for illegal or unethical activities.")
    st.write("The toolbox is not intended to be used for hacking or other malicious purposes.")

    # Display the sidebar
    st.sidebar.title(TITLE)
    st.sidebar.write("Welcome to the Python OSINT Toolbox.")
    st.sidebar.write("This toolbox is designed to help you collect information about a target.")

    # Buttons in the sidebar
    button_clicks()

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
