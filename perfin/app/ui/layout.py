from streamlit_elements import dashboard

LAYOUT = [
    # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
    dashboard.Item("year-to-date-growth", 0, 0, 1, 1),
    dashboard.Item("avg_monthly_spend", 1, 0, 1, 1),
    dashboard.Item("avg_daily_spend", 2, 0, 1, 1),
    dashboard.Item(
        "radar_chart",
        0,
        1,
        4,
        2,
    ),
    # dashboard.Item("fifth_item",            0, 2, 2, 2,),
    # dashboard.Item("sixth_item",            3, 2, 1, 1,),
]
