
import streamlit as st


pg = st.navigation([
    st.Page("wildcards.py", title="Ordfangst", icon='*️⃣'),
    #st.Page("ngram_day.py", title="N-gram", icon=":material/favorite:"),
])

pg.run()

