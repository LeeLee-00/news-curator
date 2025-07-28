class Entry:
    def __init__(self, title=None, link=None, guid=None, pub_date=None, description=None, source=None, source_url=None):
        self.title = title
        self.link = link
        self.guid = guid
        self.pub_date = pub_date
        self.description = description
        self.source = source
        self.source_url = source_url

    def __repr__(self):
        return (
            f"Entry(title={self.title!r}, link={self.link!r}, guid={self.guid!r}, "
            f"pub_date={self.pub_date!r}, description={self.description!r}, "
            f"source={self.source!r}, source_url={self.source_url!r})"
        )
    
class SearchParams:
    def __init__(self, search_type, query_term, time_span):
        self.time_span = time_span
        self.search_type = search_type 
        self.query_term = query_term