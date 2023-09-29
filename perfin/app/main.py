import json
from pathlib import Path
from types import SimpleNamespace

import streamlit as st
from streamlit import session_state as state
from streamlit_elements import dashboard, elements, event, mui, sync

from perfin.app.auth.login import AUTH, authenticate
from perfin.app.elements import Card, Dashboard, DataGrid, Pie, Radar
from perfin.app.ui.layout import LAYOUT


def handle_layout_change(updated_layout):
    # You can save the layout in a file, or do anything you want with it.
    # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
    print(updated_layout)  # noqa


def main():
    if user := authenticate():
        ############
        # Sidebar
        ############

        st.sidebar.title("Perfin")
        st.sidebar.divider()
        st.sidebar.write(f"Welcome, {user.name}")
        AUTH.logout("Logout", "sidebar")  # Logout button

        ############

        with elements("dashboard"):
            ############
            # Dashboard
            ############

            with dashboard.Grid(LAYOUT, onLayoutChange=handle_layout_change):
                mui.Paper("YTD ⬆️ (%)", key="year_to_date-growth")
                mui.Paper("Avg. Monthly spend 💸", key="avg_monthly_spend")
                mui.Paper("fifth item (cannot drag)", key="fifth_item")
                mui.Paper("sixth item (cannot resize)", key="sixth_item")

        with st.sidebar.expander("Guide"):
            st.write((Path(__file__).parent.parent / "README.md").read_text())

        st.title("")

        if "w" not in state:
            board = Dashboard()
            w = SimpleNamespace(
                dashboard=board,
                pie=Pie(board, 6, 0, 6, 7, minW=3, minH=4),
                radar=Radar(board, 12, 7, 3, 7, minW=2, minH=4),
                card=Card(board, 6, 7, 3, 7, minW=2, minH=4),
                data_grid=DataGrid(board, 6, 13, 6, 7, minH=4),
            )
            state.w = w

            w.editor.add_tab("Card content", Card.DEFAULT_CONTENT, "plaintext")
            w.editor.add_tab(
                "Data grid", json.dumps(DataGrid.DEFAULT_ROWS, indent=2), "json"
            )
            w.editor.add_tab(
                "Radar chart", json.dumps(Radar.DEFAULT_DATA, indent=2), "json"
            )
            w.editor.add_tab(
                "Pie chart", json.dumps(Pie.DEFAULT_DATA, indent=2), "json"
            )
        else:
            w = state.w

        with elements("demo"):
            event.Hotkey("ctrl+s", sync(), bindInputs=True, overrideDefault=True)

            with w.dashboard(rowHeight=57):
                w.pie(w.editor.get_content("Pie chart"))
                w.radar(w.editor.get_content("Radar chart"))
                w.card(w.editor.get_content("Card content"))
                w.data_grid(w.editor.get_content("Data grid"))


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()
