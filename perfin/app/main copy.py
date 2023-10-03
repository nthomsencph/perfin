import streamlit as st
from streamlit import session_state as state
from streamlit_elements import elements

from perfin.app.auth import authenticate
from perfin.app.elements import DomWrapper
from perfin.app.ui.sidebar import init_sidebar


def main():
    if user := authenticate():
        # initialize sidebar
        init_sidebar(user.name)

        # if DomWrapper not in state, create it
        #  and populate it's elements from db
        if dw := DomWrapper.init_if_missing(state):
            dw.populate_elements_from_db(user)  # NOTE: this is not implemented yet
        else:
            # if dw exists, simply retrieve it from state
            dw = state.get(DomWrapper.state_key)

        # initialize dashboard
        with elements("dashboard"):
            with dw["dashboard"](rowHeight=57):
                dw["kpi_YTD_spend"](
                    title="YTD Spend",
                    content="100.000",
                )
                dw["kpi_YTD_income"](
                    title="YTD Income",
                    content="200.000",
                )
                dw["kpi_YTD_savings"](
                    title="YTD Savings",
                    content="100.000",
                )
                dw["kpi_MTD_spend"](
                    title="MTD Spend",
                    content="10.000",
                )
                dw["pie"]()
                dw["radar"]()
                dw["card"]()
                dw["data_grid"]()


if __name__ == "__main__":
    # st.set_page_config(
    #     page_icon= "💰",
    #     page_title= "Perfin - Personal Finance",
    #     layout= "wide",
    #     initial_sidebar_state= "expanded",
    #     menu_items= {
    #         'Get Help': 'https://www.github.com/nthomsencph/perfin',
    #         'Report a bug': "https://www.github.com/nthomsencph/perfin/issues",
    #         'About': "# Personal finance made easy. Perfin enables you to track your expenses and income, and visualize your spending habits."
    #     }
    # )
    main()
