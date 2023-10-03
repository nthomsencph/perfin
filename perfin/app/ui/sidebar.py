from os import getcwd
from pathlib import Path

import streamlit as st


def init_sidebar(name: str) -> None:
    from perfin.app.auth.login import AUTH  # noqa: F811

    st.sidebar.title(":blue[Perfin]")
    st.sidebar.divider()
    st.sidebar.write(f"Welcome, {name}")
    AUTH.logout("Logout", "sidebar")  # Logout button

    with st.sidebar.expander("Guide"):
        try:
            st.write((Path(getcwd()) / "README.md").read_text())
        except FileNotFoundError:
            st.error("README.md not found.")
