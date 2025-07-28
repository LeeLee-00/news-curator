import streamlit as st
import pandas as pd
from search_logic import search_single_term

TIME_SPANS = ["12h", "1d", "7d", "30d", "100d"]

def search_section(terms: list[str], session_state):
    st.subheader("Search News")
    ts = st.selectbox("Time Span", TIME_SPANS)
    typ = st.selectbox("Search In", ["Title","Article Body"])
    if "results" not in session_state:
        session_state.results = {}
    for t in terms:
        if st.button(t, key=f"src_{t}"):
            df = search_single_term(t, ts, typ)
            session_state.results = {t: df}
    for term, df in session_state.results.items():
        if df is not None and not df.empty:
            st.write(f"Results for {term}")
            st.dataframe(df)
            yield term, df
