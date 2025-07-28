import json, logging
from pathlib import Path

TERMS_FILE = Path("shared_models/terms.json")

def load_terms() -> list[str]:
    try:
        return json.loads(TERMS_FILE.read_text())
    except Exception as e:
        logging.error(f"Error loading terms: {e}")
        return []

def save_terms(terms: list[str]) -> None:
    try:
        TERMS_FILE.write_text(json.dumps(terms, indent=2))
        logging.info("Saved terms successfully.")
    except Exception as e:
        logging.error(f"Error saving terms: {e}")
