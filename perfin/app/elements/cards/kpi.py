from datetime import datetime

from streamlit_elements import mui

from perfin.app.elements.dashboard import Dashboard


class KPI(Dashboard.Item):
    def __call__(self, *, title, content):
        with mui.Card(
            key=self._key,
            sx={
                "display": "flex",
                "flexDirection": "column",
                "borderRadius": 3,
                "overflow": "hidden",
                "alignItems": "center",
                "boxSizing": "border-box",
            },
            elevation=1,
        ):
            mui.CardHeader(
                subheader=title,
            )

            with mui.CardContent(sx={"flex": 1}):
                mui.Typography(
                    content,
                    sx={
                        # increase font size
                        "fontSize": 24,
                        # center text
                        "display": "flex",
                    },
                )
