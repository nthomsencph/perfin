# import streamlit as st
# from pathlib import Path


# class Stylesheet:

#     @classmethod
#     def __repr__(cls):
#         return cls.load_css()

#     @st.cache
#     @classmethod
#     def load_css(clss):
#         with Path("perfin/app/ui/stylesheets.css").open("r") as f:
#             return f'<style>{f.read()}</style>'


# st.markdown(Stylesheet, unsafe_allow_html=True)
