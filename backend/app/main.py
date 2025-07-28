from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from shared_models.classes import SearchParams
from app.query_logic import query
from enum import Enum

app = FastAPI()

class SearchParamsRequest(BaseModel):
    search_type: str= "allintitle"
    query_term: str
    time_span: str

@app.post("/search")
async def search_news(params: SearchParamsRequest):
    try:
        search_params = SearchParams(
            search_type=params.search_type,
            query_term=params.query_term,
            time_span=params.time_span
        )
        # print(f"Search Parameters - Search Type: {search_params.search_type}, Query Term: {search_params.query_term}, Time Span: {search_params.time_span}")
        results = query(search_params)
        # print("results", results)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
