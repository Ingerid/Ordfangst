import streamlit as st
import pandas as pd
from io import BytesIO


@st.cache_data( show_spinner=False)
def data_to_excel(df: pd.DataFrame) -> BytesIO:
    """Make an excel object out of a dataframe as an IO-object"""
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Sheet1")
    processed_data = output.getvalue()
    return processed_data


def download_widget(data, word="ordfangst"):
    col1, col2 = st.columns(2)
    with col1:
        filename = st.text_input(
            "Filnavn for nedlasting", f"konkordanser_{word}.xlsx"
        )
    with col2:
        st.write("")
        if st.download_button(
            ":arrow_down: :gray[Last ned til excel]",
            data_to_excel(data),
            filename,
            help="Åpnes i Excel eller tilsvarende program",
        ):
            st.toast(f"Lagret til {filename}", icon="📥")



subheader = "Søk etter ord og ordformer i NBs samlinger" 
app_description ="""Med denne appen kan man søke etter deler av ord og ordformer i Nasjonalbibliotekets samlinger,
og se frekvenser, trendlinjer og kontekster hvor ordene opptrer."""
repo_url  ="https://github.com/Yoonsen/Ordfangst"
contact_url = "https://www.nb.no/dh-lab/kontakt/"
dhlab_url = "https://nb.no/dhlab/"
nb_logo = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" height="70px" width="250px" class="t2-icon t2-icon-logo" aria-hidden="true" focusable="false" alt="DH-lab"><path fill="black" d="M 4.9 7.8 C 5.5 7.8 6 7.3 6 6.7 C 6 6.1 5.5 5.7 4.9 5.7 C 4.3 5.7 3.8 6.2 3.8 6.8 C 3.8 7.3 4.3 7.8 4.9 7.8 Z M 15.7 23.7 C 16.3 23.7 16.8 23.2 16.8 22.6 C 16.8 22 16.3 21.5 15.7 21.5 C 15.1 21.5 14.6 22 14.6 22.6 C 14.6 23.3 15.1 23.7 15.7 23.7 Z M 7.6 0.3 L 7.6 20.1 L 20.2 20.1 L 20.2 0.3 L 7.6 0.3 Z M 10.3 7.8 C 9.7 7.8 9.2 7.3 9.2 6.7 C 9.2 6.1 9.7 5.6 10.3 5.6 C 10.9 5.6 11.4 6.1 11.4 6.7 C 11.4 7.3 10.9 7.8 10.3 7.8 Z M 15.6 18.4 C 15 18.4 14.5 17.9 14.5 17.3 C 14.5 16.7 15 16.2 15.6 16.2 C 16.2 16.2 16.7 16.7 16.7 17.3 C 16.7 17.9 16.2 18.4 15.6 18.4 Z M 15.6 13.1 C 15 13.1 14.5 12.6 14.5 12 C 14.5 11.4 15 10.9 15.6 10.9 C 16.2 10.9 16.7 11.4 16.7 12 C 16.7 12.6 16.2 13.1 15.6 13.1 Z M 15.6 7.8 C 15 7.8 14.5 7.3 14.5 6.7 C 14.5 6.1 15 5.6 15.6 5.6 C 16.2 5.6 16.7 6.1 16.7 6.7 C 16.7 7.3 16.2 7.8 15.6 7.8 Z"></path></svg>"""
dhlab_logo = "DHlab_logo_web_en_black.png"


contact_html =  f"""<a href="{contact_url}" target="_blank"><i style='font-size:15px; color: #262730;' class='fas'>&#xf0e0;</i></a>"""
#st.image(Image.open(dhlab_logo), width = 200, )


def header(app_title):
    col1, col2, col3 = st.columns([2, 1, 1])

    
    col1.title(app_title, help=app_description)
    col1.markdown(f"""<div style="display: flex; align-items: center; gap: 5px; margin-top: -20px;"><a href="{repo_url}" target="_blank">
        <i class="fa fa-github" aria-hidden="true"></i>""", unsafe_allow_html=True)
        
#        <i style='font-size:15px; color: #262730;' class='fab'>&#f09b;</i></a></div>""", unsafe_allow_html=True)
 #   col2.markdown(
#         f"""[![Repo](https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png)]({repo_url})""",
 #       unsafe_allow_html=True
  #  )
    
    col3.markdown(
        """<style>img {opacity: 0.9;}</style><a href="https://nb.no/dhlab">"""
        + nb_logo
        + "</a>",
        unsafe_allow_html=True,
    )
