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

sys.path.insert(0, '/resources/database_setup.py')

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
# Define global variables or constants
TITLE = "Passive and Active OSINT Toolbox"


# Define load_data function
@st.cache()  # This decorator ensures that this function is cached and that its result is reused across multiple page views
def load_data():
    data = datasets.load_iris()
    return pd.DataFrame(np.c_[data['data'], data['target']], columns=data['feature_names'] + ['target'])

# Define main function
# Define main function
def main():
    # Set title for your app
    st.title(TITLE)  # The text will appear in the web application header

    # Create an instance of writeToDB
    db_instance = writeToDB()

    # Now you can call the read_from_db method
    data = db_instance.read_from_db('your_table_name')

    df = load_data()  # Call the function to get our dataset

    # Displaying the dataset
    st.subheader('Iris Dataset')  # This will be displayed on the web page under the main title
    st.write(df)  # By default, this displays the first line of data and a "show more" button at the bottom for viewing all data

    # Add some explanatory text to our webpage
    st.markdown('This is a GUI for the Open Source Intelligence (OSINT) Toolbox. The toolbox is divided into two categories: passive and active OSINT. '
                'Passive OSINT involves collecting information without directly interacting with the target. Active OSINT involves interacting with the '
                'target to collect information. The toolbox is designed to help security professionals and ethical hackers gather information about a target.')
# Call main function
if __name__ == "__main__":
    main()