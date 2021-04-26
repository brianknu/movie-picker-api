import os
import json
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from utils.database import get_db_client
from utils.json_encoders import RecommendationEncoder
from movies.repositories.recommendations_repository import get_all_movies, get_random_movie, insert_recommendation, \
    delete_recommendation, get_recommendation_by_id


def create_app():
    flask_app = Flask(__name__)
    return flask_app


# Initial configuration
load_dotenv()
db = get_db_client()
db_cl = db.get_collection(os.getenv('COLLECTION_NAME'))
app = create_app()


# Router
@app.route('/recommendations', methods=['GET'])
def get_all_recommendations_endpoint():
    all_rc = get_all_movies(db_cl)
    app.json_encoder = RecommendationEncoder
    return jsonify(all_rc)


@app.route('/recommendations/random', methods=['GET'])
def get_random_recommendations_endpoint():
    random_movie = get_random_movie(db_cl)
    app.json_encoder = RecommendationEncoder
    return jsonify(random_movie)


@app.route('/recommendations', methods=['POST'])
def add_recommendations_endpoint():
    request_data = json.loads(request.data.decode('utf8'))
    insert_recommendation(db_cl, request_data)
    return jsonify({"Message": "ok"})


@app.route('/recommendations/<movie_id>', methods=['DELETE'])
def delete_recommendations(movie_id):
    deleted_count = delete_recommendation(db_cl, movie_id)
    return jsonify({"Deleted count": str(deleted_count)})


@app.route('/recommendations/<movie_id>', methods=['GET'])
def get_recommendation_by_id_endpoint(movie_id):
    rc = get_recommendation_by_id(db_cl, movie_id)
    app.json_encoder = RecommendationEncoder
    return jsonify(rc)


if __name__ == '__main__':
    app.run(debug=True)
