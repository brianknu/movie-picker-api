from movies.entities.recommendation import Recommendation
from movies.entities.movie import Movie
from movies.entities.user import User
from random import randrange


def get_all_movies(db_cl):
    all_recommendations_from_db = db_cl.find({})
    r_list = []
    for item in all_recommendations_from_db:
        movie = Movie(item.get('trailer'), item.get('description'))
        user = User(item.get('user'))
        r_list.append(Recommendation(movie, user))
    return r_list


def get_random_movie(db_cl):
    count = db_cl.count_documents({})
    random_index = (randrange(count))
    random_movie = db_cl.find().limit(-1).skip(random_index).next()
    movie = Movie(random_movie.get('trailer'), random_movie.get('description'))
    user = User(random_movie.get('user'))
    return Recommendation(movie, user)


def insert_recommendation(db_cl, request_data):
    recommendation = Recommendation(Movie(request_data.get('trailer'), request_data.get('description')),
                                    User(request_data.get('user')))
    dic = {
        "user": recommendation.user.name,
        "description": recommendation.movie.description,
        "trailer": recommendation.movie.trailer
    }

    return db_cl.insert_one(dic)
