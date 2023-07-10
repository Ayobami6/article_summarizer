from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from services.openai_service import OpenAIService
from services.scraping_service import ScrapingService

# create an app instance from FastApi
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# create a data class for data validation


class Data(BaseModel):
    url: str


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/summarize")
def summarize_content(data: Data) -> str:
    scrape_service = ScrapingService()
    openai_service = OpenAIService()
    # Scrape the content
    content = scrape_service.scrape_content(data.url)
    # summarize with openai
    try:
        summarized_content = openai_service.summarize_and_explain(content)
    except Exception as e:
        return str(e)
    return summarized_content
