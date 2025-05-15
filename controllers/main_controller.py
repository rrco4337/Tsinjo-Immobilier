from flask import Blueprint, render_template

import joblib

main_bp = Blueprint('main', __name__)



@main_bp.route('/acceuil')
def acceuil():
  
    return render_template('acceuil.html')

@main_bp.route('/maison')
def maison_critere():
  
    return render_template('maison.html')

@main_bp.route('/terrain')
def terrain_critere():
  
    return render_template('terrain.html')



