from flask import Flask
from controllers.main_controller import main_bp
from controllers.user_controller import auth_bp
from controllers.terrain_controller import terrain_bp


from config import Config  # Importe la configuration

# Création de l'application Flask
app = Flask(__name__)

# Charge la configuration depuis config.py
app.config.from_object(Config)

# Enregistrement des Blueprints (controllers)
app.register_blueprint(main_bp) 

app.register_blueprint(auth_bp)

app.register_blueprint(terrain_bp)

# Point d'entrée pour démarrer l'application
if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])