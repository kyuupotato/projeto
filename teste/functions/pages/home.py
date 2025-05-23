
import streamlit as st
import requests

# Sua chave da API do Geoapify (insira a real aqui)
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
        return response.json().get("features", [])
    else:
        st.error("Erro ao buscar lugares.")
        return []

def run():
    st.title("🔍 Buscar Lugares em Cotia-SP")
    st.write("Digite um termo de busca para encontrar locais próximos (ex: pizzaria, farmácia, mercado).")

    termo = st.text_input("O que você está procurando?", "pizzaria")

    # Localização fixa: Cotia-SP
    lat = -23.6029545
    lon = -46.9190217

    if st.button("Buscar"):
        lugares = buscar_lugares(termo, lat, lon)
        if lugares:
            for lugar in lugares:
                props = lugar["properties"]
                st.subheader(props.get("name", "Sem nome"))
                st.write(props.get("formatted", "Sem endereço"))
                st.map({"lat": [props["lat"]], "lon": [props["lon"]]})
        else:
            st.warning("Nenhum lugar encontrado.")
