import os
from flask import Flask
import connexion
import flask_sqlalchemy
from config import db, ma

# instance the App
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

@app.route('/healthz')
def healthz_check():
    db.session.execute('SELECT 1')
    return 'The app is able to connecto to the DB'

if __name__ == '__main__':
#    print(config['host']['host'], config['host']['port'])
    app.run(debug=True,host=os.getenv('LISTEN_HOST'),port=os.getenv('LISTEN_PORT'))
