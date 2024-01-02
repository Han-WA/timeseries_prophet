import streamlit as st
from streamlit_option_menu import option_menu

import about, prop, dsgn, proj

st.set_page_config(
    page_title = "Dashboard"
)

class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title" : title,
            "function" : function
        })

    def run():
        with st.sidebar:
            app = option_menu(
            menu_title = "Stock Price Prediction", 
            options = ["About Project","Data Overview", "Project Design","Prophet Model Test"],
            icons = ["bookmark-star-fill","clipboard2-fill","gear-wide-connected", "graph-up-arrow"],
            menu_icon = "grid-fill",
        )
        if app == "About Project":
            proj.app()
        if app == "Data Overview":
            about.app()
        if app == "Prophet Model Test":
            prop.app()
        if app == "Project Design":
            dsgn.app()
    
    run()