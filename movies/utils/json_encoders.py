from json import JSONEncoder


class RecommendationEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
