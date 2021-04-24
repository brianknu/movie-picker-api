from flask import Flask, request, jsonify
from dotenv import load_dotenv
from movies.repositories.recommendations_repository import get_all_movies, get_random_movie, insert_recommendation
from movies.utils.database import get_db_client
from movies.utils.json_encoders import RecommendationEncoder
import os
import json


def create_app():
    flask_app = Flask(__name__)
    return flask_app


# Initial configuration
load_dotenv()
db = get_db_client()
db_cl = db.get_collection(os.getenv('COLLECTION_NAME'))
app = create_app()


# Router
@app.route('/api/movies/all', methods=['GET'])
def get_all_recommendations():
    all_rc = get_all_movies(db_cl)
    app.json_encoder = RecommendationEncoder
    return jsonify(all_rc)


@app.route('/api/movies/random', methods=['GET'])
def get_random_recommendations():
    random_movie = get_random_movie(db_cl)
    app.json_encoder = RecommendationEncoder
    return jsonify(random_movie)


@app.route('/api/movies/add', methods=['POST'])
def add_recommendations():
    request_data = json.loads(request.data.decode('utf8'))
    inserted_object_id = insert_recommendation(db_cl, request_data)
    return jsonify({"inserted object id:": inserted_object_id})


if __name__ == '__main__':
    app.run(debug=True)
