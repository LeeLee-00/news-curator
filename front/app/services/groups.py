import json, logging
from pathlib import Path
import streamlit as st  # Assuming Streamlit is being used

GROUPS_FILE = Path("shared_models/articles.json")

def load_groups() -> dict[str, list[dict]]:
    logging.info("Loading groups from file.")
    if not GROUPS_FILE.exists():
        logging.warning(f"Groups file {GROUPS_FILE} does not exist.")
        return {}
    try:
        raw = GROUPS_FILE.read_text().strip()
        logging.info("Groups loaded successfully.")
        return json.loads(raw) if raw else {}
    except Exception as e:
        logging.error(f"Error loading groups: {e}")
        return {}

def save_group(name: str, articles: list[dict]):
    logging.info(f"Saving group '{name}' with {len(articles)} articles.")
    groups = load_groups()
    bucket = groups.get(name, [])
    links = {a["link"] for a in bucket}
    for art in articles:
        # coerce Timestamp → str
        art = art.copy()
        pub = art.get("pub_date")
        if hasattr(pub, "isoformat"):
            art["pub_date"] = pub.isoformat()
        if art["link"] not in links:
            bucket.append(art)
    groups[name] = bucket
    try:
        GROUPS_FILE.write_text(json.dumps(groups, indent=2))
        logging.info(f"Group '{name}' saved successfully.")
        st.success(f"Group '{name}' saved successfully.")
    except Exception as e:
        logging.error(f"Error saving group '{name}': {e}")

def remove_articles(name: str, titles: list[str]) -> int:
    logging.info(f"Removing articles from group '{name}' with titles: {titles}")
    groups = load_groups()
    bucket = groups.get(name, [])
    remaining = [a for a in bucket if a["title"] not in titles]
    removed = len(bucket) - len(remaining)
    groups[name] = remaining
    try:
        GROUPS_FILE.write_text(json.dumps(groups, indent=2))
        logging.info(f"Removed {removed} articles from group '{name}'.")
        st.success(f"Removed {removed} articles from group '{name}'.")
    except Exception as e:
        logging.error(f"Error removing articles from group '{name}': {e}")
    return removed

def remove_group(name: str):
    logging.info(f"Removing group '{name}'.")
    groups = load_groups()
    if name in groups:
        del groups[name]
        try:
            GROUPS_FILE.write_text(json.dumps(groups, indent=2))
            logging.info(f"Group '{name}' removed successfully.")
            st.success(f"Group '{name}' removed successfully.")
        except Exception as e:
            logging.error(f"Error removing group '{name}': {e}")
    else:
        logging.warning(f"Group '{name}' does not exist.")
