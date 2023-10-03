import streamlit as st
import streamlit_authenticator as stauth

from db.crud import UserCRUD
from perfin.app.models import User
from perfin.config import COOKIE, PRE_AUTHORIZED

AUTH = stauth.Authenticate(
    credentials=UserCRUD.retrive_users_for_auth(),
    cookie_name=COOKIE["name"],
    key=COOKIE["key"],
    cookie_expiry_days=COOKIE["expiry_days"],
    preauthorized=PRE_AUTHORIZED["emails"],
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
