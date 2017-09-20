from flask import Flask, jsonify
app = Flask(__name__)

people = {1: {'name': 'sunny', 'likes': 'coffee'}}


@app.route('/hello/<string:name>')
def hello_world():
    # return jsonify({'msg': 'Hello, World!'})
    return 'hello {}'.format(name)


@app.route('/people/<int:id>')
def get_people(id):
    return jsonify({'person': people[id]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
