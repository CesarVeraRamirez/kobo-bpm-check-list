import requests
import pandas as pd

# =========================
# Configuracion y desglose de datos
# =========================
ASSET_UID = "Insertar Asset uid personal"
BASE_URL = f"https://kf.kobotoolbox.org/api/v2/assets/{ASSET_UID}/data/"
TOKEN = "Insertar token personal"

headers = {
    "Authorization": f"Token {TOKEN}"
}

all_results = []
url = BASE_URL

# =========================
# 1. DESCARGA COMPLETA DE DATOS
# =========================
print("Conectando y descargando datos...")
while url:
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    data = r.json()
    all_results.extend(data["results"])
    url = data.get("next")

df = pd.json_normalize(all_results)

# Aqui limpiamos las columnas para que en power BI se vea el punto especifico que se va a analizar
df.columns = [c.split('/')[-1] for c in df.columns]

# ==========================================================
# NUEVO: CAMBIO MANUAL DE RESPUESTAS (A -> CUMPLE, B -> NO CUMPLE)
# ==========================================================
# Esto busca en todo el DataFrame y reemplaza los valores exactos para que en la visualizacion quede mas claro los criterios, si cumplen o no cumplen
df = df.replace({'A': 'CUMPLE', 'R': 'NO CUMPLE'})

# =========================
# 2. Obtener etiquetas a partir de etiquetass reales
# =========================
print("Obteniendo etiquetas de las preguntas...")
FORM_URL = f"https://kf.kobotoolbox.org/api/v2/assets/{ASSET_UID}/"
r_form = requests.get(FORM_URL, headers=headers)
form_data = r_form.json()

mapeo_preguntas = {}
for item in form_data.get("content", {}).get("survey", []):
    if "name" in item:
        nombre_final = item["name"].split('/')[-1]
        label = item.get("label")
        if isinstance(label, dict):
            label = label.get("Spanish") or label.get("es") or next(iter(label.values()), nombre_final)
        mapeo_preguntas[nombre_final] = str(label) if label else nombre_final

# =========================
# 3. FILTRO: Las fechas se tomaron a partir del 26 de abril para mantener confidencialidad y solo usar los datos anonimos para la prueba tecnica de github
# =========================
df["_submission_time"] = pd.to_datetime(df["_submission_time"], errors="coerce")
df = df[df["_submission_time"] >= "2026-04-26"]

# =========================
# 4. LIMPIEZA Y RENOMBRADO DE DATOS
# =========================
df.columns = df.columns.str.replace(".", "_")

if not df.empty:
    df["mes"] = df["_submission_time"].dt.to_period("M").astype(str)

df.rename(columns=mapeo_preguntas, inplace=True)

# =========================
# 5. EXPORTAR
# =========================
df.to_excel("kobo_data_completo.xlsx", index=False)

print("✔ Filtrado de BPM prueba tecnica aplicado desde 26 de abril 2026")
print("✔ Respuestas convertidas: A -> CUMPLE, B -> NO CUMPLE")
print("✔ Filas exportadas:", len(df))