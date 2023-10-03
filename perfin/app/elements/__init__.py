from collections import OrderedDict

from streamlit.runtime.state import SessionStateProxy

from perfin.app.elements.cards.card import Card  # noqa: F401
from perfin.app.elements.cards.kpi import KPI  # noqa: F401
from perfin.app.elements.dashboard import Dashboard  # noqa: F401
from perfin.app.elements.datagrid import DataGrid  # noqa: F401
from perfin.app.elements.plots.nivo.pie import Pie  # noqa: F401
from perfin.app.elements.plots.nivo.radar import Radar  # noqa: F401


def _set_elements():
    board = Dashboard()
    return OrderedDict(
        [
            ("dashboard", board),
            ("kpi_YTD_spend", KPI(board, 0, 0, 1, 2)),
            ("kpi_YTD_income", KPI(board, 1, 0, 1, 2)),
            ("kpi_YTD_savings", KPI(board, 2, 0, 1, 2)),
            ("kpi_MTD_spend", KPI(board, 3, 0, 1, 2)),
            ("pie", Pie(board, 6, 0, 6, 7, minW=3, minH=4)),
            ("radar", Radar(board, 12, 7, 3, 7, minW=2, minH=4)),
            ("card", Card(board, 6, 7, 3, 7, minW=2, minH=4)),
            ("data_grid", DataGrid(board, 6, 13, 6, 7, minH=4)),
        ]
    )


class DomWrapper:
    state_key = "dw"

    def __init__(self, elements: OrderedDict) -> None:
        self.elements: OrderedDict = elements

    @classmethod
    def init_if_missing(cls, state: SessionStateProxy, elements=_set_elements):
        if not state.get(cls.state_key):
            state[cls.state_key] = cls(
                elements=elements() if callable(elements) else elements
            )
            return state[cls.state_key]

    def populate_elements_from_db(self, user):
        # TODO: Add logic to fetch data from db
        # TODO: Add logic to filter data based on user
        pass

    def __getattr__(self, name):
        for element in self.elements:
            if element.name == name:
                return element

    def __getitem__(self, item):
        return self.elements[item]


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
