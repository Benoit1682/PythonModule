from flask import Flask
import pymysql

app = Flask(__name__)

# Configuration de la base de données
app.config['DB'] = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'benoit_fournier_expi1a_mpd'
}

# Route pour afficher les données de la base de données
db = pymysql.connect(
        host=app.config['DB']['host'],
        user=app.config['DB']['user'],
        password=app.config['DB']['password'],
        database=app.config['DB']['database']
    )

cursor = db.cursor()
cursor.execute("SELECT * FROM t_personne")
rows = cursor.fetchall()

cursor.close()
db.close()

for row in rows:
        print("Chier module 164",row)