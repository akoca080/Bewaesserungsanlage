import streamlit as st
from streamlit_option_menu import option_menu
from UI import Startseite as start
from UI import SensorDaten as sens


#Navigationsleiste inklusice CSS Code von Streamlit.com 
#https://docs.streamlit.io/develop/concepts/configuration/theming

if "Seite" not in st.session_state:
    st.session_state["Seite"] = "Startseite"

def main():
    st.set_page_config(layout="wide")

    st.markdown(
        """
        <style>
        .stApp {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
        }
        .block-container {
            max-width: 1400px;  /* Setze die Breite nach Bedarf */
            margin: 0px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    menu_options = ["Startseite", "Sensordaten"]
    
    option = option_menu(
        menu_title="",
        options=menu_options,
        icons=["house", "tools", "search", "play-circle", "bar-chart", "download"],
        menu_icon="cast", 
        default_index=menu_options.index(st.session_state["Seite"]),
        orientation="horizontal",
        styles={
            "container": {"padding": "5px", "background-color": "#1e1e1e"},
            "icon": {"color": "white", "font-size": "24px"},
            "nav-link": {
                "font-size": "14px",
                "color": "white",
                "text-align": "center",
                "margin": "0px",
                "padding": "10px",
                "flex-direction": "column",
                "display": "flex",
                "align-items": "center",
                "justify-content": "center",
            },
            "nav-link-selected": {
                "background-color": "#444",
                "font-weight": "bold",
                "border-radius": "10px",
            },
        }
    )

    if option != st.session_state["Seite"]:
        st.session_state["Seite"] = option
        st.rerun()

    with st.container():
        st.markdown('<div class="block-container">', unsafe_allow_html=True)

        if st.session_state["Seite"] == "Startseite":
            start.startseite()
        elif st.session_state["Seite"] == "Validation":
            sens.Sensor_Daten()


        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
