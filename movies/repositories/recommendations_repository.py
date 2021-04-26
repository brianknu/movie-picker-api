from bson import ObjectId
from movies.entities.recommendation import Recommendation
from movies.entities.movie import Movie
from movies.entities.user import User


def get_all_movies(db_cl):
    all_recommendations_from_db = db_cl.find({})
    r_list = []
    for item in all_recommendations_from_db:
        movie_id = str(item['_id'])
        movie = Movie(item['trailer'], item['description'])
        user = User(item['user'])
        r_list.append(Recommendation(movie, user, movie_id))
    return r_list


def get_random_movie(db_cl):
    random_movie_cursor = db_cl.aggregate([{'$sample': {'size': 1}}])
    random_movie = next(random_movie_cursor)
    random_movie_id = str(random_movie['_id'])
    movie = Movie(random_movie['trailer'], random_movie['description'])
    user = User(random_movie['user'])
    return Recommendation(movie, user, random_movie_id)


def insert_recommendation(db_cl, request_data):
    recommendation = Recommendation(Movie(request_data['trailer'], request_data['description']),
                                    User(request_data['user']))
    dic = {
        "user": recommendation.user.name,
        "description": recommendation.movie.description,
        "trailer": recommendation.movie.trailer
    }

    return db_cl.insert_one(dic)


def delete_recommendation(db_cl, movie_id):
    result = db_cl.delete_one({'_id': ObjectId(movie_id)})
    return result.deleted_count


def get_recommendation_by_id(db_cl, recommendation_id):
    recommendation = db_cl.find_one({'_id': ObjectId(recommendation_id)})
    movie = Movie(recommendation['trailer'], recommendation['description'])
    user = User(recommendation['user'])
    return Recommendation(movie, user, recommendation_id)
