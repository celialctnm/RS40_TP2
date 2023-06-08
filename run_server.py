# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import create_engine, event, func
from flask import Flask, render_template, request, redirect, session, jsonify
import json
from flask_bcrypt import Bcrypt

# définir le message secret
SECRET_MESSAGE = "testmdp:)"  # A modifier
app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://celia:03092002@localhost/RS40'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

db2 = create_engine('mysql+mysqldb://celia:03092002@localhost/RS40')


class Utilisateurs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    passwd = db.Column(db.String(500))

    def __init__(self, nom, passwd):
        self.nom = nom
        self.passwd = passwd


class UtilisateursSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nom', 'passwd')


utilisateur_schema = UtilisateursSchema()
utilisateurs_schema = UtilisateursSchema(many=True)


@app.route('/get', methods=['GET'])
def get_user():
    all_utilisateurs = Utilisateurs.query.all()
    results = utilisateurs_schema.dump(all_utilisateurs)
    return jsonify(results)


@app.route('/add', methods=['POST'])
def add_user():
    nom = request.form['username']
    passwd = request.form['password']

    utilisateurs = Utilisateurs(nom, passwd)
    db.session.add(utilisateurs)
    db.session.commit()
    return utilisateur_schema.jsonify(utilisateurs)


'''
@app.route("/mdp")
def get_secret_message():
    return SECRET_MESSAGE
'''


app.secret_key = 'your-secret-key'  # Clé secrète pour les sessions


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Enregistrement de l'utilisateur avec le nom d'utilisateur et le mot de passe haché
        utilisateur = Utilisateurs(username, hashed_password)
        db.session.add(utilisateur)
        db.session.commit()

        return redirect('/login')  # Rediriger vers la page de connexion après l'inscription

    return render_template('register.html')

# Route pour la page de login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        utilisateur_co = ""
        password_bdd = ""
        utilisateurs = Utilisateurs.query.all()
        print("utilisateurs  : ", utilisateurs)
        for utilisateur in utilisateurs:
            if utilisateur.nom == username:
                utilisateur_co = utilisateur.nom
                password_bdd = utilisateur.passwd

        verif_mdp = bcrypt.check_password_hash(password_bdd, password)

        if username == utilisateur_co and verif_mdp == True:
            session['logged_in'] = True
            return redirect('/success')
        else:
            return redirect('/')
    return render_template('login.html')


# Route pour la page de succès après la connexion
@app.route('/success')
def success():
    if 'logged_in' in session and session['logged_in']:
        return render_template('islog.html')
    else:
        return redirect('/')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/')


if __name__ == "__main__":
    # HTTP version
    #app.run(debug=True, host="0.0.0.0", port=8082)

    # HTTPS version
    ssl_context = ("server-public-key.pem", "server-private-key.pem")
    app.run(debug=True, host="0.0.0.0", port=8081, ssl_context=ssl_context)

    # A compléter  : nécessité de déplacer les bons fichiers vers ce répertoire