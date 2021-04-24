class Movie:
    def __init__(self, link, description):
        self.link = link
        self.description = description

    def print_movie(self):
        return f"Link: {self.link} Description: {self.description}."
