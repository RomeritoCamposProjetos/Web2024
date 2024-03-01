from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory='temp')

app = FastAPI()

@app.route('/')
def read_root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )