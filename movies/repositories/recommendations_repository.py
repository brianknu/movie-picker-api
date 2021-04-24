from movies.entities.recommendation import Recommendation
from movies.entities.movie import Movie
from movies.entities.user import User


def get_all_movies(db_cl):
    all_recommendations_from_db = db_cl.find({})
    r_list = []
    for item in all_recommendations_from_db:
        movie = Movie(item.get('trailer'), item.get('description'))
        user = User(item.get('user'))
        r_list.append(Recommendation(movie, user))
    return r_list
