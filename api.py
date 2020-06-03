from flask import Flask, jsonify, request

app = Flask(__name__) #Inicializa a aplicação

devs = [
    {'id': 1, 'name': 'Ana Paula', 'lang': 'Java'},
    {'id': 2, 'name': 'Marcio', 'lang': 'Python'},
    {'id': 3, 'name': 'Antonio', 'lang': 'R'}
]

@app.route('/index')
def index():
    return "Bem vindo a nossa API", 200

@app.route('/list_devs')
def lista_devs():
    return jsonify(devs), 200

@app.route('/dev/<int:id>')
def get_dev(id):
    for dev in devs:
        if dev['id'] == id:
            return jsonify(dev), 200
    return jsonify({'error': 'id {} not found'.format(id)}), 404

@app.route('/dev', methods=['POST'])
def create_dev():
    data = request.get_json()
    devs.append(data)
    return jsonify(data), 201

@app.route('/dev/<int:id>', methods=['DELETE'])
def remove_dev(id):
    for dev in devs:
        if dev['id'] == id:
            devs.remove(dev)
            return jsonify({'message': 'dev removido com sucesso'}, dev), 200
    return jsonify({'error': 'id {} not found'.format(id)}), 404

@app.route('/dev/<int:id>', methods=['PUT'])
def update_dev(id):
    for dev in devs:
        if dev['id'] == id:
            dev = [{'id': 1, 'name': 'Ana Paula', 'lang': 'JS'}]
            return jsonify({'message': 'dev atualizado com sucesso'}, dev), 200
    return jsonify({'error': 'id {} not found'.format(id)}), 404

if __name__ == '__main__':
    app.run(debug=True)