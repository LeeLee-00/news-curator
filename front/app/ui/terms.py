import streamlit as st
import logging
from services.terms import load_terms, save_terms

def term_manager() -> list[str]:
    terms = load_terms()
    q = st.text_input("Enter Query Term")
    if st.button("Add Query Term"):
        t = q.upper().strip()
        if t and t not in terms:
            terms.append(t); save_terms(terms)
            st.success(f"Added '{t}'"); logging.info(f"Added term {t}")
        elif not t:
            st.error("Cannot add empty")
    st.subheader("Manage Terms")
    for t in terms:
        c1, c2 = st.columns([4,1])
        with c1:
            st.write(f"• {t}")
        with c2:
            if st.button("Delete", key=f"del_{t}"):
                terms.remove(t)
                save_terms(terms)
                st.success(f"Deleted '{t}'")
                st.rerun()
    return terms
