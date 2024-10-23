# $env:FLASK_APP = "static.py"
# $env:FLASK_DEBUG = 1
# flask run
# py -m flask run
# http://127.0.0.1:5000/

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory baza podataka (lista rečnika sa predmetima)
predmeti = [
    {'id': 1, 'predmet': 'Matematika', 'sifra': 'MAT101'},
    {'id': 2, 'predmet': 'Fizika', 'sifra': 'FIZ102'}
]

# GET metoda za dobijanje svih predmeta
@app.route('/', methods=['GET'])
@app.route('/predmeti', methods=['GET'])
def get_predmeti():
    return jsonify(predmeti)

# GET metoda za dobijanje pojedinačnog predmeta po ID-u
@app.route('/predmeti/<int:predmet_id>', methods=['GET'])
def get_predmet(predmet_id):
    predmet = next((p for p in predmeti if p['id'] == predmet_id), None)
    if predmet:
        return jsonify(predmet)
    else:
        return jsonify({'error': 'Predmet nije pronađen'}), 404

# POST metoda za kreiranje novog predmeta
@app.route('/predmeti', methods=['POST'])
def create_predmet():
    novi_predmet = request.get_json()
    novi_predmet['id'] = len(predmeti) + 1  # Automatsko postavljanje ID-a
    predmeti.append(novi_predmet)
    return jsonify(novi_predmet), 201  # Vraća status 201 (Created)

# PUT metoda za ažuriranje postojećeg predmeta
@app.route('/predmeti/<int:predmet_id>', methods=['PUT'])
def update_predmet(predmet_id):
    updated_predmet = request.get_json()
    predmet = next((p for p in predmeti if p['id'] == predmet_id), None)
    if predmet:
        predmet.update(updated_predmet)  # Ažuriraj podatke predmeta
        return jsonify(predmet)
    else:
        return jsonify({'error': 'Predmet nije pronađen'}), 404

# DELETE metoda za brisanje predmeta
@app.route('/predmeti/<int:predmet_id>', methods=['DELETE'])
def delete_predmet(predmet_id):
    global predmeti
    predmeti = [p for p in predmeti if p['id'] != predmet_id]
    return jsonify({'message': 'Predmet je obrisan'})

if __name__ == '__main__':
    app.run(debug=True)