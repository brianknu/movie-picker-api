class Recommendation:
    def __init__(self, movie, user, mongo_id=None):
        self.movie = movie
        self.user = user
        self.mongo_id = mongo_id
