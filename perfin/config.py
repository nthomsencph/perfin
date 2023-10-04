from pathlib import Path

_menu_items = {
    "Get Help": "https://www.github.com/nthomsencph/perfin",
    "Report a bug": "https://www.github.com/nthomsencph/perfin/issues",
    "About": "# Personal finance made easy. Perfin enables you to track your expenses and income, and visualize your spending habits.",
}

ST_PAGE_CONFIG = {
    "page_icon": "💰",
    "page_title": "Perfin - Personal Finance",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
    "menu_items": {
        "Get Help": "https://www.github.com/nthomsencph/perfin",
        "Report a bug": "https://www.github.com/nthomsencph/perfin/issues",
        "About": "# Personal finance made easy. Perfin enables you to track your expenses and income, and visualize your spending habits.",
    },
}

_db_path = "db/perfin.db"
DB_URL = f"sqlite:///{_db_path}"

DB_ECHO = True

COOKIE = {
    "expiry_days": 30,
    "key": "random_signature_key",
    "name": "random_cookie_name",
}

PRE_AUTHORIZED = {"emails": []}

from configparser import ConfigParser

config = ConfigParser()
config.read("config.cfg")

API_KEY = config["LANGCHAIN"]["API_KEY"]
