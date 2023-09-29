import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

from perfin.app.models import User

with open("perfin/app/auth/users.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

AUTH = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["preauthorized"],
)


def authenticate():
    """Authenticate user and return user object if successful"""

    try:
        name, auth_status, username = AUTH.login("Login", "main")
        user = User(name=name, auth_status=auth_status, username=username)

        if user.auth_status == False:
            st.error("Username/password is incorrect")

        elif user.auth_status == None:
            st.warning("Please enter your username and password")

        else:
            return user  # Return user object if successful

    except KeyError as _:
        """Raised when authentication isn't found in session state.
        Weird library bug, but this is a workaround"""
        return False
