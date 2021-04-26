from movies.repositories.recommendations_repository import get_all_movies, get_random_movie, insert_recommendation, \
    delete_recommendation, get_recommendation_by_id
from movies.utils.database import get_db_client
from movies.utils.json_encoders import RecommendationEncoder
