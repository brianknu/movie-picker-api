from flask import Flask
from flask import jsonify


def create_app():
    flask_app = Flask(__name__)
    return flask_app


app = create_app()


@app.route('/api/movies', methods=['GET'])
def get_users():
    response = {'message': 'success bk9'}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
