# RS40_TP2

## Installation préalable

### Librairies python nécessaires

```
pip install flask_sqlalchemy
pip install flask_marshmallow
pip install sqlalchemy
pip install flask
pip install flask_bcrypt
pip install mysqlclient
```

### Création d'une database

````
Créer une base de données 'RS40'
Créer une table 'Utilisateurs'
  id -- int(11) -- auto_increment
  nom -- varchar(100) --
  passwd -- varchar(500) -- 
````

### Changement URL Flask (run_server.py)

Remplacer ces deux lignes 

````
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://celia:03092002@localhost/RS40'
db2 = create_engine('mysql+mysqldb://celia:03092002@localhost/RS40')
````

Par vos identifiants, par exemple

```
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/RS40'
mysql://username:password@server/db

db2 = create_engine('mysql+mysqldb://root:''@localhost/RS40')
dialect+driver://username:password@host:port/database
```

Pour plus d'info, vous pouvez consulter cette page 
https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/ 
