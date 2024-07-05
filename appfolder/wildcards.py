
import streamlit as st
import dhlab.api.dhlab_api as api
import dhlab as dh 
from utils import header, download_widget, nb_logo


# TODO: Add standard app header with logo + links + info
st.set_page_config(page_title="Ordfangst", layout="wide", initial_sidebar_state="auto", menu_items=None,  page_icon='*️⃣')
st.session_state.update(st.session_state)

st.html(body = """<style> body * {font-family:'DM Sans'}</style>""")

header("Ordfangst")

word = st.text_input("Søkeord", placeholder="Angi søkeuttrykk med *", help="Sett * hvor som helst i ordet og så mange ganger det er passende. Pass bare på at et ord ikke kan ha * i både start og slutt. En av endene må ha et annet tegn")

with st.expander("Innstillinger"):
    freqlimcol, limcol = st.columns([1,1])

#factor = factorcol.number_input("Matchlengde", min_value=-10, value=2, help="Tallet som skrives inn her legges til lengden på ordet, målt i antall tegn inkludert * og bokstaver. Små tall vil typisk lage bøyningsparadigmer, mens store tall gir sammensetninger. Angivelsen kan også være negativ, men ikke mindre enn minus antall * i søkeuttrykket")
freqlim = freqlimcol.number_input("Laveste frekvensverdi",min_value=1, value=10)
limit = limcol.number_input("Resultatstørrelse", min_value=5, value=1000)

df = api.wildcard_search(word, factor=50, freq_limit=freqlim, limit=limit).reset_index(names=["Ord"]).rename(columns={"freq":"Frekvens"})

data = df.sort_values(by="Frekvens", ascending=False)
data["choice"] = False

data_col, viz_col = st.columns([2,2])

options = data_col.data_editor(
    data, 
    column_config={
        "choice": st.column_config.CheckboxColumn(
            "Velg",
            help = "Velg ord du vil undersøke nærmere med trendlinjer og konkordanser",
            #default=False,
        ),
    },
    hide_index=True,
)

chosen = options[options.choice].Ord.tolist()


def ngram_widget(words, container): 
    """Plot N-gram trendlines for chosen words"""
    from_year, to_year = viz_col.select_slider("Årstall", options=list(range(1800, 2025, 1)), value=(1800, 2024))
    lines = dh.Ngram(words, from_year=from_year, to_year=to_year).frame
    container.line_chart(lines)

def concordance_widget(words, container):
    """Fetch concordances for the chosen words"""
    concs = api.concordance(words=words, window=25, limit=1000)    
    container.dataframe(concs)


chosen_visualisation = viz_col.selectbox("Velg visualisering", ["N-gram", "Konkordanser"])

if chosen_visualisation == "N-gram":
    ngram_widget(chosen, viz_col)
elif chosen_visualisation == "Konkordanser":
    concordance_widget(chosen, viz_col)
    

concs = api.concordance(words=chosen, window=25, limit=100)

st.dataframe(concs.frame)

download_widget(concs, word="_".join(chosen) if isinstance(chosen, list) else chosen)

