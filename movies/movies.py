from flask import Flask
from flask import jsonify
from entities.movie import Movie


def create_app():
    flask_app = Flask(__name__)
    return flask_app


app = create_app()


@app.route('/api/movies', methods=['GET'])
def get_movies():
    example = Movie("example link", "description example")
    response = {'message': example.print_movie()}
    return jsonify(response)


@app.route('/api/movies/random', methods=['GET'])
def get_random_movie():
    example = Movie("example link", "description example")
    response = {'message': example.print_movie()}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
