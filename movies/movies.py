import os
from flask import Flask
from flask import jsonify
from entities.movie import Movie
from utils.database import get_db_client
from dotenv import load_dotenv


def create_app():
    flask_app = Flask(__name__)
    return flask_app


load_dotenv()
db = get_db_client()
recommendation_collection_db = db.get_collection(os.getenv('COLLECTION_NAME'))
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
