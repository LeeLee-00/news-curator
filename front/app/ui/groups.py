import streamlit as st
import pandas as pd
from services.groups import (
    load_groups, save_group, remove_articles, remove_group
)

def group_view_section(gen_results):
    st.subheader("Save & Manage Groups")
    # for each search result from search_section:
    for term, df in gen_results:
        with st.form(f"form_{term}"):
            sel = st.multiselect("Pick to save", df["title"].tolist())
            ex = ["<new>"] + list(load_groups().keys())
            choice = st.selectbox("Group", ex)
            grp = st.text_input("New Name", key=f"new_{term}") if choice=="<new>" else choice
            if st.form_submit_button("Save"):
                to_save = [df[df.title==s].iloc[0].to_dict() for s in sel]
                save_group(grp, to_save)
                st.success(f"Saved {len(to_save)} to {grp}")
    # manage existing groups
    st.subheader("View Saved Groups")
    grps = load_groups()
    if not grps:
        return
    g = st.selectbox("Pick Group", list(grps))
    dfg = pd.DataFrame(grps[g])
    dfg["pub_date"] = pd.to_datetime(dfg["pub_date"])
    st.dataframe(dfg)

    with st.form("rm"):
        rem = st.multiselect("Remove from group", dfg["title"].tolist())
        if st.form_submit_button("Remove"):
            cnt = remove_articles(g, rem)
            st.success(f"Removed {cnt}")
            st.rerun()

    if st.button("Delete Group"):
        remove_group(g)
        st.success(f"Deleted {g}")
        st.rerun()
