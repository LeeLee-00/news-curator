import requests
from bs4 import BeautifulSoup
from shared_models.classes import Entry, SearchParams

def create_entry_from_item(item):
    return Entry(
        title=item.title.text if item.title else None,
        link=item.link.text if item.link else None,
        guid=item.guid.text if item.guid else None,
        pub_date=item.pubDate.text if item.pubDate else None,
        description=item.description.text if item.description else None,
        source=item.source.text if item.source else None,
        source_url=item.source["url"] if item.source and item.source.has_attr("url") else None,
    )

def make_request(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'xml')  # Assuming the response is in XML format
    return soup

def make_url(params):
    return f"https://news.google.com/rss/search?q={params.search_type}:{params.query_term}+when:{params.time_span}&hl=en-US&gl=US&ceid=US:en"


def parse_xlml_to_dict(xlml):
    entries = []
    for item in xlml.find_all("item"):
        entry = create_entry_from_item(item)
        entries.append(entry)
    return entries

def query(params: SearchParams):
    url = make_url(params)
    xlml_soup = make_request(url)
    return parse_xlml_to_dict(xlml_soup)