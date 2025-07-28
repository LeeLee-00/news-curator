import streamlit as st
import requests
import pandas as pd
from pydantic import BaseModel
import logging
from bs4 import BeautifulSoup


class SearchParamsRequest(BaseModel):
    search_type: str
    query_term: str
    time_span: str

def perform_query(search_params: SearchParamsRequest) -> list:
    """Perform a search query using the provided parameters."""
    try:
        response = requests.post("http://google_news_api:8527/search", json=search_params.dict())
        response.raise_for_status()
        return response.json().get("results", [])
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred during the request: {e}")
        st.error("An error occurred while fetching the results. Please try again later. Error: " + str(e))
        return []
    

def wrap_text(text, width):
    current_line = []
    lines = []
    for word in text.split(" "):
        current_line.append(word)
        if len(current_line) > width:
            lines.append(" ".join(current_line))
            current_line = []
    lines.append(" ".join(current_line))
    return "\n".join(lines)

def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    # del df["guid"]
    df['description'] = df['description'].apply(lambda x: BeautifulSoup(x, "html.parser").get_text() if pd.notnull(x) else x)
    df['description'] = df['description'].apply(lambda x: wrap_text(x, 40))
    df['pub_date'] = pd.to_datetime(df['pub_date'])
    df = df[["guid", "pub_date", "title", "description", "source", "link"]]
    # df = df.sort_values(by="pub_date", ascending=False, inplace=True)
    # reassign sort (drop inplace) so df stays a DataFrame
    df = df.sort_values(by="pub_date", ascending=False)   
    #df["title"] = st.text(df["title"].apply(lambda x: wrap_text(x, 40)))
    return df

def search_single_term(query_term: str, time_span: str, search_type: str) -> pd.DataFrame:
    """Search for a single term and return the results as a DataFrame."""

    if search_type == "Title":
        search_type = "allintitle"
    elif search_type == "Article Body":
        search_type = "allintext"
        
    if not query_term:
        st.warning("Please enter a query term.")
        return pd.DataFrame()

    search_params = SearchParamsRequest(
        search_type=search_type,
        query_term=query_term,
        time_span=time_span
    )
    results = perform_query(search_params)
    if results:
        df = pd.DataFrame(results)
        df = clean_df(df)
        return df
    else:
        st.write("No results found.")
        return pd.DataFrame()

def search_multiple(selected_terms: list, search_exclusivity: str, time_span: str, search_type: str) -> list:
    if search_exclusivity == "ALL":
        operator = "AND"
    else:
        operator = "OR"
    
    search_params = SearchParamsRequest(
        search_type = "allintitle" if search_type == "Title" else "allintext",
        query_term = f"%20{operator}%20".join(selected_terms),
        time_span = time_span,
    )

    return perform_query(search_params)
