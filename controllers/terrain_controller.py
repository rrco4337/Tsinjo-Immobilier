from flask import Blueprint, render_template, request
from modele import predict_price

terrain_bp = Blueprint('terrain', __name__)

@terrain_bp.route('/terrain', methods=['GET', 'POST'])
def formulaire_terrain():
    if request.method == 'POST':
        donnees = {
            "surface": int(request.form['surface']),
            "acces": int(request.form['acces']),
            "typePapier": request.form['typePapier'],
            "pretBatir": request.form['pretBatir'],
            "cloture": request.form['cloture'],
            "latitude": float(request.form['latitude']),
            "longitude": float(request.form['longitude'])
        }
        prix = predict_price(donnees)
        return render_template('resultat.html', prix=prix)

    return render_template('formulaire.html')
