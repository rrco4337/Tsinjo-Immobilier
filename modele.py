import pandas as pd
from sklearn.linear_model import LinearRegression

# Données d'entraînement
donnees_terrains = [
    {"surface": 500, "acces": 3, "typePapier": "Titre Foncier", "pretBatir": "Oui", "cloture": "Oui", "latitude": -18.8792, "longitude": 47.5079, "prix": 80000000},
    {"surface": 300, "acces": 1, "typePapier": "Certificat Foncier", "pretBatir": "Non", "cloture": "Non", "latitude": -20.2974, "longitude": 44.3174, "prix": 30000000},
    {"surface": 800, "acces": 2, "typePapier": "Lettre d’Attribution", "pretBatir": "Oui", "cloture": "Oui", "latitude": -18.9137, "longitude": 47.5361, "prix": 60000000},
    {"surface": 600, "acces": 3, "typePapier": "Titre Foncier", "pretBatir": "Oui", "cloture": "Non", "latitude": -19.8723, "longitude": 47.0381, "prix": 70000000},
    {"surface": 400, "acces": 2, "typePapier": "Aucun", "pretBatir": "Non", "cloture": "Non", "latitude": -21.4266, "longitude": 47.0857, "prix": 25000000}
]

mapping_papier = {
    "Titre Foncier": 3,
    "Certificat Foncier": 2,
    "Lettre d’Attribution": 1,
    "Aucun": 0
}

def encoder(d):
    return {
        "surface": d["surface"],
        "acces": d["acces"],
        "typePapier": mapping_papier[d["typePapier"]],
        "pretBatir": 1 if d["pretBatir"] == "Oui" else 0,
        "cloture": 1 if d["cloture"] == "Oui" else 0,
        "latitude": d["latitude"],
        "longitude": d["longitude"]
    }

# Entraînement
df = pd.DataFrame([encoder(d) | {"prix": d["prix"]} for d in donnees_terrains])
X = df.drop(columns="prix")
y = df["prix"]
model = LinearRegression()
model.fit(X, y)

def predict_price(donnee_form):
    donnees_encodees = pd.DataFrame([encoder(donnee_form)])
    return int(model.predict(donnees_encodees)[0])
