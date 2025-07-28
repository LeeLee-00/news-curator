import streamlit as st
from ui.terms import term_manager
from ui.search import search_section
from ui.groups import group_view_section

def main():
    st.set_page_config(layout="wide")
    # Flash messages… (same as before)

    st.title("News Search Interface")
    terms = term_manager()

    # capture the generator of search results
    results = list(search_section(terms, st.session_state))

    # hand that generator to the groups UI
    group_view_section(results)

if __name__ == "__main__":
    main()
