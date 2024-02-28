from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# definindo local dos templates (página index.html está aqui)
templates = Jinja2Templates(directory='temp')

# iniciando aplicação
app = FastAPI()

# definindo a rota para a página inicial
@app.get("/", response_class=HTMLResponse)
def reed_root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html",
    )