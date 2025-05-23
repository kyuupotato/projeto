from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests
from fastapi import FastAPI, Request


app = FastAPI()
templates = Jinja2Templates(directory="templates")

GEOAPIFY_API_KEY = "72e7cd6225a947ae92bb11cf1a774249"

def buscar_lugares(term, lat, lon, raio=5000):
    url = "https://api.geoapify.com/v2/places"
    params = {
        "categories": "catering.restaurant",
        "filter": f"circle:{lon},{lat},{raio}",
        "bias": f"proximity:{lon},{lat}",
        "limit": 10,
        "lang": "pt",
        "name": term,
        "apiKey": GEOAPIFY_API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        features = response.json().get("features", [])
        return [
            {
                "name": f["properties"].get("name", "Sem nome"),
                "endereco": f["properties"].get("formatted", "Sem endereço"),
                "lat": f["properties"]["lat"],
                "lon": f["properties"]["lon"]
            }
            for f in features
        ]
    else:
        return []

@app.get("/", response_class=HTMLResponse)
def form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/buscar", response_class=HTMLResponse)
async def buscar(request: Request, termo: str = Form(...)):
    lat = -23.6029545  # Cotia
    lon = -46.9190217
    lugares = buscar_lugares(termo, lat, lon)
    return templates.TemplateResponse("resultados.html", {
        "request": request,
        "termo": termo,
        "lugares": lugares
    })
